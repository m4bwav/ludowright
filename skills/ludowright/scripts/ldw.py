#!/usr/bin/env python3
"""ludowright's counting tool. Judgment stays with the model; this script checks and counts.

  findings validate FILE        check a findings file against the contract (exit 1 on errors)
  findings md FILE [-o OUT]     the readable markdown view of a findings file
  findings new --game NAME      print an empty findings file to fill
  ev TABLE                      expected value, spread and odds of a weighted outcome table
  curve TABLE                   fit a cost curve over items and flag over- and under-costed ones
  economy TABLE                 source and sink totals per period, net flow, leak and drain flags
  sim TABLE --steps N           Monte Carlo over a declared table (draws, deltas or a deck)
  draw --deck D --copies C --drawn N   hypergeometric odds of drawing copies of a card
  ramp TABLE [--steps N]        difficulty ramp check: UNCAPPED, FLOOR@n / CAP@n, FLAT-EARLY
  stop TABLE                    stop-or-continue check: best settle threshold, FIRST-IS-BEST / NEVER-STOP / FLAT
  director TABLE --days N       event schedule from comps: gaps, clumps, first threat, budget; NO-BREATHER / CLUMP / RUNAWAY
  mood TABLE --hours N          stacked-modifier meter seeking a target: hours below threshold; UNCAPPED / SPIKE / OSCILLATES
  grammar TABLE --root SYM      text grammar check: UNDEFINED, UNREACHABLE, DEAD-UNDER, RECURSIVE, LOW-VARIETY
  growth TABLE                  deck size per stage against a target band: BLOAT, OFF-BAND, NO-THIN; resource STARVED / FLOODED
  quota TABLE                   rising payments against an income ramp: slack per payment; TIGHT, LOOSE, CLIFF

Tables are JSON or CSV. Shapes are in kb/balance-tables.md. Standard library only; Python 3.9+.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import os
import random
import re
import statistics
import sys

VERSION = "0.1.55"
FORMAT = "ludowright-findings"
FORMAT_VERSION = "1.1"
SEVERITIES = ("critical", "major", "minor", "note")
CATEGORIES = ("dominant-strategy", "degenerate-loop", "dead-choice", "economy-leak", "difficulty-spike",
              "onboarding-gap", "pacing", "scope-risk", "broken-promise", "balance", "progression", "clarity",
              "uncertainty", "level-design", "ai-behaviour", "feel", "other")
KINDS = ("review", "improve", "design-check")
LEVELS = ("high", "medium", "low")
EFFORTS = ("S", "M", "L")
STAGES = ("concept", "prototype", "in-development", "shipped", "live")
BUILT = ("no", "partial")
ID_RE = re.compile(r"^F-\d{3,}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def fail(msg, code=2):
    print(msg, file=sys.stderr)
    sys.exit(code)


def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError) as e:
        fail(f"cannot read {path}: {e}")


# ---------------------------------------------------------------- findings contract

def validate_findings(doc):
    """Errors and warnings for a findings document. The contract is README.md 'Findings contract'."""
    errs, warns = [], []
    if not isinstance(doc, dict):
        return ["top level is not an object"], warns
    if doc.get("format") != FORMAT:
        errs.append(f"format must be {FORMAT!r}")
    ver = str(doc.get("version", ""))
    if not re.match(r"^1\.\d+$", ver):
        errs.append(f"version {ver!r} is not a 1.x version this validator reads")
    for k in ("game", "kind", "date", "findings"):
        if k not in doc:
            errs.append(f"missing {k}")
    if doc.get("kind") not in KINDS:
        errs.append(f"kind must be one of {', '.join(KINDS)}")
    if "date" in doc and not DATE_RE.match(str(doc["date"])):
        errs.append("date must be YYYY-MM-DD")
    if "stage" in doc and doc["stage"] not in STAGES:
        errs.append(f"stage must be one of {', '.join(STAGES)}")
    if not isinstance(doc.get("sources_read", []), list):
        errs.append("sources_read must be a list")
    elif not doc.get("sources_read"):
        warns.append("sources_read is empty: say what was read")
    fs = doc.get("findings")
    if not isinstance(fs, list):
        errs.append("findings must be a list")
        return errs, warns
    seen = set()
    for i, f in enumerate(fs):
        where = f"findings[{i}]"
        if not isinstance(f, dict):
            errs.append(f"{where} is not an object")
            continue
        fid = f.get("id")
        where = f"{fid or where}"
        if not isinstance(fid, str) or not ID_RE.match(fid):
            errs.append(f"{where}: id must look like F-001")
        elif fid in seen:
            errs.append(f"{where}: duplicate id")
        seen.add(fid)
        for k in ("severity", "category", "title", "location", "principle", "evidence", "suggestion"):
            if not f.get(k):
                errs.append(f"{where}: missing {k}")
        if f.get("severity") and f["severity"] not in SEVERITIES:
            errs.append(f"{where}: severity must be one of {', '.join(SEVERITIES)}")
        if f.get("category") and f["category"] not in CATEGORIES:
            errs.append(f"{where}: unknown category {f['category']!r}")
        loc = f.get("location")
        if loc is not None:
            if not isinstance(loc, dict) or not loc.get("file"):
                errs.append(f"{where}: location needs a file (a path, or 'design' for a pitch with no files)")
            elif not any(loc.get(k) for k in ("section", "line", "rule", "symbol")):
                warns.append(f"{where}: location has a file but no section, line, rule or symbol")
        pr = f.get("principle")
        if pr is not None:
            if not isinstance(pr, dict) or not pr.get("name"):
                errs.append(f"{where}: principle needs a name")
            elif not pr.get("source"):
                warns.append(f"{where}: principle has no source (a kb file or a book citation)")
        if isinstance(f.get("evidence"), str) and len(f["evidence"]) < 20:
            warns.append(f"{where}: evidence is under 20 characters; quote the rule, number or line")
        for k, allowed in (("impact", LEVELS), ("confidence", LEVELS), ("effort", EFFORTS)):
            if k in f and f[k] not in allowed:
                errs.append(f"{where}: {k} must be one of {', '.join(allowed)}")
        if "built" in f and f["built"] not in BUILT:
            errs.append(f"{where}: built must be one of {', '.join(BUILT)}")
        if doc.get("kind") == "improve" and ("impact" not in f or "effort" not in f):
            errs.append(f"{where}: an improve file ranks by impact and effort; both are required")
        if f.get("category") == "feel" and f.get("handoff") != "juice-scan":
            warns.append(f"{where}: a feel finding should hand off to juice-scan (handoff: juice-scan)")
    return errs, warns


def rank_key(f):
    sev = {s: i for i, s in enumerate(SEVERITIES)}.get(f.get("severity"), 9)
    imp = {"high": 0, "medium": 1, "low": 2}.get(f.get("impact"), 1)
    eff = {"S": 0, "M": 1, "L": 2}.get(f.get("effort"), 1)
    return (sev, imp, eff, f.get("id", ""))


def findings_md(doc):
    fs = sorted(doc.get("findings", []), key=rank_key)
    title = {"review": "Design review", "improve": "Improvement list", "design-check": "Design check"}.get(doc.get("kind"), "Findings")
    out = [f"# {title}: {doc.get('game', '?')}", "",
           f"{doc.get('date', '')} · {len(fs)} findings · format {doc.get('format')} {doc.get('version')}"]
    if doc.get("summary"):
        out += ["", doc["summary"]]
    counts = {s: sum(1 for f in fs if f.get("severity") == s) for s in SEVERITIES}
    line = " · ".join(f"{s} {n}" for s, n in counts.items() if n)
    unbuilt = sum(1 for f in fs if f.get("built"))
    if unbuilt:
        line += f" · {unbuilt} of them on parts not built yet"
    if doc.get("stage"):
        line = f"Stage: {doc['stage']} · " + line
    out += ["", line]
    out += ["", "| ID | Severity | Category | Finding | Impact | Effort |", "|---|---|---|---|---|---|"]
    for f in fs:
        tag = " (not built yet)" if f.get("built") == "no" else " (partly built)" if f.get("built") == "partial" else ""
        out.append(f"| {f.get('id')} | {f.get('severity')} | {f.get('category')} | {f.get('title')}{tag} | {f.get('impact', '')} | {f.get('effort', '')} |")
    for f in fs:
        loc = f.get("location") or {}
        where = loc.get("file", "")
        for k in ("section", "rule", "symbol", "line"):
            if loc.get(k):
                where += f" {k} {loc[k]}"
        pr = f.get("principle") or {}
        out += ["", f"## {f.get('id')} · {f.get('title')}", "",
                f"- Severity: {f.get('severity')} · category: {f.get('category')}" + (f" · confidence: {f['confidence']}" if f.get("confidence") else ""),
                f"- Where: {where}",
                *([f"- Built: {f['built']} (a gap in the build, not a flaw in the design as written)"] if f.get("built") else []),
                f"- Principle: {pr.get('name', '')}" + (f" ({pr['source']})" if pr.get("source") else ""),
                f"- Evidence: {f.get('evidence', '')}",
                f"- Suggestion: {f.get('suggestion', '')}"]
        if f.get("handoff"):
            out.append(f"- Hand off to: {f['handoff']}")
    if doc.get("sources_read"):
        out += ["", "## Read", ""] + [f"- {s}" for s in doc["sources_read"]]
    return "\n".join(out) + "\n"


def cmd_findings(a):
    if a.action == "new":
        print(json.dumps({"format": FORMAT, "version": FORMAT_VERSION, "game": a.game or "", "kind": a.kind,
                          "date": __import__("datetime").date.today().isoformat(), "sources_read": [], "summary": "",
                          "findings": []}, indent=2))
        return 0
    doc = load_json(a.file)
    errs, warns = validate_findings(doc)
    if a.action == "validate":
        for e in errs:
            print(f"ERROR {e}")
        for w in warns:
            print(f"warn  {w}")
        n = len(doc.get("findings", [])) if isinstance(doc, dict) else 0
        print(f"{'OK' if not errs else 'INVALID'}: {n} findings, {len(errs)} errors, {len(warns)} warnings")
        return 1 if errs else 0
    if errs:
        print("refusing to render an invalid file; run `findings validate` first", file=sys.stderr)
        return 1
    text = findings_md(doc)
    if a.out:
        with open(a.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(a.out)
    else:
        sys.stdout.write(text)
    return 0


# ---------------------------------------------------------------- tables

def load_table(path):
    """A JSON object (with a 'rows' list and settings) or list of rows, or a CSV (rows only). Numbers are parsed."""
    if path.lower().endswith(".csv"):
        with open(path, encoding="utf-8-sig", newline="") as f:
            rows = [{k.strip(): num(v) for k, v in r.items() if k} for r in csv.DictReader(f)]
        return {"rows": rows}
    doc = load_json(path)
    if isinstance(doc, list):
        doc = {"rows": doc}
    doc["rows"] = [{k: num(v) for k, v in r.items()} for r in doc.get("rows", [])]
    return doc


def num(v):
    if isinstance(v, (int, float)) or v is None:
        return v
    s = str(v).strip()
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s


def fmt(x):
    return f"{x:.4g}" if isinstance(x, float) else str(x)


def ev_stats(rows):
    tot = sum(float(r.get("weight", 1)) for r in rows)
    if tot <= 0:
        fail("weights sum to zero")
    ps = [float(r.get("weight", 1)) / tot for r in rows]
    vs = [float(r["value"]) for r in rows]
    mean = sum(p * v for p, v in zip(ps, vs))
    var = sum(p * (v - mean) ** 2 for p, v in zip(ps, vs))
    return {"outcomes": len(rows), "ev": mean, "sd": math.sqrt(var), "min": min(vs), "max": max(vs),
            "p": [{"outcome": r.get("outcome", i), "p": p, "value": v} for i, (r, p, v) in enumerate(zip(rows, ps, vs))]}


def cmd_ev(a):
    t = load_table(a.table)
    s = ev_stats(t["rows"])
    if a.json:
        print(json.dumps(s, indent=1))
        return 0
    print(f"{s['outcomes']} outcomes · EV {fmt(s['ev'])} · SD {fmt(s['sd'])} · range {fmt(s['min'])}..{fmt(s['max'])}")
    for r in s["p"]:
        print(f"  {str(r['outcome']):<24} p {r['p']:.3f}  value {fmt(r['value'])}")
    return 0


def solve(ata, atb):
    """Gaussian elimination with partial pivoting; returns None when singular."""
    n = len(ata)
    m = [row[:] + [atb[i]] for i, row in enumerate(ata)]
    for c in range(n):
        piv = max(range(c, n), key=lambda r: abs(m[r][c]))
        if abs(m[piv][c]) < 1e-12:
            return None
        m[c], m[piv] = m[piv], m[c]
        for r in range(n):
            if r != c:
                f = m[r][c] / m[c][c]
                m[r] = [x - f * y for x, y in zip(m[r], m[c])]
    return [m[i][n] / m[i][i] for i in range(n)]


def fit_curve(rows, attrs, cost_key="cost"):
    """Least squares: cost ~ intercept + sum(w_k * attr_k). Returns weights and per-item residuals."""
    X = [[1.0] + [float(r.get(k) or 0) for k in attrs] for r in rows]
    y = [float(r[cost_key]) for r in rows]
    n = len(X[0])
    ata = [[sum(x[i] * x[j] for x in X) for j in range(n)] for i in range(n)]
    for i in range(1, n):
        ata[i][i] += 1e-9  # a whisker of ridge keeps a column of zeros from being singular
    atb = [sum(x[i] * yy for x, yy in zip(X, y)) for i in range(n)]
    w = solve(ata, atb)
    if w is None:
        return None
    items = []
    for r, x, yy in zip(rows, X, y):
        pred = sum(a * b for a, b in zip(w, x))
        items.append({"name": r.get("name", "?"), "cost": yy, "fair": pred, "delta": yy - pred,
                      "ratio": (pred / yy) if yy else None})
    resid = [i["delta"] for i in items]
    sd = statistics.pstdev(resid) if len(resid) > 1 else 0.0
    ss_res = sum(d * d for d in resid)
    mean_y = sum(y) / len(y)
    ss_tot = sum((v - mean_y) ** 2 for v in y)
    return {"intercept": w[0], "weights": dict(zip(attrs, w[1:])), "items": items, "resid_sd": sd,
            "r2": 1 - ss_res / ss_tot if ss_tot else 1.0}


def parse_rates(spec):
    """'gold:1,wood:0.5' -> {'gold': 1.0, 'wood': 0.5}: each cost column's worth in the base currency."""
    rates = {}
    for part in spec.split(","):
        k, _, v = part.partition(":")
        try:
            rates[k.strip()] = float(v) if v else 1.0
        except ValueError:
            fail(f"--costs wants column:rate pairs, got {part!r}")
    return rates


def cmd_curve(a):
    t = load_table(a.table)
    rows = t["rows"]
    rates = parse_rates(a.costs) if a.costs else t.get("costs")
    if rates:
        rows = [dict(r, cost=sum(float(r.get(k) or 0) * v for k, v in rates.items())) for r in rows]
    skip = {"name", "cost"} | set(rates or {})
    attrs = a.attrs.split(",") if a.attrs else t.get("attrs") or [k for k in rows[0] if k not in skip and isinstance(rows[0][k], (int, float))]
    if len(rows) < len(attrs) + 2:
        fail(f"{len(rows)} items cannot fit {len(attrs)} attributes and an intercept; add items or drop attributes")
    fit = fit_curve(rows, attrs)
    if fit is None:
        fail("the attributes are collinear; drop one")
    tol = a.tolerance
    flagged = []
    for it in fit["items"]:
        rel = it["delta"] / it["fair"] if it["fair"] else 0
        it["flag"] = "UNDER-COSTED" if rel < -tol else "OVER-COSTED" if rel > tol else ""
        if it["flag"]:
            flagged.append(it)
    if a.json:
        print(json.dumps(dict(fit, tolerance=tol, flagged=len(flagged)), indent=1))
        return 0
    ws = ", ".join(f"{k} {fmt(v)}" for k, v in fit["weights"].items())
    print(f"{len(rows)} items · cost = {fmt(fit['intercept'])} + {ws} · R2 {fit['r2']:.3f} · tolerance {tol:.0%}")
    for it in sorted(fit["items"], key=lambda i: i["delta"]):
        print(f"  {str(it['name']):<24} cost {fmt(it['cost']):>7} fair {fmt(it['fair']):>7}  {it['flag']}")
    if fit["r2"] < 0.5:
        print("note: R2 under 0.5; the attributes miss what the costs price in (a situational effect, synergy or a missing column)")
    return 0


def economy(t, periods):
    """Flows per resource: rows {resource, kind: source|sink, amount, per?: period|use, uses?: n, start?}."""
    res = {}
    for r in t["rows"]:
        name = r.get("resource", "?")
        e = res.setdefault(name, {"source": 0.0, "sink": 0.0, "start": 0.0, "items": []})
        amt = float(r.get("amount") or 0) * float(r.get("uses") or 1)
        if r.get("kind") == "start":
            e["start"] += amt
            continue
        if r.get("kind") not in ("source", "sink"):
            fail(f"row {r}: kind must be source, sink or start")
        e[r["kind"]] += amt
        e["items"].append((r["kind"], r.get("name", ""), amt))
    caps = t.get("caps", {})
    out = {}
    for name, e in res.items():
        net = e["source"] - e["sink"]
        end = e["start"] + net * periods
        flags = []
        if net > 0 and name not in caps:
            flags.append("LEAK: grows without a sink to match and no cap")
        if net > 0 and name in caps and end > caps[name]:
            flags.append(f"CAP: reaches the cap of {caps[name]} by period {math.ceil((caps[name] - e['start']) / net)}")
        if net < 0 and end < 0:
            flags.append(f"DRAIN: runs out by period {math.floor(e['start'] / -net) + 1}")
        if e["sink"] == 0:
            flags.append("NO-SINK")
        if e["source"] == 0:
            flags.append("NO-SOURCE")
        top = sorted(e["items"], key=lambda i: -i[2])[:3]
        out[name] = {"source": e["source"], "sink": e["sink"], "net": net, "start": e["start"],
                     f"after_{periods}": end, "flags": flags, "top": top}
    return out


def cmd_economy(a):
    t = load_table(a.table)
    periods = a.periods or int(t.get("periods", 10))
    eco = economy(t, periods)
    if a.json:
        print(json.dumps(eco, indent=1))
        return 0
    for name, e in eco.items():
        print(f"{name:<16} +{fmt(e['source'])} -{fmt(e['sink'])} = net {fmt(e['net'])}/period · start {fmt(e['start'])} · after {periods}: {fmt(e[f'after_{periods}'])}  {'; '.join(e['flags'])}")
    return 0


def run_sim(t, steps, runs, seed):
    """Three models, picked by t['model']:
    draw  - each step draws one row by weight; tracks the sum of 'value' (loot, damage rolls).
    walk  - like draw, but stops when the total crosses t['target'] (turns to kill, turns to afford).
    deck  - rows are cards with 'count'; draws t['hand'] cards a step without replacement, reshuffling;
            reports how often each card is seen and the per-step value."""
    rng = random.Random(seed)
    rows = t["rows"]
    model = t.get("model", "draw")
    weights = [float(r.get("weight", 1)) for r in rows]
    totals, hits_at = [], []
    seen = {str(r.get("outcome", r.get("name", i))): 0 for i, r in enumerate(rows)}
    for _ in range(runs):
        total, hit = 0.0, None
        if model == "deck":
            pile = [i for i, r in enumerate(rows) for _ in range(int(r.get("count", 1)))]
            draw = []
            for s in range(steps):
                hand = []
                for _ in range(int(t.get("hand", 5))):
                    if not draw:
                        draw = pile[:]
                        rng.shuffle(draw)
                    hand.append(draw.pop())
                for i in hand:
                    seen[str(rows[i].get("outcome", rows[i].get("name", i)))] += 1
                    total += float(rows[i].get("value", 0))
        else:
            for s in range(steps):
                i = rng.choices(range(len(rows)), weights)[0]
                seen[str(rows[i].get("outcome", rows[i].get("name", i)))] += 1
                total += float(rows[i].get("value", 0))
                if model == "walk" and hit is None and total >= float(t["target"]):
                    hit = s + 1
                    break
        totals.append(total)
        hits_at.append(hit)
    totals.sort()
    q = lambda p: totals[min(len(totals) - 1, int(p * len(totals)))]
    res = {"model": model, "runs": runs, "steps": steps, "seed": seed, "mean": statistics.fmean(totals),
           "sd": statistics.pstdev(totals), "p05": q(0.05), "p50": q(0.5), "p95": q(0.95),
           "seen_share": {k: v / (runs * steps * (int(t.get("hand", 5)) if model == "deck" else 1)) for k, v in seen.items()}}
    if model == "walk":
        got = [h for h in hits_at if h is not None]
        res["reached"] = len(got) / runs
        if got:
            got.sort()
            res["steps_to_target"] = {"mean": statistics.fmean(got), "p05": got[int(0.05 * len(got))],
                                      "p50": got[len(got) // 2], "p95": got[min(len(got) - 1, int(0.95 * len(got)))]}
    for k in ("threshold",):
        if k in t:
            res["p_at_least_threshold"] = sum(1 for v in totals if v >= float(t[k])) / runs
    return res


def cmd_sim(a):
    t = load_table(a.table)
    steps = a.steps or int(t.get("steps", 10))
    r = run_sim(t, steps, a.runs, a.seed)
    if a.json:
        print(json.dumps(r, indent=1))
        return 0
    print(f"{r['model']} · {r['runs']} runs x {r['steps']} steps · seed {r['seed']} · total mean {fmt(r['mean'])} SD {fmt(r['sd'])} · p05 {fmt(r['p05'])} p50 {fmt(r['p50'])} p95 {fmt(r['p95'])}")
    if "steps_to_target" in r:
        s = r["steps_to_target"]
        print(f"  reached target in {r['reached']:.1%} of runs · steps mean {fmt(s['mean'])} p05 {s['p05']} p50 {s['p50']} p95 {s['p95']}")
    elif r["model"] == "walk":
        print(f"  reached target in {r.get('reached', 0):.1%} of runs")
    if "p_at_least_threshold" in r:
        print(f"  P(total >= threshold) {r['p_at_least_threshold']:.3f}")
    for k, v in sorted(r["seen_share"].items(), key=lambda kv: -kv[1])[:12]:
        print(f"  {k:<24} seen {v:.3f}")
    return 0


def draw_odds(deck, copies, drawn):
    """Hypergeometric: P(at least k of `copies` in `drawn` cards from `deck`), k = 0..min(copies, drawn)."""
    if not (0 <= copies <= deck and 0 <= drawn <= deck):
        fail("draw needs 0 <= copies <= deck and 0 <= drawn <= deck")
    total = math.comb(deck, drawn)
    exact = [math.comb(copies, k) * math.comb(deck - copies, drawn - k) / total for k in range(min(copies, drawn) + 1)]
    return [sum(exact[k:]) for k in range(len(exact))]


def cmd_draw(a):
    r = draw_odds(a.deck, a.copies, a.drawn)
    if a.json:
        print(json.dumps({"deck": a.deck, "copies": a.copies, "drawn": a.drawn, "p_at_least": r}))
        return 0
    print(f"{a.copies} copies in {a.deck} cards, {a.drawn} drawn (no replacement)")
    for k in range(1, len(r)):
        print(f"  P(at least {k}) {r[k]:.4f}")
    return 0


# ---------------------------------------------------------------- card pool shape

DECK_BANDS = {"mean_cost": (0.8, 2.2), "zero_cost_max": 0.30, "keyword_max": 0.60, "pool_ratio_max": 1.5}


def deck_shape(rows, bands=None):
    """Cost histogram, keyword shares, cards per pool and branching-upgrade share of a card table.
    Columns: cost; optional keywords (';' or ',' list), pool, upgrades (number of upgrade branches)."""
    b = dict(DECK_BANDS, **(bands or {}))
    n = len(rows)
    if not n:
        fail("deck needs at least one row")
    costs = [r.get("cost") for r in rows if isinstance(r.get("cost"), (int, float))]
    hist, kw, pools = {}, {}, {}
    for c in costs:
        hist[c] = hist.get(c, 0) + 1
    for r in rows:
        for k in str(r.get("keywords") or "").replace(",", ";").split(";"):
            k = k.strip().lower()
            if k:
                kw[k] = kw.get(k, 0) + 1
        if r.get("pool") not in (None, ""):
            pools[r["pool"]] = pools.get(r["pool"], 0) + 1
    branching = sum(1 for r in rows if isinstance(r.get("upgrades"), (int, float)) and r["upgrades"] >= 2)
    mean = sum(costs) / len(costs) if costs else None
    flags = []
    if mean is not None and not b["mean_cost"][0] <= mean <= b["mean_cost"][1]:
        flags.append(f"MEAN_COST {mean:.2f} outside {b['mean_cost'][0]}-{b['mean_cost'][1]}")
    if costs and hist.get(0, 0) / len(costs) > b["zero_cost_max"]:
        flags.append(f"ZERO_COST {hist[0] / len(costs):.0%} of cards cost 0")
    for k, v in kw.items():
        if v / n > b["keyword_max"]:
            flags.append(f"KEYWORD_EVERYWHERE {k} on {v / n:.0%} of cards: it no longer distinguishes")
    if len(pools) > 1 and max(pools.values()) / min(pools.values()) > b["pool_ratio_max"]:
        flags.append(f"POOL_UNEVEN largest pool {max(pools.values())} vs smallest {min(pools.values())}")
    return {"cards": n, "mean_cost": mean, "cost_hist": dict(sorted(hist.items())),
            "keywords": {k: v / n for k, v in sorted(kw.items(), key=lambda x: -x[1])},
            "pools": pools, "branching_share": branching / n, "flags": flags}


def cmd_deck(a):
    r = deck_shape(load_table(a.table)["rows"])
    if a.json:
        print(json.dumps(r))
        return 0
    print(f"{r['cards']} cards, mean cost {fmt(r['mean_cost']) if r['mean_cost'] is not None else '-'}")
    print("cost " + "  ".join(f"{c}:{v}" for c, v in r["cost_hist"].items()))
    for k, v in r["keywords"].items():
        print(f"  {k:<14}{v:.0%}")
    if r["pools"]:
        print("pools " + "  ".join(f"{p}:{v}" for p, v in r["pools"].items()))
    print(f"branching upgrades {r['branching_share']:.0%}")
    for f in r["flags"] or ["OK inside the reference bands"]:
        print(f)
    return 1 if r["flags"] else 0


# ---------------------------------------------------------------- difficulty ramps

RAMP_CHECKS = (0, 1, 5, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000)
RAMP_EARLY = 5  # a ramp that flattens in fewer steps than this is barely felt


def ramp_spec(r):
    """One ramp from a row: formula fields (base with factor or add, floor, cap) or a step -> value table."""
    pts = r.get("values") if isinstance(r.get("values"), (list, dict)) else r.get("points")
    if isinstance(pts, list):
        pts = {i: v for i, v in enumerate(pts)}
    if isinstance(pts, dict):
        table = sorted((int(num(k)), float(num(v))) for k, v in pts.items())
        if len(table) < 2:
            fail(f"ramp {r.get('name', '?')}: a table needs at least two steps")
        return {"table": table}
    if r.get("base") is None or (r.get("factor") is None) == (r.get("add") is None):
        fail(f"ramp {r.get('name', '?')}: give base plus one of factor or add, or a values table")
    return {"base": float(r["base"]), "factor": r.get("factor"), "add": r.get("add")}


def ramp_value(spec, n, floor=None, cap=None):
    """Raw formula value at step n and the clamped value the game would use."""
    try:
        raw = spec["base"] * float(spec["factor"]) ** n if spec.get("factor") is not None else spec["base"] + float(spec["add"]) * n
    except OverflowError:
        raw = math.inf
    v = raw
    if floor is not None and v < floor:
        v = floor
    if cap is not None and v > cap:
        v = cap
    return raw, v


def ramp(r, steps=None):
    """Check one difficulty ramp: values at checkpoints, where it floors or caps, last/first ratio and flags.
    UNCAPPED: grows past 3x with no cap (or shrinks below 1/3 with no floor) within the steps checked.
    FLOOR@n / CAP@n: the first step that reaches the floor or cap (a table: the step it stops changing).
    FLAT-EARLY: it flattens in under 5 steps, or does not change over its first 5 steps."""
    r = {k: v for k, v in r.items() if v not in (None, "")}
    spec = ramp_spec(r)
    name = str(r.get("name", "ramp"))
    floor = float(r["floor"]) if r.get("floor") is not None else None
    cap = float(r["cap"]) if r.get("cap") is not None else None
    sec = float(r["step_seconds"]) if r.get("step_seconds") else None
    out = {"name": name, "per": r.get("per", "step"), "step_seconds": sec, "floor": floor, "cap": cap}
    if "table" in spec:
        table = [(s, v) for s, v in spec["table"] if steps is None or s <= steps]
        if len(table) < 2:
            fail(f"ramp {name}: fewer than two table steps within --steps")
        vals = dict(table)
        last_step = table[-1][0]
        # where it flattens: the first step after which nothing changes again
        flat_at = None
        for i in range(len(table) - 1, 0, -1):
            if table[i][1] != table[i - 1][1]:
                flat_at = table[i][0] if i < len(table) - 1 else None
                break
        else:
            flat_at = table[0][0]
        changed = any(v != table[0][1] for _, v in table)
        rising = table[-1][1] > table[0][1]
        floor_at = flat_at if flat_at is not None and changed and not rising else None
        cap_at = flat_at if flat_at is not None and changed and rising else None
        early = [v for s, v in table if s < RAMP_EARLY]
        flat_start = len(early) >= 2 and len(set(early)) == 1
        bounded_up, bounded_down = cap_at is not None, floor_at is not None
        out["kind"] = "table"
    else:
        last_step = int(steps if steps is not None else r.get("steps", 100))
        checks = sorted({c for c in RAMP_CHECKS if c <= last_step} | {last_step})
        floor_at = cap_at = None
        for n in range(last_step + 1):
            raw, _ = ramp_value(spec, n, floor, cap)
            if floor_at is None and floor is not None and raw <= floor:
                floor_at = n
            if cap_at is None and cap is not None and raw >= cap:
                cap_at = n
            if (floor is None or floor_at is not None) and (cap is None or cap_at is not None):
                break
        checks = sorted(set(checks) | {s - d for s in (floor_at, cap_at) if s is not None for d in (0, 1) if s - d >= 0})
        vals = {n: ramp_value(spec, n, floor, cap)[1] for n in checks}
        early_vals = [ramp_value(spec, n, floor, cap)[1] for n in range(min(RAMP_EARLY, last_step + 1))]
        flat_start = len(early_vals) >= 2 and len(set(early_vals)) == 1
        bounded_up, bounded_down = cap is not None, floor is not None
        out["kind"] = "formula"
        out["formula"] = (f"{fmt(spec['base'])} x {fmt(float(spec['factor']))}^n" if spec.get("factor") is not None
                          else f"{fmt(spec['base'])} + {fmt(float(spec['add']))}n")
    first, last = vals[min(vals)], vals[last_step]
    ratio = last / first if first else None
    flags = []
    if ratio is not None and ratio > 3 and not bounded_up:
        flags.append("UNCAPPED")
    if ratio is not None and 0 < ratio < 1 / 3 and not bounded_down:
        flags.append("UNCAPPED")
    if floor_at is not None:
        flags.append(f"FLOOR@{floor_at}")
    if cap_at is not None:
        flags.append(f"CAP@{cap_at}")
    flat_step = min(s for s in (floor_at, cap_at, 10 ** 9) if s is not None)
    if flat_step < RAMP_EARLY or flat_start:
        flags.append("FLAT-EARLY")
    out.update({"steps": last_step, "values": {str(k): v for k, v in sorted(vals.items())}, "floor_at": floor_at,
                "cap_at": cap_at, "ratio": ratio, "flags": flags,
                "flat_reason": ("no change over the first steps" if flat_start else
                                f"flattens at step {flat_step}") if "FLAT-EARLY" in flags else None})
    return out


def ramp_rows(path):
    """Ramps from JSON ({ramps: [...]}, {rows: [...]}, a list or one ramp) or CSV (formula rows, or step,value[,name])."""
    if path.lower().endswith(".csv"):
        rows = load_table(path)["rows"]
        if rows and "step" in rows[0] and "value" in rows[0]:
            by = {}
            for r in rows:
                by.setdefault(str(r.get("name", "ramp")), {})[r["step"]] = r["value"]
            return [{"name": k, "values": v} for k, v in by.items()]
        return rows
    doc = load_json(path)
    if isinstance(doc, list):
        return doc
    if "ramps" in doc or "rows" in doc:
        return doc.get("ramps") or doc.get("rows")
    return [doc]


def cmd_ramp(a):
    res = [ramp(r, a.steps) for r in ramp_rows(a.table)]
    if a.json:
        print(json.dumps(res, indent=1))
        return 0
    for r in res:
        sec = r["step_seconds"]
        t = (lambda n: f" ({fmt(n * sec)} s)") if sec else (lambda n: "")
        head = r.get("formula") or f"table of {len(r['values'])} steps"
        bounds = "".join(f" · {k} {fmt(r[k])}" for k in ("floor", "cap") if r[k] is not None)
        ratio = f"last/first {r['ratio']:.3g}" if r["ratio"] is not None else "last/first n/a"
        print(f"{r['name']}: {head}{bounds} · per {r['per']} · {r['steps']} steps{t(r['steps'])} · {ratio}  {' '.join(r['flags'])}")
        print("  " + " · ".join(f"step {k}{t(int(k))} {fmt(v)}" for k, v in r["values"].items()))
        if r["flat_reason"]:
            print(f"  FLAT-EARLY: {r['flat_reason']}")
    return 0


# ---------------------------------------------------------------- stop or continue

def stop_check(t, runs=20000, seed=1):
    """Stop-or-continue loop with attrition: options arrive one per step; settling ends the run and pays
    value * condition / start. Moving on costs condition (an attrition draw). With 'noisy', each attribute is
    seen with chance condition / start, else read as its mean. Scores fixed-threshold policies over many runs."""
    rng = random.Random(seed)
    steps, attrs = int(t.get("steps", 10)), int(t.get("attributes", 1))
    start, noisy = float(t.get("condition", 100)), bool(t.get("noisy", False))
    opt, att = t.get("option") or t["rows"], t.get("attrition") or [{"value": 0}]
    ow, aw = [float(r.get("weight", 1)) for r in opt], [float(r.get("weight", 1)) for r in att]
    ov, av = [float(r["value"]) for r in opt], [float(r["value"]) for r in att]
    mean1 = sum(w * v for w, v in zip(ow, ov)) / sum(ow)
    runs_data = []
    for _ in range(runs):
        cond, seq = start, []
        for s in range(steps):
            if s:
                cond = max(0.0, cond + rng.choices(av, aw)[0])
            vals = rng.choices(ov, ow, k=attrs)
            seen = sum(v if not noisy or rng.random() < cond / start else mean1 for v in vals)
            seq.append((seen, sum(vals) * cond / start, cond))
            if cond <= 0:
                break
        runs_data.append(seq)
    firsts = sorted(r[0][0] for r in runs_data)
    cands = sorted({firsts[min(len(firsts) - 1, int(q / 20 * len(firsts)))] for q in range(21)})
    def play(th):
        pay, at = 0.0, 0
        for seq in runs_data:
            for i, (seen, real, cond) in enumerate(seq):
                if seen >= th or i == len(seq) - 1 or cond <= 0:
                    pay += real
                    at += i + 1
                    break
        return pay / runs, at / runs
    pols = [{"threshold": th, "ev": e, "mean_stop": m} for th in cands for e, m in [play(th)]]
    best = max(pols, key=lambda p: p["ev"])
    first = statistics.fmean(seq[0][1] for seq in runs_data)
    oracle = statistics.fmean(max(x[1] for x in seq) for seq in runs_data)
    flags = []
    if first >= 0.95 * best["ev"]:
        flags.append("FIRST-IS-BEST")
    if best["mean_stop"] >= 0.9 * steps:
        flags.append("NEVER-STOP")
    if all(v >= 0 for v in av):
        flags.append("NO-COST")
    evs = [p["ev"] for p in pols]
    if max(evs) - min(evs) <= 0.05 * abs(best["ev"] or 1):
        flags.append("FLAT")
    return {"runs": runs, "seed": seed, "steps": steps, "noisy": noisy, "ev_first": first, "ev_oracle": oracle,
            "best": best, "policies": pols, "flags": flags or ["TENSE"]}


def cmd_stop(a):
    r = stop_check(load_table(a.table), a.runs, a.seed)
    if a.json:
        print(json.dumps(r, indent=1))
        return 0
    b = r["best"]
    print(f"stop · {r['runs']} runs x {r['steps']} steps · seed {r['seed']} · noisy {r['noisy']}  {' '.join(r['flags'])}")
    print(f"  best: settle when seen value >= {fmt(b['threshold'])} · EV {fmt(b['ev'])} · mean stop step {fmt(b['mean_stop'])}")
    print(f"  settle on first: EV {fmt(r['ev_first'])} · hindsight best (upper bound): EV {fmt(r['ev_oracle'])}")
    for p in r["policies"]:
        print(f"  threshold {fmt(p['threshold']):>8}  EV {fmt(p['ev']):>8}  stop step {fmt(p['mean_stop'])}")
    return 0


# ---------------------------------------------------------------- event director

def plin(points, x):
    """Piecewise-linear lookup over [[x, y], ...]; flat beyond the ends."""
    pts = sorted((float(a), float(b)) for a, b in points)
    if x <= pts[0][0]:
        return pts[0][1]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x <= x1:
            return y0 + (y1 - y0) * (x - x0) / ((x1 - x0) or 1)
    return pts[-1][1]


def director_run(t, days, rng):
    """One run: a sorted list of (day, category) events from independent comps."""
    ev = []
    for c in t["comps"]:
        kind, start = c.get("kind", "mtb"), float(c.get("start_day", 0))
        cat, sp = c.get("category", "event"), float(c.get("min_spacing", 0))
        if kind == "once":
            if float(c["day"]) <= days:
                ev.append((float(c["day"]), cat))
        elif kind == "onoff":
            on, off = float(c["on_days"]), float(c["off_days"])
            lo, hi = c.get("count") or [1, 1]
            d = start
            while d < days:
                k = rng.randint(int(lo), int(hi))
                while k > 1 and (k - 1) * sp > on:
                    k -= 1
                xs = sorted(rng.uniform(0, on - (k - 1) * sp) for _ in range(k))
                ev += [(d + x + i * sp, cat) for i, x in enumerate(xs) if d + x + i * sp <= days]
                d += on + off
        else:
            mtb, picks = float(c["mtb_days"]), c.get("choices")
            d = start + rng.expovariate(1 / mtb)
            while d <= days:
                ch = rng.choices([p["category"] for p in picks], [float(p.get("weight", 1)) for p in picks])[0] if picks else cat
                ev.append((d, ch))
                d += max(sp, rng.expovariate(1 / mtb))
    return sorted(ev)


def pctl(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(q * len(xs)))] if xs else None


def director(t, days=120, runs=2000, seed=1):
    """Independent comps schedule events; reports gaps, clumps, first threat and the threat budget over days."""
    rng = random.Random(seed)
    comps = t["comps"]
    cats = sorted({c.get("category", "event") for c in comps if "choices" not in c} |
                  {p["category"] for c in comps for p in c.get("choices") or []})
    threats = set(t.get("threats") or [k for k in cats if "threat" in k.lower()] or cats)
    window, floor, grace = float(t.get("clump_window", 1)), float(t.get("breather", 3)), t.get("grace")
    points, curve, ad = float(t.get("points", 100)), t.get("budget"), t.get("adapt")
    marks = sorted({d for d in (30, 60, days) if d <= days})
    counts, gaps, longest, clumps, firsts, early, spacing = {k: 0 for k in cats}, [], [], [], [], 0, []
    bud = {d: [] for d in marks}
    afac = (lambda v: plin(ad["curve"], v)) if ad and ad.get("curve") else (lambda v: 1.0)
    for _ in range(runs):
        ev = director_run(t, days, rng)
        for _, k in ev:
            counts[k] = counts.get(k, 0) + 1
        th = [d for d, k in ev if k in threats]
        firsts.append(th[0] if th else None)
        if grace is not None and th and th[0] < float(grace):
            early += 1
        edges = th + [days]
        gaps.append(max((b - a for a, b in zip(edges, edges[1:])), default=days))
        spacing += [b - a for a, b in zip(th, th[1:])]
        clumps.append(sum(1 for a, b in zip(th, th[1:]) if b - a < window))
        dayset, best, cur = {int(d) for d in th}, 0, 0
        for d in range(int(days) + 1):
            cur = cur + 1 if d in dayset else 0
            best = max(best, cur)
        longest.append(best)
        a_val, ti = float(ad.get("start", 0)) if ad else 0.0, 0
        for d in range(int(days) + 1):
            if ad:
                a_val += float(ad.get("per_day", 1))
                while ti < len(th) and th[ti] < d + 1:
                    if rng.random() < float(ad.get("loss_chance", 0)):
                        a_val -= float(ad.get("loss", 0))
                    ti += 1
                a_val = min(float(ad.get("max", math.inf)), max(float(ad.get("min", -math.inf)), a_val))
            if d in bud:
                bud[d].append(points * (plin(curve, d) if curve else 1.0) * afac(a_val))
    got = [f for f in firsts if f is not None]
    start_b = points * (plin(curve, 0) if curve else 1.0) * afac(float(ad.get("start", 0)) if ad else 0.0)
    res = {"days": days, "runs": runs, "seed": seed, "threats": sorted(threats),
           "per_30_days": {k: v / runs * 30 / days for k, v in counts.items()},
           "longest_gap_p50": pctl(gaps, 0.5), "longest_threat_run_p50": pctl(longest, 0.5),
           "clumps_per_run": statistics.fmean(clumps), "first_threat_min": min(got) if got else None,
           "first_threat_p50": pctl(got, 0.5), "min_spacing_seen": min(spacing) if spacing else None,
           "budget": {d: {"p10": pctl(v, .1), "p50": pctl(v, .5), "p90": pctl(v, .9)} for d, v in bud.items()}}
    flags = []
    if res["longest_gap_p50"] is not None and res["longest_gap_p50"] < floor:
        flags.append("NO-BREATHER")
    if res["clumps_per_run"] >= 1:
        flags.append("CLUMP")
    if early:
        flags.append("EARLY-THREAT")
    if res["budget"][marks[-1]]["p50"] > 3 * start_b and not (ad and "max" in ad):
        flags.append("RUNAWAY")
    res["flags"] = flags or ["PACED"]
    return res


def cmd_director(a):
    r = director(load_json(a.table), a.days, a.runs, a.seed)
    if a.json:
        print(json.dumps(r, indent=1))
        return 0
    print(f"director · {r['runs']} runs x {r['days']} days · seed {r['seed']} · threats {', '.join(r['threats'])}  {' '.join(r['flags'])}")
    print("  per 30 days: " + " · ".join(f"{k} {fmt(v)}" for k, v in r["per_30_days"].items()))
    print(f"  first threat: min {fmt(r['first_threat_min'])} · p50 {fmt(r['first_threat_p50'])} · closest pair {fmt(r['min_spacing_seen'])} days")
    print(f"  longest gap p50 {fmt(r['longest_gap_p50'])} days · longest threat-day run p50 {r['longest_threat_run_p50']} · clumps per run {fmt(r['clumps_per_run'])}")
    print("  budget: " + " · ".join(f"day {d} p10 {fmt(b['p10'])} p50 {fmt(b['p50'])} p90 {fmt(b['p90'])}" for d, b in r["budget"].items()))
    return 0


# ---------------------------------------------------------------- mood meter

def mood(t, hours=720, runs=200, seed=1):
    """Mood seeks a target (base plus stacked event effects) at capped rise and fall rates per hour.
    Copy k of an event counts effect * mult^(k-1), up to its stack limit."""
    rng = random.Random(seed)
    base, rise, fall, th = float(t["base"]), float(t["rise_per_hour"]), float(t["fall_per_hour"]), float(t["threshold"])
    lo, hi = [float(x) for x in t.get("range", [0, 100])]
    bands = sorted(((float(v), k) for k, v in (t.get("bands") or {"break": 0}).items()), reverse=True)
    events = t["events"]
    names = [e.get("name", str(i)) for i, e in enumerate(events)]
    vals, below, crosses = [], 0, 0
    band_h, peak = {k: 0 for _, k in bands}, {n: 0 for n in names}
    for _ in range(runs):
        m, active, was = float(t.get("start", base)), [[] for _ in events], None
        for h in range(hours):
            target = base
            for i, e in enumerate(events):
                active[i] = [x for x in active[i] if x > h]
                p = float(e.get("rate_per_day", 0)) / 24
                n = int(p) + (rng.random() < p - int(p))
                active[i] += [h + float(e.get("duration_h", 24))] * n
                lim, mult = e.get("stack_limit"), float(e.get("stack_mult", 1))
                k = len(active[i]) if lim is None else min(len(active[i]), int(lim))
                peak[names[i]] = max(peak[names[i]], len(active[i]))
                target += float(e["effect"]) * (k if mult == 1 else (1 - mult ** k) / (1 - mult))
            m = min(m + rise, target) if target > m else max(m - fall, target)
            m = min(hi, max(lo, m))
            vals.append(m)
            now = m < th
            if now:
                below += 1
                for off, k in bands:
                    if m <= th - off:
                        band_h[k] += 1
                        break
            if was is not None and now != was:
                crosses += 1
            was = now
    tot = hours * runs
    res = {"hours": hours, "runs": runs, "seed": seed, "p05": pctl(vals, .05), "p50": pctl(vals, .5), "p95": pctl(vals, .95),
           "share_below": below / tot, "share_by_band": {k: v / tot for k, v in band_h.items()},
           "crossings_per_day": crosses / runs / (hours / 24), "peak_copies": peak}
    flags = []
    if rise == fall and rise >= 0.25 * abs(hi - lo):
        flags.append("SPIKE")
    if any(e.get("stack_limit") is None and peak[names[i]] > 5 for i, e in enumerate(events)):
        flags.append("UNCAPPED")
    if below == 0:
        flags.append("NEVER-BREAKS")
    if res["share_below"] > 0.5:
        flags.append("ALWAYS-BREAKS")
    if res["crossings_per_day"] > float(t.get("oscillate_per_day", 1)):
        flags.append("OSCILLATES")
    res["flags"] = flags or ["STEADY"]
    return res


def cmd_mood(a):
    r = mood(load_json(a.table), a.hours, a.runs, a.seed)
    if a.json:
        print(json.dumps(r, indent=1))
        return 0
    print(f"mood · {r['runs']} runs x {r['hours']} h · seed {r['seed']}  {' '.join(r['flags'])}")
    print(f"  mood p05 {fmt(r['p05'])} · p50 {fmt(r['p50'])} · p95 {fmt(r['p95'])} · below threshold {r['share_below']:.1%} of hours · crossings per day {fmt(r['crossings_per_day'])}")
    print("  bands: " + " · ".join(f"{k} {v:.1%}" for k, v in r["share_by_band"].items()))
    print("  peak copies: " + " · ".join(f"{k} {v}" for k, v in r["peak_copies"].items()))
    return 0


# ---------------------------------------------------------------- text grammar

SYM_RE = re.compile(r"\[([^\[\]]+)\]")
COND_RE = re.compile(r"^\s*([\w.]+)\s*(==|!=|>=|<=|>|<)\s*(.+?)\s*$")


def cond_ok(expr, consts):
    """Comma-separated conditions, all must hold. A missing constant fails every test except !=."""
    for part in [x for x in (expr or "").split(",") if x.strip()]:
        m = COND_RE.match(part)
        if not m:
            fail(f"bad condition: {part}")
        k, op, v = m.groups()
        if k not in consts:
            if op != "!=":
                return False
            continue
        try:
            x, y = float(consts[k]), float(v)
        except ValueError:
            x, y = str(consts[k]), v
            if op not in ("==", "!="):
                return False
        if not {"==": x == y, "!=": x != y, ">": x > y, "<": x < y, ">=": x >= y, "<=": x <= y}[op]:
            return False
    return True


def grammar(t, root="r_name", samples=500, seed=1, consts=None):
    """Weighted rewrite grammar with conditions and priority tiers: structure checks, combination count, variety."""
    consts, lists, rules = consts or {}, t.get("lists") or {}, {}
    for r in t["rules"]:
        rules.setdefault(r["lhs"], []).append(r)
    def live(sym):
        ok = [r for r in rules.get(sym, []) if cond_ok(r.get("if"), consts)]
        top = max((float(r.get("priority", 0)) for r in ok), default=0)
        return [r for r in ok if float(r.get("priority", 0)) == top]
    refs = lambda r: SYM_RE.findall(r["rhs"])
    used = {s for rs in rules.values() for r in rs for s in refs(r)}
    undefined = sorted(s for s in used | {root} if s not in rules and s not in lists)
    dead = sorted(s for s in rules if s not in lists and not live(s))
    seen, stack = set(), [root]
    while stack:
        s = stack.pop()
        if s not in seen:
            seen.add(s)
            stack += [x for r in rules.get(s, []) for x in refs(r)]
    unreachable = sorted(s for s in set(rules) | set(lists) if s not in seen)
    def reaches(a, b):
        vis, st = set(), [x for r in live(a) for x in refs(r)]
        while st:
            s = st.pop()
            if s == b:
                return True
            if s not in vis:
                vis.add(s)
                st += [x for r in live(s) for x in refs(r)]
        return False
    recursive = sorted(s for s in rules if reaches(s, s))
    memo = {}
    def count(s):
        if s in lists:
            return len(lists[s])
        if s in recursive:
            return math.inf
        if s not in memo:
            memo[s] = 0
            memo[s] = sum(math.prod(count(x) for x in refs(r)) for r in live(s))
        return memo[s]
    combos = count(root)
    rng = random.Random(seed)
    def expand(s, depth=0):
        if s in lists and lists[s]:
            return rng.choice(lists[s]), None
        opts = live(s)
        if not opts or depth > 50:
            return f"[{s}]", None
        r = rng.choices(opts, [float(x.get("p", 1)) for x in opts])[0]
        return SYM_RE.sub(lambda m: expand(m.group(1), depth + 1)[0], r["rhs"]), r["rhs"]
    freq, branch = {}, {}
    for _ in range(samples):
        o, b = expand(root)
        freq[o] = freq.get(o, 0) + 1
        branch[b] = branch.get(b, 0) + 1
    tops = live(root)
    tw = sum(float(r.get("p", 1)) for r in tops) or 1
    alts = [{"rhs": r["rhs"], "expected": float(r.get("p", 1)) / tw, "observed": branch.get(r["rhs"], 0) / samples} for r in tops]
    uniq = len(freq) / samples
    flags = [f for f, hit in (("UNDEFINED", undefined), ("UNREACHABLE", unreachable), ("DEAD-UNDER", dead),
                              ("RECURSIVE", recursive), ("LOW-VARIETY", uniq < 0.8)) if hit]
    return {"root": root, "samples": samples, "seed": seed, "consts": consts, "undefined": undefined,
            "unreachable": unreachable, "dead_under": dead, "recursive": recursive,
            "combinations": "infinite" if combos == math.inf else ("over 1e6" if combos > 1e6 else int(combos)),
            "unique_share": uniq, "top_repeats": sorted(freq.items(), key=lambda kv: -kv[1])[:5],
            "alternatives": alts, "flags": flags or ["CLEAN"]}


def cmd_grammar(a):
    consts = dict(kv.split("=", 1) for kv in a.const or [])
    r = grammar(load_json(a.table), a.root, a.samples, a.seed, consts)
    if a.json:
        print(json.dumps(r, indent=1))
    else:
        print(f"grammar · root {r['root']} · {r['samples']} samples · seed {r['seed']}  {' '.join(r['flags'])}")
        for k in ("undefined", "unreachable", "dead_under", "recursive"):
            if r[k]:
                print(f"  {k.replace('_', ' ')}: {', '.join(r[k])}")
        print(f"  combinations {r['combinations']} · unique share {r['unique_share']:.1%}")
        for alt in r["alternatives"]:
            print(f"  {alt['expected']:.1%} expected, {alt['observed']:.1%} seen: {alt['rhs']}")
        print("  most repeated: " + " · ".join(f"{o} x{n}" for o, n in r["top_repeats"]))
    return 1 if r["undefined"] or r["dead_under"] else 0


# ---------------------------------------------------------------- deck growth across a run

def growth(t):
    """Project deck size per stage from adds and removals by source against a target band.
    BLOAT: past the ceiling. OFF-BAND: final size outside the end band. NO-THIN: cards are added but no source removes any.
    With a 'resource' (cards that produce or consume it per play): ratio of produced to consumed per average hand;
    STARVED under 0.8, FLOODED over 1.5 or nothing consumes it."""
    band = t.get("band", {})
    start = float(t.get("start", band.get("start", 10)))
    per, ceiling = band.get("per_stage"), band.get("ceiling")
    lo, hi = band.get("end_low"), band.get("end_high")
    stages = t.get("stages") or t.get("rows") or []
    if not stages:
        fail("growth: give 'stages', each with adds and removals by source")
    size, out, flags, added, removed = start, [], [], 0.0, 0.0
    for i, st in enumerate(stages, 1):
        a = sum(float(v) for v in (st.get("adds") or {}).values())
        r = sum(float(v) for v in (st.get("removals") or {}).values())
        added, removed = added + a, removed + r
        size = max(0.0, size + a - r)
        row = {"stage": st.get("name", i), "adds": a, "removals": r, "size": size,
               "target": start + float(per) * i if per is not None else None}
        if ceiling is not None and size > float(ceiling):
            row["flag"] = "BLOAT"
            if "BLOAT" not in flags:
                flags.append("BLOAT")
        out.append(row)
    if (lo is not None and size < float(lo)) or (hi is not None and size > float(hi)):
        flags.append("OFF-BAND")
    if added > 0 and removed == 0:
        flags.append("NO-THIN")
    res = {"start": start, "end": size, "band": band, "stages": out, "flags": flags}
    rc = t.get("resource")
    if rc:
        cards = rc.get("cards", [])
        deck = float(rc.get("deck", size)) or 1.0
        hand = float(rc.get("hand", 5))
        prod = sum(float(c.get("copies", 1)) * float(c.get("produce", 0)) for c in cards) * hand / deck
        cons = sum(float(c.get("copies", 1)) * float(c.get("consume", 0)) for c in cards) * hand / deck
        ratio = prod / cons if cons else None
        res["resource"] = {"name": rc.get("name", "resource"), "produced_per_hand": prod, "consumed_per_hand": cons, "ratio": ratio}
        if ratio is not None and ratio < 0.8:
            flags.append("STARVED")
        elif ratio is None or ratio > 1.5:
            flags.append("FLOODED")
    if not flags:
        flags.append("ON-BAND")
    return res


def cmd_growth(a):
    r = growth(load_json(a.table))
    if a.json:
        print(json.dumps(r, indent=1))
        return 0
    print(f"deck {fmt(r['start'])} -> {fmt(r['end'])}  {' '.join(r['flags'])}")
    for s in r["stages"]:
        tg = f" (target {fmt(s['target'])})" if s["target"] is not None else ""
        print(f"  stage {s['stage']}: +{fmt(s['adds'])} -{fmt(s['removals'])} = {fmt(s['size'])}{tg} {s.get('flag', '')}".rstrip())
    rc = r.get("resource")
    if rc:
        ratio = f"{rc['ratio']:.3g}" if rc["ratio"] is not None else "n/a"
        print(f"  {rc['name']}: made {rc['produced_per_hand']:.3g} / spent {rc['consumed_per_hand']:.3g} per hand, ratio {ratio}")
    return 0


# ---------------------------------------------------------------- quota with a countdown

def quota(t):
    """Rising payments, each due after a number of periods, against an income ramp (a ramp row: base with factor
    or add, or a values table). Per payment: required income per period, expected income over its window, slack.
    TIGHT: slack under 1.0. LOOSE: slack over 2.0 for three or more payments in a row. CLIFF: required rate more than doubles."""
    pays = t.get("payments") or t.get("rows") or []
    if not pays:
        fail("quota: give 'payments' with amount and periods")
    if not t.get("income"):
        fail("quota: give an 'income' ramp")
    inc = t["income"]
    spec = ramp_spec(inc)
    floor = float(inc["floor"]) if inc.get("floor") is not None else None
    cap = float(inc["cap"]) if inc.get("cap") is not None else None

    def income(n):
        if "table" in spec:
            v = spec["table"][0][1]
            for k, x in spec["table"]:
                if k <= n:
                    v = x
            return v
        return ramp_value(spec, n, floor, cap)[1]

    t0, out, flags, run, prev = 0, [], [], 0, None
    for i, p in enumerate(pays, 1):
        amt, n = float(p["amount"]), int(p["periods"])
        exp = sum(income(t0 + k) for k in range(n))
        t0 += n
        req = amt / n
        slack = exp / amt if amt else math.inf
        f = []
        if slack < 1.0:
            f.append("TIGHT")
        if prev is not None and req > 2 * prev:
            f.append("CLIFF")
        run = run + 1 if slack > 2.0 else 0
        if run >= 3:
            f.append("LOOSE")
        prev = req
        flags += [x for x in f if x not in flags]
        out.append({"payment": p.get("name", i), "amount": amt, "periods": n, "due_at": t0,
                    "required_per_period": req, "expected": exp, "slack": slack, "flags": f})
    return {"payments": out, "flags": flags or ["PACED"]}


def cmd_quota(a):
    r = quota(load_json(a.table))
    if a.json:
        print(json.dumps(r, indent=1))
        return 0
    print(f"{len(r['payments'])} payments  {' '.join(r['flags'])}")
    for p in r["payments"]:
        print(f"  {p['payment']}: {fmt(p['amount'])} in {p['periods']} (due {p['due_at']}) · need {p['required_per_period']:.4g}/period"
              f" · expect {p['expected']:.4g} · slack {p['slack']:.3g} {' '.join(p['flags'])}".rstrip())
    return 0


def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    p = argparse.ArgumentParser(prog="ldw", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", action="version", version=f"ludowright {VERSION} (findings {FORMAT_VERSION})")
    sp = p.add_subparsers(dest="cmd", required=True)
    f = sp.add_parser("findings", help="the findings contract: validate, md, new")
    f.add_argument("action", choices=("validate", "md", "new"))
    f.add_argument("file", nargs="?")
    f.add_argument("-o", "--out")
    f.add_argument("--game")
    f.add_argument("--kind", choices=KINDS, default="review")
    f.set_defaults(fn=cmd_findings)
    e = sp.add_parser("ev", help="expected value of a weighted outcome table"); e.add_argument("table"); e.add_argument("--json", action="store_true"); e.set_defaults(fn=cmd_ev)
    c = sp.add_parser("curve", help="cost curve fit and outliers"); c.add_argument("table"); c.add_argument("--attrs", help="comma list of attribute columns")
    c.add_argument("--costs", help="several cost columns as column:rate pairs, folded into one cost (gold:1,wood:0.5)")
    c.add_argument("--tolerance", type=float, default=0.15, help="flag items whose cost is off the fit by more than this share (default 0.15)")
    c.add_argument("--json", action="store_true"); c.set_defaults(fn=cmd_curve)
    o = sp.add_parser("economy", help="sources, sinks, net flow and leaks"); o.add_argument("table"); o.add_argument("--periods", type=int); o.add_argument("--json", action="store_true"); o.set_defaults(fn=cmd_economy)
    m = sp.add_parser("sim", help="Monte Carlo over a declared table"); m.add_argument("table"); m.add_argument("--steps", type=int); m.add_argument("--runs", type=int, default=10000)
    m.add_argument("--seed", type=int, default=1); m.add_argument("--json", action="store_true"); m.set_defaults(fn=cmd_sim)
    d = sp.add_parser("draw", help="hypergeometric draw odds for copies of a card"); d.add_argument("--deck", type=int, required=True)
    d.add_argument("--copies", type=int, required=True); d.add_argument("--drawn", type=int, required=True); d.add_argument("--json", action="store_true"); d.set_defaults(fn=cmd_draw)
    dk = sp.add_parser("deck", help="card pool shape: cost histogram, keyword shares, pools, branching upgrades")
    dk.add_argument("table"); dk.add_argument("--json", action="store_true"); dk.set_defaults(fn=cmd_deck)
    r = sp.add_parser("ramp", help="difficulty ramp check: uncapped growth, where it floors or caps, flat early")
    r.add_argument("table"); r.add_argument("--steps", type=int, help="steps to check (formula ramps; default the ramp's steps or 100)")
    r.add_argument("--json", action="store_true"); r.set_defaults(fn=cmd_ramp)
    s = sp.add_parser("stop", help="stop-or-continue check: best settle threshold under attrition and noisy information")
    s.add_argument("table"); s.add_argument("--runs", type=int, default=20000); s.add_argument("--seed", type=int, default=1)
    s.add_argument("--json", action="store_true"); s.set_defaults(fn=cmd_stop)
    g = sp.add_parser("director", help="event director: on/off windows, MTB, spacing, grace, adapt counter")
    g.add_argument("table"); g.add_argument("--days", type=int, default=120); g.add_argument("--runs", type=int, default=2000)
    g.add_argument("--seed", type=int, default=1); g.add_argument("--json", action="store_true"); g.set_defaults(fn=cmd_director)
    md = sp.add_parser("mood", help="mood meter: stacked effects with caps, seek rates, threshold and bands")
    md.add_argument("table"); md.add_argument("--hours", type=int, default=720); md.add_argument("--runs", type=int, default=200)
    md.add_argument("--seed", type=int, default=1); md.add_argument("--json", action="store_true"); md.set_defaults(fn=cmd_mood)
    gr = sp.add_parser("grammar", help="text grammar check: weights, conditions, priority, variety")
    gr.add_argument("table"); gr.add_argument("--root", default="r_name"); gr.add_argument("--samples", type=int, default=500)
    gr.add_argument("--seed", type=int, default=1); gr.add_argument("--const", action="append", help="KEY=VAL, repeatable")
    gr.add_argument("--json", action="store_true"); gr.set_defaults(fn=cmd_grammar)
    gw = sp.add_parser("growth", help="deck size per stage against a target band, thinning and resource ratio")
    gw.add_argument("table"); gw.add_argument("--json", action="store_true"); gw.set_defaults(fn=cmd_growth)
    q = sp.add_parser("quota", help="rising payments with countdowns against an income ramp: slack, TIGHT, LOOSE, CLIFF")
    q.add_argument("table"); q.add_argument("--json", action="store_true"); q.set_defaults(fn=cmd_quota)
    a = p.parse_args(argv)
    if a.cmd == "findings" and a.action != "new" and not a.file:
        fail("findings validate and md need a FILE")
    return a.fn(a) or 0


if __name__ == "__main__":
    sys.exit(main())

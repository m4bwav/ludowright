#!/usr/bin/env python3
"""ludowright's counting tool. Judgment stays with the model; this script checks and counts.

  findings validate FILE        check a findings file against the contract (exit 1 on errors)
  findings md FILE [-o OUT]     the readable markdown view of a findings file
  findings new --game NAME      print an empty findings file to fill
  ev TABLE                      expected value, spread and odds of a weighted outcome table
  curve TABLE                   fit a cost curve over items and flag over- and under-costed ones
  economy TABLE                 source and sink totals per period, net flow, leak and drain flags
  sim TABLE --steps N           Monte Carlo over a declared table (draws, deltas or a deck)

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

VERSION = "0.1.11"
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
    a = p.parse_args(argv)
    if a.cmd == "findings" and a.action != "new" and not a.file:
        fail("findings validate and md need a FILE")
    return a.fn(a) or 0


if __name__ == "__main__":
    sys.exit(main())

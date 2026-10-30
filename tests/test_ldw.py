"""Offline tests for scripts/ldw.py. Run: python -m unittest discover -s tests"""
import contextlib
import io
import json
import math
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "skills", "ludowright", "scripts"))
import ldw  # noqa: E402


def good_finding(**kw):
    f = {"id": "F-001", "severity": "major", "category": "dominant-strategy", "title": "One card wins every run",
         "location": {"file": "docs/cards.txt", "rule": "Overclock"}, "principle": {"name": "no dominant strategy", "source": "kb/review-rubric.md R-03"},
         "evidence": "Overclock costs 1 and doubles output; nothing else at cost 1 comes close", "suggestion": "Cost 2, or exhaust on use",
         "impact": "high", "effort": "S", "confidence": "high"}
    f.update(kw)
    return f


def doc(findings, kind="review"):
    return {"format": "ludowright-findings", "version": "1.0", "game": "Test", "kind": kind, "date": "2026-10-29",
            "sources_read": ["docs/cards.txt"], "findings": findings}


class Findings(unittest.TestCase):
    def test_valid_file_passes(self):
        errs, warns = ldw.validate_findings(doc([good_finding()]))
        self.assertEqual(errs, [])

    def test_missing_principle_and_bad_severity_fail(self):
        f = good_finding(severity="huge")
        del f["principle"]
        errs, _ = ldw.validate_findings(doc([f]))
        self.assertTrue(any("severity" in e for e in errs))
        self.assertTrue(any("missing principle" in e for e in errs))

    def test_duplicate_ids_and_unknown_category(self):
        errs, _ = ldw.validate_findings(doc([good_finding(), good_finding(category="vibes")]))
        self.assertTrue(any("duplicate id" in e for e in errs))
        self.assertTrue(any("unknown category" in e for e in errs))

    def test_improve_needs_impact_and_effort(self):
        f = good_finding()
        del f["effort"]
        errs, _ = ldw.validate_findings(doc([f], kind="improve"))
        self.assertTrue(any("impact and effort" in e for e in errs))

    def test_feel_finding_warns_without_handoff(self):
        _, warns = ldw.validate_findings(doc([good_finding(category="feel")]))
        self.assertTrue(any("juice-scan" in w for w in warns))

    def test_wrong_major_version_fails(self):
        d = doc([])
        d["version"] = "2.0"
        errs, _ = ldw.validate_findings(d)
        self.assertTrue(any("version" in e for e in errs))

    def test_md_ranks_by_severity(self):
        md = ldw.findings_md(doc([good_finding(id="F-002", severity="minor", title="Minor thing"), good_finding()]))
        self.assertLess(md.index("F-001 · One card"), md.index("F-002 · Minor thing"))
        self.assertIn("Principle: no dominant strategy (kb/review-rubric.md R-03)", md)

    def test_stage_and_built_are_checked_and_shown(self):
        d = doc([good_finding(built="no"), good_finding(id="F-002", built="maybe")])
        d["stage"] = "prototype"
        errs, _ = ldw.validate_findings(d)
        self.assertEqual([e for e in errs if "built" in e], ["F-002: built must be one of no, partial"])
        d["findings"].pop()
        md = ldw.findings_md(d)
        self.assertIn("Stage: prototype", md)
        self.assertIn("1 of them on parts not built yet", md)
        self.assertIn("(not built yet)", md)
        d["stage"] = "beta"
        self.assertTrue(any("stage" in e for e in ldw.validate_findings(d)[0]))

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "f.json")
            with open(p, "w", encoding="utf-8") as fh:
                json.dump(doc([good_finding(id="X")]), fh)
            with contextlib.redirect_stdout(io.StringIO()) as out:
                code = ldw.main(["findings", "validate", p])
            self.assertEqual(code, 1)
            self.assertIn("INVALID", out.getvalue())


class Maths(unittest.TestCase):
    def test_ev_golden(self):
        s = ldw.ev_stats([{"outcome": "miss", "value": 0, "weight": 1}, {"outcome": "hit", "value": 6, "weight": 2},
                          {"outcome": "crit", "value": 12, "weight": 1}])
        self.assertAlmostEqual(s["ev"], 6.0)
        self.assertAlmostEqual(s["sd"], math.sqrt(18))

    def test_curve_recovers_weights_and_flags_outlier(self):
        rows = [{"name": f"c{i}", "damage": d, "block": b, "cost": 1 + 0.5 * d + 0.25 * b} for i, (d, b) in
                enumerate([(2, 0), (4, 0), (0, 4), (0, 8), (2, 4), (6, 2)])]
        rows.append({"name": "bargain", "damage": 8, "block": 4, "cost": 2.0})  # fair cost is 6
        fit = ldw.fit_curve(rows, ["damage", "block"])
        self.assertIsNotNone(fit)
        bargain = [i for i in fit["items"] if i["name"] == "bargain"][0]
        self.assertLess(bargain["delta"], 0)
        clean = ldw.fit_curve(rows[:-1], ["damage", "block"])
        self.assertAlmostEqual(clean["weights"]["damage"], 0.5, places=4)
        self.assertAlmostEqual(clean["intercept"], 1.0, places=4)

    def test_economy_flags_leak_and_drain(self):
        t = {"rows": [{"resource": "gold", "kind": "source", "name": "mine", "amount": 5},
                      {"resource": "gold", "kind": "sink", "name": "upkeep", "amount": 2},
                      {"resource": "food", "kind": "start", "amount": 10},
                      {"resource": "food", "kind": "sink", "name": "eat", "amount": 3},
                      {"resource": "food", "kind": "source", "name": "farm", "amount": 1}]}
        e = ldw.economy(t, 10)
        self.assertEqual(e["gold"]["net"], 3)
        self.assertTrue(any(f.startswith("LEAK") for f in e["gold"]["flags"]))
        self.assertTrue(any(f.startswith("DRAIN: runs out by period 6") for f in e["food"]["flags"]))

    def test_sim_draw_mean_within_band_of_exact_ev(self):
        rows = [{"outcome": "a", "value": 0, "weight": 1}, {"outcome": "b", "value": 10, "weight": 1}]
        r = ldw.run_sim({"rows": rows, "model": "draw"}, steps=10, runs=4000, seed=7)
        exact = 50.0
        se = r["sd"] / math.sqrt(4000)
        self.assertLess(abs(r["mean"] - exact), 3 * se + 1e-9)
        self.assertEqual(r, ldw.run_sim({"rows": rows, "model": "draw"}, steps=10, runs=4000, seed=7))  # seeded = repeatable

    def test_sim_walk_and_deck(self):
        w = ldw.run_sim({"rows": [{"value": 3}], "model": "walk", "target": 10}, steps=20, runs=50, seed=1)
        self.assertEqual(w["steps_to_target"]["p50"], 4)
        d = ldw.run_sim({"rows": [{"name": "strike", "count": 5, "value": 6}, {"name": "defend", "count": 5, "value": 0}],
                         "model": "deck", "hand": 5}, steps=2, runs=200, seed=1)
        self.assertAlmostEqual(d["mean"], 30.0)  # two hands of five from a ten-card deck = every card once
        self.assertAlmostEqual(d["seen_share"]["strike"], 0.5)


if __name__ == "__main__":
    unittest.main()

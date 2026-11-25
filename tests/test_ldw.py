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
    def test_deck_shape_flags_and_counts(self):
        rows = [{"cost": c, "keywords": k, "pool": p, "upgrades": u} for c, k, p, u in
                [(0, "exhaust", "a", 2), (1, "exhaust;retain", "a", 2), (1, "", "a", 1), (2, "exhaust", "b", 2), (3, "", "b", 2)]]
        r = ldw.deck_shape(rows)
        self.assertEqual(r["cost_hist"], {0: 1, 1: 2, 2: 1, 3: 1})
        self.assertAlmostEqual(r["mean_cost"], 1.4)
        self.assertAlmostEqual(r["keywords"]["exhaust"], 0.6)
        self.assertAlmostEqual(r["branching_share"], 0.8)
        self.assertEqual(r["flags"], [])
        r = ldw.deck_shape(rows + [{"cost": 0, "keywords": "exhaust", "pool": "a"}] * 3)
        self.assertTrue(any(f.startswith("ZERO_COST") for f in r["flags"]))
        self.assertTrue(any(f.startswith("KEYWORD_EVERYWHERE exhaust") for f in r["flags"]))
        self.assertTrue(any(f.startswith("POOL_UNEVEN") for f in r["flags"]))

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

    def test_curve_folds_several_currencies(self):
        self.assertEqual(ldw.parse_rates("gold:1,wood:0.5,ore"), {"gold": 1.0, "wood": 0.5, "ore": 1.0})
        rows = [{"name": f"b{i}", "gold": g, "wood": w, "power": 1 + 0.5 * (g + 0.5 * w)} for i, (g, w) in
                enumerate([(2, 0), (4, 2), (0, 4), (6, 2), (2, 6), (8, 0)])]
        with tempfile.TemporaryDirectory() as td:
            p = os.path.join(td, "t.json")
            with open(p, "w", encoding="utf-8") as fh:
                json.dump({"rows": rows, "attrs": ["power"]}, fh)
            with contextlib.redirect_stdout(io.StringIO()) as out:
                code = ldw.main(["curve", p, "--costs", "gold:1,wood:0.5", "--json"])
        self.assertEqual(code, 0)
        fit = json.loads(out.getvalue())
        self.assertAlmostEqual(fit["weights"]["power"], 2.0, places=4)
        self.assertEqual(fit["flagged"], 0)

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



class KbSectionsTest(unittest.TestCase):
    def test_shaping_verb_and_stuck_hints_present(self):
        import pathlib
        kb = pathlib.Path(__file__).resolve().parent.parent / "skills" / "ludowright" / "kb"
        core = (kb / "core-loops-and-goals.md").read_text(encoding="utf-8")
        ux = (kb / "ux-and-the-brain.md").read_text(encoding="utf-8")
        index = (kb / "INDEX.md").read_text(encoding="utf-8")
        self.assertIn("## Shaping verb against a visible target", core)
        self.assertIn("## Staged stuck-hints", ux)
        self.assertIn("## Light-touch onboarding and a daily find", ux)
        self.assertIn("staged stuck-hints", index)
        self.assertIn("shaping verbs", index)

    def test_osrs_harvest_checks_present(self):
        import pathlib
        kb = pathlib.Path(__file__).resolve().parent.parent / "skills" / "ludowright" / "kb"
        more = (kb / "review-rubric-more.md").read_text(encoding="utf-8")
        for rid in ("R-83 Round trip", "R-84 Rounding", "R-85 Shared resource", "R-86 Disasters"):
            self.assertIn("### " + rid, more)
        self.assertIn("R-01 to R-86", (kb / "INDEX.md").read_text(encoding="utf-8"))

    def test_explorer_and_campos_lines_present(self):
        import pathlib
        kb = pathlib.Path(__file__).resolve().parent.parent / "skills" / "ludowright" / "kb"
        lore = (kb / "worldbuilding-and-lore.md").read_text(encoding="utf-8")
        ai = (kb / "game-ai-for-designers.md").read_text(encoding="utf-8")
        self.assertIn("## Adapting a co-made world", lore)
        lines = lore.splitlines()
        for n in range(10, 15):
            self.assertTrue(any(l.startswith(f"{n}. ") for l in lines), n)
        self.assertIn("State explosion", ai)

    def test_rubric_range_matches_last_item(self):
        import pathlib, re
        kb = pathlib.Path(__file__).resolve().parent.parent / "skills" / "ludowright" / "kb"
        more = (kb / "review-rubric-more.md").read_text(encoding="utf-8")
        last = max(int(n) for n in re.findall(r"^### R-([0-9]+)", more, re.M))
        self.assertEqual(last, 86)
        for f in ("INDEX.md", "review-rubric.md"):
            self.assertIn(f"R-53 to R-{last}" if f != "INDEX.md" else f"R-01 to R-{last}", (kb / f).read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()


class DrawOdds(unittest.TestCase):
    def test_golden_ace_in_five(self):
        r = ldw.draw_odds(52, 4, 5)
        self.assertAlmostEqual(r[1], 1 - 1712304 / 2598960, places=12)
        self.assertEqual(r[0], 1.0)
        self.assertAlmostEqual(r[4], 48 / 2598960, places=15)

    def test_whole_deck_and_zero_copies(self):
        self.assertAlmostEqual(ldw.draw_odds(10, 3, 10)[3], 1.0)
        self.assertEqual(ldw.draw_odds(10, 0, 4), [1.0])

    def test_bad_input_fails(self):
        with self.assertRaises(SystemExit):
            ldw.draw_odds(10, 11, 2)


class RampTest(unittest.TestCase):
    # Two invented ramps of common shapes: a spawn interval that shrinks 6% per point to a floor, and a fall
    # speed that adds a little every frame with no cap.
    SHRINK = {"name": "spawn interval", "base": 3, "factor": 0.94, "floor": 0.6, "per": "point"}
    GROW = {"name": "fall speed", "base": 4, "add": 0.009, "per": "frame", "steps": 3600, "step_seconds": 1 / 60}

    def run_cli(self, ramps, *args):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "ramps.json")
            with open(p, "w", encoding="utf-8") as f:
                json.dump({"ramps": ramps}, f)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                ldw.main(["ramp", p, *args])
            return buf.getvalue()

    def test_shrinking_ramp_floors_at_27(self):
        r = ldw.ramp(self.SHRINK)
        self.assertEqual(r["floor_at"], 27)  # raw 3 x 0.94^26 is 0.6003, still above the floor
        self.assertAlmostEqual(r["values"]["1"], 2.82)
        self.assertAlmostEqual(r["values"]["26"], 3 * 0.94 ** 26)
        self.assertEqual(r["values"]["100"], 0.6)
        self.assertEqual(r["flags"], ["FLOOR@27"])
        out = self.run_cli([self.SHRINK])
        self.assertIn("FLOOR@27", out)
        self.assertIn("step 1 2.82", out)

    def test_growing_ramp_is_uncapped(self):
        r = ldw.ramp(self.GROW)
        self.assertIn("UNCAPPED", r["flags"])
        self.assertGreater(r["ratio"], 8)
        self.assertAlmostEqual(r["values"]["3600"], 4 + 0.009 * 3600)
        out = self.run_cli([self.GROW])
        self.assertIn("UNCAPPED", out)
        self.assertIn("(60 s)", out)
        capped = ldw.ramp(dict(self.GROW, cap=12))
        self.assertNotIn("UNCAPPED", capped["flags"])
        self.assertIn("CAP@889", capped["flags"])  # 4 + 0.009n reaches 12 at n = 888.9

    def test_flat_early(self):
        self.assertIn("FLAT-EARLY", ldw.ramp({"base": 1, "factor": 0.5, "floor": 0.4})["flags"])
        tiers = ldw.ramp({"name": "tiers", "values": {"0": 10, "2": 10, "4": 10, "6": 14, "8": 18, "10": 20, "12": 20}})
        self.assertEqual(tiers["flags"], ["CAP@10", "FLAT-EARLY"])
        self.assertEqual(tiers["flat_reason"], "no change over the first steps")
        self.assertNotIn("FLAT-EARLY", ldw.ramp(self.SHRINK)["flags"])

    def test_steps_override_and_shrink_without_floor(self):
        r = ldw.ramp(dict(self.SHRINK, floor=None), steps=50)
        self.assertEqual(r["steps"], 50)
        self.assertIn("UNCAPPED", r["flags"])

    def test_json_matches_text(self):
        data = json.loads(self.run_cli([self.SHRINK, self.GROW], "--json"))
        self.assertEqual([d["flags"] for d in data], [["FLOOR@27"], ["UNCAPPED"]])
        self.assertAlmostEqual(data[0]["values"]["1"], 2.82)

    def test_csv_table(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "ramp.csv")
            with open(p, "w", encoding="utf-8") as f:
                f.write("name,step,value\nwaves,0,2\nwaves,1,3\nwaves,2,5\nwaves,3,8\n")
            rows = ldw.ramp_rows(p)
        r = ldw.ramp(rows[0])
        self.assertEqual(r["kind"], "table")
        self.assertEqual(r["flags"], ["UNCAPPED"])

    def test_bad_ramp_fails(self):
        with self.assertRaises(SystemExit):
            ldw.ramp({"base": 1, "factor": 0.5, "add": 1})


class StopTest(unittest.TestCase):
    COIN = [{"value": 0}, {"value": 100}]

    def test_free_waiting_finds_the_top(self):
        r = ldw.stop_check({"steps": 12, "option": self.COIN, "attrition": [{"value": 0}]}, runs=20000, seed=1)
        self.assertEqual(r["best"]["threshold"], 100)
        self.assertAlmostEqual(r["best"]["ev"], 100 * (1 - 0.5 ** 12), delta=0.2)
        self.assertAlmostEqual(r["ev_first"], 50, delta=3 * 50 / math.sqrt(20000))
        self.assertIn("NO-COST", r["flags"])

    def test_lethal_attrition_means_settle_first(self):
        r = ldw.stop_check({"steps": 12, "option": self.COIN, "attrition": [{"value": -100}]}, runs=5000, seed=1)
        self.assertIn("FIRST-IS-BEST", r["flags"])
        self.assertAlmostEqual(r["best"]["ev"], r["ev_first"], delta=3 * 50 / math.sqrt(5000))

    def test_noise_costs_value_and_oracle_bounds(self):
        t = {"steps": 12, "attributes": 5, "option": [{"weight": 2, "value": 100}, {"weight": 3, "value": 50},
             {"weight": 5, "value": 0}], "attrition": [{"weight": 2, "value": 0}, {"weight": 6, "value": -8},
             {"weight": 2, "value": -25}]}
        clear = ldw.stop_check(dict(t), runs=20000, seed=1)
        noisy = ldw.stop_check(dict(t, noisy=True), runs=20000, seed=1)
        self.assertEqual(clear["flags"], ["TENSE"])
        self.assertLess(noisy["best"]["ev"], clear["best"]["ev"])
        self.assertLessEqual(clear["best"]["ev"], clear["ev_oracle"])
        self.assertGreater(clear["best"]["ev"], clear["ev_first"] * 1.05)


FIXTURES = os.path.join(os.path.dirname(__file__), "..", "skills", "ludowright", "evals")


class Director(unittest.TestCase):
    WINDOWED = {"grace": 11, "comps": [{"category": "big_threat", "kind": "onoff", "start_day": 11, "on_days": 4.6,
                                         "off_days": 6, "count": [1, 2], "min_spacing": 1.9}]}

    def test_windowed_respects_grace_spacing_and_rate(self):
        r = ldw.director(self.WINDOWED, days=1000, runs=500, seed=1)
        self.assertGreaterEqual(r["first_threat_min"], 11)
        self.assertGreaterEqual(r["min_spacing_seen"], 1.9 - 1e-9)
        expected = 1.5 / 10.6 * 30
        self.assertAlmostEqual(r["per_30_days"]["big_threat"], expected, delta=0.15 * expected)
        self.assertEqual(r["flags"], ["PACED"])

    def test_weighted_mtb_matches_weight_shares(self):
        w = {"misc": 3.5, "big_threat": 1.4, "arrival": 2.4, "small_threat": 0.6}
        t = {"comps": [{"kind": "mtb", "mtb_days": 1.35, "choices": [{"category": k, "weight": v} for k, v in w.items()]}]}
        r = ldw.director(t, days=120, runs=2000, seed=1)
        tot = sum(r["per_30_days"].values())
        for k, v in w.items():
            self.assertAlmostEqual(r["per_30_days"][k] / tot, v / sum(w.values()), delta=0.03)
        self.assertAlmostEqual(tot, 30 / 1.35, delta=1.0)

    def test_clumped_and_runaway_flags(self):
        t = {"comps": [{"category": "threat", "kind": "mtb", "mtb_days": 0.5}], "budget": [[0, 1], [120, 5]]}
        flags = ldw.director(t, days=120, runs=200, seed=1)["flags"]
        for f in ("CLUMP", "NO-BREATHER", "RUNAWAY"):
            self.assertIn(f, flags)
        t["adapt"] = {"per_day": 0, "max": 10}
        self.assertNotIn("RUNAWAY", ldw.director(t, days=120, runs=50, seed=1)["flags"])

    def test_early_threat_before_grace(self):
        t = dict(self.WINDOWED, grace=20)
        self.assertIn("EARLY-THREAT", ldw.director(t, days=60, runs=50, seed=1)["flags"])


class Mood(unittest.TestCase):
    def table(self, **ev):
        e = {"name": "nuisance", "effect": -3, "duration_h": 24, "rate_per_day": 8}
        e.update(ev)
        return {"base": 50, "rise_per_hour": 6, "fall_per_hour": 4, "threshold": 35,
                "bands": {"minor": 0, "major": 10, "extreme": 20}, "events": [e]}

    def test_uncapped_nuisance_flags(self):
        r = ldw.mood(self.table(), hours=720, runs=50, seed=1)
        self.assertIn("UNCAPPED", r["flags"])
        self.assertIn("ALWAYS-BREAKS", r["flags"])
        self.assertAlmostEqual(r["p50"], 50 - 3 * 8, delta=2)

    def test_capped_half_multiplier_settles(self):
        r = ldw.mood(self.table(stack_limit=3, stack_mult=0.5), hours=720, runs=50, seed=1)
        self.assertNotIn("UNCAPPED", r["flags"])
        self.assertAlmostEqual(r["p50"], 50 - 3 - 1.5 - 0.75, delta=0.5)
        self.assertEqual(r["flags"], ["NEVER-BREAKS"])

    def test_spike_when_rates_equal_and_high(self):
        t = self.table(stack_limit=1)
        t.update(rise_per_hour=40, fall_per_hour=40)
        self.assertIn("SPIKE", ldw.mood(t, hours=48, runs=5, seed=1)["flags"])


class Grammar(unittest.TestCase):
    def setUp(self):
        with open(os.path.join(FIXTURES, "grammar-fixture.json"), encoding="utf-8") as f:
            self.g = json.load(f)

    def test_flags_count_and_weights(self):
        r = ldw.grammar(self.g, "r_name", samples=2000, seed=1, consts={"flesh": "Machine"})
        self.assertEqual(r["undefined"], ["missing"])
        self.assertEqual(r["dead_under"], ["r_blood"])
        self.assertEqual(r["combinations"], 8 * 8 + 5 + 5 * 3)
        top = r["alternatives"][0]
        self.assertAlmostEqual(top["expected"], 12 / 23, places=6)
        self.assertAlmostEqual(top["observed"], 0.52, delta=0.05)
        self.assertIn("LOW-VARIETY", r["flags"])

    def test_condition_and_priority_fallback(self):
        r = ldw.grammar(self.g, "r_wound", samples=50, seed=1, consts={"flesh": "Machine"})
        self.assertEqual([a["rhs"] for a in r["alternatives"]], ["a dented plate"])
        r = ldw.grammar(self.g, "r_wound", samples=50, seed=1)
        self.assertEqual(r["dead_under"], [])
        self.assertEqual(r["combinations"], 2)

    def test_recursion_and_cli_exit(self):
        g = {"rules": [{"lhs": "r_name", "rhs": "[r_name]a"}, {"lhs": "r_name", "rhs": "b"}]}
        self.assertEqual(ldw.grammar(g, samples=20)["recursive"], ["r_name"])
        with contextlib.redirect_stdout(io.StringIO()):
            code = ldw.main(["grammar", os.path.join(FIXTURES, "grammar-fixture.json"), "--samples", "100"])
        self.assertEqual(code, 1)


class RimHarvestKb(unittest.TestCase):
    def test_sections_present(self):
        import pathlib
        kb = pathlib.Path(__file__).resolve().parent.parent / "skills" / "ludowright" / "kb"
        tables = (kb / "balance-tables.md").read_text(encoding="utf-8")
        for h in ("## director:", "## mood:", "## grammar:"):
            self.assertIn(h, tables)
        self.assertIn("ldw.py grammar", (kb / "procgen.md").read_text(encoding="utf-8"))
        self.assertIn("ldw.py mood", (kb / "balance-and-economy.md").read_text(encoding="utf-8"))


class GrowthTest(unittest.TestCase):
    # Invented bands: 10 cards at start, +5 per stage, end in 25-30, ceiling 40; level-ups add cards each stage.
    BAND = {"per_stage": 5, "end_low": 25, "end_high": 30, "ceiling": 40}

    def table(self, removal=0):
        st = [{"name": i, "adds": {"level-up": 5, "reward": 1}, "removals": {"paid": removal} if removal else {}} for i in range(1, 4)]
        return {"start": 10, "band": self.BAND, "stages": st}

    def test_no_removal_is_no_thin(self):
        r = ldw.growth(self.table())
        self.assertEqual(r["end"], 28)
        self.assertEqual(r["flags"], ["NO-THIN"])
        self.assertEqual(r["stages"][0]["target"], 15)

    def test_one_removal_per_stage_clears(self):
        r = ldw.growth(self.table(removal=1))
        self.assertEqual(r["end"], 25)
        self.assertEqual(r["flags"], ["ON-BAND"])

    def test_bloat_and_off_band(self):
        t = {"start": 10, "band": self.BAND, "stages": [{"adds": {"a": 12}, "removals": {"b": 1}}] * 3}
        self.assertEqual(ldw.growth(t)["flags"], ["BLOAT", "OFF-BAND"])

    def test_starved_and_flooded(self):
        cards = [{"copies": 1, "produce": 2}, {"copies": 6, "consume": 1}]
        r = ldw.growth(dict(self.table(1), resource={"name": "ammo", "hand": 5, "deck": 20, "cards": cards}))
        self.assertAlmostEqual(r["resource"]["ratio"], 2 / 6)
        self.assertIn("STARVED", r["flags"])
        cards = [{"copies": 6, "produce": 1}, {"copies": 1, "consume": 1}]
        self.assertIn("FLOODED", ldw.growth(dict(self.table(1), resource={"cards": cards}))["flags"])


class QuotaTest(unittest.TestCase):
    def test_tripling_quota_outruns_growing_income(self):
        # Income 10 x 1.15^n per period (about 2x per window); payments triple every time, 5 periods each.
        t = {"income": {"base": 10, "factor": 1.15}, "payments": [{"amount": 30 * 3 ** i, "periods": 5} for i in range(5)]}
        r = ldw.quota(t)
        exp0 = sum(10 * 1.15 ** k for k in range(5))
        self.assertAlmostEqual(r["payments"][0]["expected"], exp0)
        self.assertAlmostEqual(r["payments"][0]["slack"], exp0 / 30)
        tight = [p["payment"] for p in r["payments"] if "TIGHT" in p["flags"]]
        self.assertEqual(tight[0], 4)  # slack 2.25, 1.51, 1.01, then 0.68
        self.assertIn("CLIFF", r["flags"])

    def test_flat_income_is_tight_early(self):
        t = {"income": {"base": 10, "add": 0}, "payments": [{"amount": a, "periods": 5} for a in (40, 60, 90)]}
        r = ldw.quota(t)
        self.assertEqual(r["payments"][1]["flags"], ["TIGHT"])
        self.assertEqual(r["payments"][0]["flags"], [])

    def test_loose_after_three(self):
        t = {"income": {"base": 10, "add": 0}, "payments": [{"amount": 10, "periods": 5}] * 3}
        self.assertEqual(ldw.quota(t)["payments"][2]["flags"], ["LOOSE"])
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "q.json")
            with open(p, "w", encoding="utf-8") as f:
                json.dump(t, f)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                ldw.main(["quota", p])
            self.assertIn("LOOSE", buf.getvalue())

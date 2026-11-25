import json
import os
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "skills" / "design-variety" / "scripts"
sys.path.insert(0, str(SCRIPTS))

import seed  # noqa: E402
from data import DIRECTIONS, LAYOUTS, TYPES  # noqa: E402

HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")


class DataTests(unittest.TestCase):
    def test_enough_variety(self):
        self.assertGreaterEqual(len(DIRECTIONS), 20)
        self.assertGreaterEqual(sum(len(d["palettes"]) for d in DIRECTIONS.values()), 45)

    def test_direction_schema(self):
        required = {"vibe", "types", "fonts", "palettes", "tokens", "rules", "layouts", "signatures", "motion"}
        token_keys = {"radius", "border", "shadow", "h_case", "h_weight", "h_tracking", "h_leading"}
        for name, d in DIRECTIONS.items():
            with self.subTest(name):
                self.assertTrue(required <= set(d), f"missing keys in {name}")
                self.assertTrue(set(d["types"]) <= set(TYPES))
                self.assertTrue(token_keys <= set(d["tokens"]))
                self.assertGreaterEqual(len(d["rules"]), 4)
                self.assertGreaterEqual(len(d["signatures"]), 3)
                self.assertGreaterEqual(len(d["fonts"]), 2)
                for k in d["layouts"]:
                    self.assertIn(k, LAYOUTS)
                self.assertIn(d["tokens"]["h_weight"], ("400", "700"))

    def test_palette_contrast(self):
        for name, d in DIRECTIONS.items():
            for pname, bg, text, accent, sec in d["palettes"]:
                with self.subTest(f"{name}/{pname}"):
                    for c in (bg, text, accent, sec):
                        self.assertRegex(c, HEX)
                    self.assertGreaterEqual(seed.contrast(text, bg), 7.0, "body text must be >= 7:1")
                    self.assertGreaterEqual(seed.contrast(accent, bg), 3.0, "accent must be >= 3:1")

    def test_every_type_has_directions_and_layouts(self):
        for t in TYPES:
            with self.subTest(t):
                self.assertGreaterEqual(sum(t in d["types"] for d in DIRECTIONS.values()), 4)
                self.assertGreaterEqual(sum(t in v[1] for v in LAYOUTS.values()), 2)

    def test_both_themes_available(self):
        dark = sum(seed.is_dark(p[1]) for d in DIRECTIONS.values() for p in d["palettes"])
        light = sum(not seed.is_dark(p[1]) for d in DIRECTIONS.values() for p in d["palettes"])
        self.assertGreaterEqual(dark, 12)
        self.assertGreaterEqual(light, 12)


class BriefTests(unittest.TestCase):
    def test_deterministic(self):
        self.assertEqual(seed.build_brief(seed=7), seed.build_brief(seed=7))

    def test_variety_across_seeds(self):
        dirs = {seed.build_brief(seed=i)["direction"] for i in range(200)}
        self.assertGreaterEqual(len(dirs), 18)

    def test_type_filter(self):
        for t in TYPES:
            for i in range(30):
                b = seed.build_brief(seed=i, ptype=t)
                with self.subTest(t, i=i):
                    self.assertIn(t, DIRECTIONS[b["direction"]]["types"])
                    self.assertIn(t, LAYOUTS[b["layout"]["key"]][1])

    def test_theme_filter(self):
        for i in range(60):
            self.assertEqual(seed.build_brief(seed=i, theme="dark")["theme"], "dark")
            self.assertEqual(seed.build_brief(seed=i, theme="light")["theme"], "light")

    def test_brief_is_coherent(self):
        for i in range(100):
            b = seed.build_brief(seed=i)
            d = DIRECTIONS[b["direction"]]
            self.assertIn((b["fonts"]["display"], b["fonts"]["body"]), d["fonts"])
            self.assertIn(b["signature"], d["signatures"])
            self.assertIn(b["palette"]["name"], [p[0] for p in d["palettes"]])
            self.assertGreaterEqual(seed.contrast(b["palette"]["on_accent"], b["palette"]["accent"]), 3.0)

    def test_errors(self):
        with self.assertRaises(ValueError):
            seed.build_brief(direction="nope")
        with self.assertRaises(ValueError):
            seed.build_brief(ptype="spaceship")
        with self.assertRaises(ValueError):
            seed.build_brief(direction="retro-terminal", theme="light")

    def test_avoid_recent(self):
        recent = list(DIRECTIONS)[:5]
        for i in range(50):
            self.assertNotIn(seed.build_brief(seed=i, avoid=recent)["direction"], recent)

    def test_fonts_url(self):
        url = seed.fonts_url("VT323", "IBM Plex Mono")
        self.assertIn("family=VT323&", url)
        self.assertIn("family=IBM+Plex+Mono:wght@400;700", url)


class CliTests(unittest.TestCase):
    def run_cli(self, *args, env=None):
        e = dict(os.environ, **(env or {}))
        return subprocess.run([sys.executable, str(SCRIPTS / "seed.py"), *args],
                              capture_output=True, text=True, env=e)

    def test_text_and_json(self):
        r = self.run_cli("--seed", "1")
        self.assertEqual(r.returncode, 0)
        self.assertIn("DESIGN BRIEF", r.stdout)
        j = json.loads(self.run_cli("--seed", "1", "--json").stdout)
        self.assertEqual(j["direction"], seed.build_brief(seed=1)["direction"])

    def test_bad_args_exit_2(self):
        self.assertEqual(self.run_cli("--direction", "nope").returncode, 2)

    def test_remember_avoids_repeats(self):
        with tempfile.TemporaryDirectory() as home:
            env = {"DESIGN_VARIETY_HOME": home}
            seen = []
            for _ in range(12):
                out = json.loads(self.run_cli("--remember", "--json", env=env).stdout)
                seen.append(out["direction"])
            for i in range(5, len(seen)):
                self.assertNotIn(seen[i], seen[i - 5:i])


class DocsTests(unittest.TestCase):
    def test_docs_in_sync(self):
        """references/directions must be regenerated after editing data.py."""
        import build_docs
        for name, d in DIRECTIONS.items():
            with self.subTest(name):
                path = build_docs.OUT / f"{name}.md"
                self.assertTrue(path.exists(), f"{path} missing: run build_docs.py")
                self.assertEqual(path.read_text(encoding="utf-8"), build_docs.build_one(name, d),
                                 f"{name}.md is stale: run build_docs.py")


if __name__ == "__main__":
    unittest.main()

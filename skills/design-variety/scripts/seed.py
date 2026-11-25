#!/usr/bin/env python3
"""design-variety seed: picks a random, concrete, *coherent* design brief.

Left alone, an LLM converges on the same look every time. Randomness chosen
BEFORE designing breaks that habit. The pick is coherent: palettes, fonts,
layouts and signatures all belong to the chosen direction, and every palette
passes a WCAG contrast check.

Usage:
  python3 seed.py                         random brief
  python3 seed.py --type dashboard        only directions that suit this product type
  python3 seed.py --dark | --light        force theme
  python3 seed.py --direction brutalist   force direction
  python3 seed.py --seed 42               reproducible
  python3 seed.py --remember              avoid the last 5 directions used (stored in
                                          ~/.design-variety/history.json)
  python3 seed.py --json                  machine-readable output
  python3 seed.py --list                  list directions
"""
import argparse
import json
import os
import random
import sys
from pathlib import Path
from urllib.parse import quote_plus

sys.path.insert(0, str(Path(__file__).resolve().parent))
from data import DIRECTIONS, LAYOUTS, SINGLE_WEIGHT, TYPES  # noqa: E402

HISTORY_LEN = 5

FORBIDDEN = [
    "Purple-to-blue gradient hero",
    "Inter/Roboto/system-ui as the only font",
    "Three identical feature cards in a row (icon + title + text)",
    "Centered hero + two buttons + 'trusted by' logo strip",
    "Uniform rounded-2xl cards with soft shadow on gray-50",
    "Emoji used as icons",
    "Glassmorphism on everything",
]


# ---------- color math ----------
def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def luminance(hex_color):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def is_dark(bg):
    return luminance(bg) < 0.18


def on_accent(accent, bg, text):
    """Best text color for a button filled with the accent."""
    return bg if contrast(accent, bg) >= contrast(accent, text) else text


# ---------- helpers ----------
def fonts_url(*families):
    parts = []
    for f in dict.fromkeys(families):
        q = quote_plus(f)
        parts.append(f"family={q}" if f in SINGLE_WEIGHT else f"family={q}:wght@400;700")
    return "https://fonts.googleapis.com/css2?" + "&".join(parts) + "&display=swap"


def history_path():
    base = os.environ.get("DESIGN_VARIETY_HOME") or os.path.join(os.path.expanduser("~"), ".design-variety")
    return Path(base) / "history.json"


def load_history():
    try:
        return json.loads(history_path().read_text())[-HISTORY_LEN:]
    except (OSError, ValueError):
        return []


def save_history(name):
    hist = load_history() + [name]
    p = history_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(hist[-HISTORY_LEN:]))


def build_brief(seed=None, direction=None, ptype=None, theme=None, avoid=()):
    rng = random.Random(seed)
    if ptype and ptype not in TYPES:
        raise ValueError(f"Unknown type '{ptype}'. Choose from: {', '.join(TYPES)}")

    def palettes_for(d):
        pals = DIRECTIONS[d]["palettes"]
        if theme == "dark":
            return [p for p in pals if is_dark(p[1])]
        if theme == "light":
            return [p for p in pals if not is_dark(p[1])]
        return list(pals)

    def eligible(d):
        spec = DIRECTIONS[d]
        return (not ptype or ptype in spec["types"]) and bool(palettes_for(d))

    if direction:
        if direction not in DIRECTIONS:
            raise ValueError(f"Unknown direction '{direction}'. Use --list.")
        if not palettes_for(direction):
            raise ValueError(f"Direction '{direction}' has no {theme} palette.")
        name = direction
    else:
        pool = [d for d in DIRECTIONS if eligible(d)]
        if not pool:
            raise ValueError("No direction matches those filters.")
        fresh = [d for d in pool if d not in avoid]
        name = rng.choice(fresh or pool)

    d = DIRECTIONS[name]
    pname, bg, text, accent, secondary = rng.choice(palettes_for(name))
    display, body = rng.choice(d["fonts"])

    layout_pool = [k for k in d["layouts"] if not ptype or ptype in LAYOUTS[k][1]]
    if not layout_pool:
        layout_pool = [k for k, (_, types) in LAYOUTS.items() if not ptype or ptype in types]
    layout_key = rng.choice(layout_pool)

    return {
        "direction": name,
        "vibe": d["vibe"],
        "product_type": ptype,
        "theme": "dark" if is_dark(bg) else "light",
        "palette": {
            "name": pname, "bg": bg, "text": text, "accent": accent, "secondary": secondary,
            "on_accent": on_accent(accent, bg, text),
            "contrast_text": round(contrast(text, bg), 1),
            "contrast_accent": round(contrast(accent, bg), 1),
        },
        "fonts": {"display": display, "body": body, "google_fonts_url": fonts_url(display, body)},
        "tokens": d["tokens"],
        "layout": {"key": layout_key, "description": LAYOUTS[layout_key][0]},
        "signature": rng.choice(d["signatures"]),
        "motion": d["motion"],
        "rules": d["rules"],
        "forbidden": FORBIDDEN,
        "reference": f"references/directions/{name}.md",
    }


def render(b):
    p, t = b["palette"], b["tokens"]
    out = [
        "=== DESIGN BRIEF (commit to this; do not drift to defaults) ===",
        f"Direction : {b['direction']} - {b['vibe']}",
        f"Theme     : {b['theme']}" + (f"   (for a {b['product_type']})" if b["product_type"] else ""),
        f"Palette   : {p['name']}  bg {p['bg']}  text {p['text']}  accent {p['accent']}  "
        f"secondary {p['secondary']}  on-accent {p['on_accent']}",
        f"Contrast  : text/bg {p['contrast_text']}:1, accent/bg {p['contrast_accent']}:1 (verified)",
        f"Fonts     : display = {b['fonts']['display']} | body = {b['fonts']['body']}",
        f"Fonts URL : {b['fonts']['google_fonts_url']}",
        f"Tokens    : radius {t['radius']} | border {t['border']} | shadow {t['shadow']}",
        f"Headings  : case {t['h_case']}, weight {t['h_weight']}, tracking {t['h_tracking']}, leading {t['h_leading']}",
        f"Layout    : {b['layout']['description']}",
        f"Signature : {b['signature']}  (use it in 3+ places)",
        f"Motion    : {b['motion']}",
        "Direction rules:",
        *[f"  - {r}" for r in b["rules"]],
        "Forbidden defaults:",
        *[f"  x {f}" for f in b["forbidden"]],
        f"Next: read {b['reference']} for the CSS starter, then build.",
        "Bend the brief only if the product genuinely needs it; say what you changed and why.",
    ]
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Random, coherent design brief.")
    ap.add_argument("--seed", type=int)
    ap.add_argument("--direction")
    ap.add_argument("--type", dest="ptype", help="/".join(TYPES))
    ap.add_argument("--remember", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--list", action="store_true")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--dark", action="store_true")
    g.add_argument("--light", action="store_true")
    a = ap.parse_args(argv)

    if a.list:
        for k, v in DIRECTIONS.items():
            print(f"{k:18} {', '.join(v['types']):45} {v['vibe']}")
        return 0

    theme = "dark" if a.dark else "light" if a.light else None
    try:
        brief = build_brief(a.seed, a.direction, a.ptype, theme,
                            avoid=load_history() if a.remember else ())
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if a.remember:
        save_history(brief["direction"])
    print(json.dumps(brief, indent=2, ensure_ascii=False) if a.json else render(brief))
    return 0


if __name__ == "__main__":
    sys.exit(main())

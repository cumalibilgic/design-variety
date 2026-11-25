#!/usr/bin/env python3
"""Generate references/directions/*.md from data.py (one mini design system per direction).

Run after editing data.py:  python3 build_docs.py
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from data import DIRECTIONS, LAYOUTS  # noqa: E402
from seed import contrast, fonts_url, is_dark, on_accent  # noqa: E402

OUT = HERE.parent / "references" / "directions"


def css_starter(name, d, pal, fonts):
    t = d["tokens"]
    pname, bg, text, accent, sec = pal
    oa = on_accent(accent, bg, text)
    display, body = fonts
    return f"""```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts_url(display, body)}" rel="stylesheet">
```

```css
:root {{
  --bg: {bg};
  --text: {text};
  --accent: {accent};          /* large text, borders, fills only */
  --on-accent: {oa};      /* text on accent-filled buttons */
  --secondary: {sec};       /* decorative / muted, never body text */
  --font-display: "{display}", {"monospace" if "Mono" in display or display in ("VT323",) else "serif" if display in ("Fraunces", "Playfair Display", "Instrument Serif", "DM Serif Display", "Cormorant Garamond", "Bodoni Moda", "Young Serif", "Gloock", "Italiana", "Marcellus", "Cinzel", "Limelight", "Old Standard TT", "Abril Fatface", "Shippori Mincho", "Cormorant", "UnifrakturCook") else "sans-serif"};
  --font-body: "{body}", {"monospace" if "Mono" in body else "serif" if body in ("Libre Baskerville", "Special Elite") else "sans-serif"};
  --radius: {t['radius']};
  --border: {t['border']};
  --shadow: {t['shadow']};
  --space: clamp(1rem, 0.6rem + 1.6vw, 2rem);
}}

* {{ box-sizing: border-box; }}
html {{ background: var(--bg); color: var(--text); }}
body {{ margin: 0; font-family: var(--font-body); line-height: 1.6; font-size: 1.0625rem; }}
::selection {{ background: var(--accent); color: var(--on-accent); }}

h1, h2, h3 {{
  font-family: var(--font-display);
  font-weight: {t['h_weight']};
  text-transform: {t['h_case']};
  letter-spacing: {t['h_tracking']};
  line-height: {t['h_leading']};
  margin: 0 0 .4em;
}}
h1 {{ font-size: clamp(2.75rem, 1.2rem + 7vw, 7.5rem); }}
h2 {{ font-size: clamp(1.75rem, 1rem + 3vw, 3.5rem); }}

.card {{
  background: var(--bg);
  border: var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: var(--space);
}}

.btn {{
  font: inherit; font-family: var(--font-display);
  background: var(--accent); color: var(--on-accent);
  border: var(--border); border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: .8em 1.4em; cursor: pointer;
  text-transform: {t['h_case']}; letter-spacing: {t['h_tracking'] if t['h_tracking'] != '-0.04em' else '0'};
}}
.btn:focus-visible, a:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 3px; }}

@media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; transition: none !important; }} }}
```"""


def build_one(name, d):
    lines = [f"# {name}", "", f"> {d['vibe']}", ""]
    lines += ["**Best for:** " + ", ".join(d["types"]), ""]
    lines += ["## Palettes (contrast verified)", "",
              "| Name | bg | text | accent | secondary | text/bg | accent/bg |",
              "|---|---|---|---|---|---|---|"]
    for n, bg, tx, ac, se in d["palettes"]:
        lines.append(f"| {n} | `{bg}` | `{tx}` | `{ac}` | `{se}` | {contrast(tx, bg):.1f}:1 | {contrast(ac, bg):.1f}:1 |")
    lines += ["", "Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.", ""]
    lines += ["## Fonts (Google Fonts)", ""]
    for disp, body in d["fonts"]:
        lines.append(f"- display **{disp}** + body **{body}**")
    lines += ["", "## Tokens", "", "| Token | Value |", "|---|---|"]
    for k, v in d["tokens"].items():
        lines.append(f"| `{k}` | `{v}` |")
    lines += ["", "## Rules (follow literally)", ""] + [f"- {r}" for r in d["rules"]]
    lines += ["", "## Signature ideas (pick one, use it 3+ times)", ""] + [f"- {s}" for s in d["signatures"]]
    lines += ["", "## Layouts that fit", ""]
    for k in d["layouts"]:
        lines.append(f"- **{k}**: {LAYOUTS[k][0]}")
    lines += ["", "## Motion", "", d["motion"], ""]
    pal = d["palettes"][0]
    lines += ["## CSS starter", "",
              f"Uses the first palette ({pal[0]}) and first font pair; swap in the brief's choices.", "",
              css_starter(name, d, pal, d["fonts"][0]), ""]
    return "\n".join(lines)


def build_index():
    lines = ["# Directions index", "",
             "| Direction | Theme(s) | Best for | Vibe |", "|---|---|---|---|"]
    for n, d in DIRECTIONS.items():
        themes = sorted({"dark" if is_dark(p[1]) else "light" for p in d["palettes"]})
        lines.append(f"| [{n}]({n}.md) | {'/'.join(themes)} | {', '.join(d['types'])} | {d['vibe']} |")
    lines.append("")
    return "\n".join(lines)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for n, d in DIRECTIONS.items():
        (OUT / f"{n}.md").write_text(build_one(n, d), encoding="utf-8")
    (OUT / "INDEX.md").write_text(build_index(), encoding="utf-8")
    print(f"wrote {len(DIRECTIONS)} direction files + INDEX.md to {OUT}")


if __name__ == "__main__":
    main()

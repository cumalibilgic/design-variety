#!/usr/bin/env python3
"""Rebuild docs/screenshots/*.png and docs/comparison.png from examples/*.html.
Needs google-chrome (headless) and Pillow. Run from the repo root."""
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SHOTS = ROOT / "docs" / "screenshots"
SHOTS.mkdir(parents=True, exist_ok=True)
PAGES = [("00-default-ai", "WITHOUT the skill", "default AI look"),
         ("01-brutalist", "brutalist", "seed.py --direction brutalist"),
         ("02-editorial", "editorial", "seed.py --direction editorial"),
         ("03-dark-luxe", "dark-luxe", "seed.py --direction dark-luxe"),
         ("04-playful-geometric", "playful-geometric", "seed.py --direction playful-geometric")]

for name, *_ in PAGES:
    subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--virtual-time-budget=4000", f"--screenshot={SHOTS / (name + '.png')}",
                    "--window-size=1440,1000", f"file://{ROOT / 'examples' / (name + '.html')}"],
                   check=True, capture_output=True, timeout=120)

W, H, pad, cap = 720, 500, 24, 64
sheet = Image.new("RGB", (3 * W + 4 * pad, 2 * (H + cap) + 3 * pad), "#16181d")
d = ImageDraw.Draw(sheet)
fb = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
fr = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 16)
for i, (f, t, s) in enumerate(PAGES):
    x, y = pad + (i % 3) * (W + pad), pad + (i // 3) * (H + cap + pad)
    sheet.paste(Image.open(SHOTS / f"{f}.png").convert("RGB").resize((W, H), Image.LANCZOS), (x, y))
    d.rectangle([x - 1, y - 1, x + W, y + H], outline="#555")
    d.text((x, y + H + 10), t, font=fb, fill="#ff6b6b" if i == 0 else "#7CF2D4")
    d.text((x, y + H + 38), s, font=fr, fill="#9aa0a6")
x, y = pad + 2 * (W + pad), pad + (H + cap + pad)
d.text((x, y + 10), "Same product. Same prompt.", font=fb, fill="#ffffff")
for k, l in enumerate(["Left column: what you get by default.", "Other four: one `seed.py` call each,",
                       "then the brief is followed literally.", "",
                       "Screenshots use offline fallback fonts;", "open examples/*.html for the real ones."]):
    d.text((x, y + 56 + k * 28), l, font=fr, fill="#c9ced6")
sheet.save(ROOT / "docs" / "comparison.png", optimize=True)
print("ok", sheet.size)

# wabi-sabi

> Japanese minimalism: emptiness, imperfection, ink and paper.

**Best for:** portfolio, blog, ecommerce, landing

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Washi | `#F3EEE3` | `#2A2723` | `#B23A2E` | `#8C857A` | 12.8:1 | 5.1:1 |
| Sumi | `#14130F` | `#E9E4D7` | `#D9604E` | `#4A463E` | 14.6:1 | 5.1:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Shippori Mincho** + body **Zen Kaku Gothic New**
- display **Cormorant** + body **Noto Sans**

## Tokens

| Token | Value |
|---|---|
| `radius` | `2px` |
| `border` | `1px solid color-mix(in srgb, var(--text) 25%, transparent)` |
| `shadow` | `none` |
| `h_case` | `none` |
| `h_weight` | `400` |
| `h_tracking` | `0.04em` |
| `h_leading` | `1.3` |

## Rules (follow literally)

- Extreme whitespace; at most 3-4 elements per screen
- Vertical writing for one key element (writing-mode: vertical-rl)
- A single small hanko-red accent mark; the rest is ink on paper
- Asymmetric, off-center compositions; ink-wash or brush texture on one image
- No boxes or shadows; only hairlines and space

## Signature ideas (pick one, use it 3+ times)

- A small red square seal (hanko) with a character as logo
- Vertical title text beside the main content
- Ink-wash gradient circle (ensO) as a hero motif

## Layouts that fit

- **asym-grid**: Asymmetric 12-col grid; hero text spans 8 cols, offset right, small note bottom-left
- **long-column**: One long narrow column with oversized numbered sections
- **poster**: Poster composition: one huge headline, tiny supporting text, big empty space

## Motion

Very slow, quiet fades (800-1200ms); nothing moves unless needed

## CSS starter

Uses the first palette (Washi) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@400;700&family=Zen+Kaku+Gothic+New:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #F3EEE3;
  --text: #2A2723;
  --accent: #B23A2E;          /* large text, borders, fills only */
  --on-accent: #F3EEE3;      /* text on accent-filled buttons */
  --secondary: #8C857A;       /* decorative / muted, never body text */
  --font-display: "Shippori Mincho", serif;
  --font-body: "Zen Kaku Gothic New", sans-serif;
  --radius: 2px;
  --border: 1px solid color-mix(in srgb, var(--text) 25%, transparent);
  --shadow: none;
  --space: clamp(1rem, 0.6rem + 1.6vw, 2rem);
}

* { box-sizing: border-box; }
html { background: var(--bg); color: var(--text); }
body { margin: 0; font-family: var(--font-body); line-height: 1.6; font-size: 1.0625rem; }
::selection { background: var(--accent); color: var(--on-accent); }

h1, h2, h3 {
  font-family: var(--font-display);
  font-weight: 400;
  text-transform: none;
  letter-spacing: 0.04em;
  line-height: 1.3;
  margin: 0 0 .4em;
}
h1 { font-size: clamp(2.75rem, 1.2rem + 7vw, 7.5rem); }
h2 { font-size: clamp(1.75rem, 1rem + 3vw, 3.5rem); }

.card {
  background: var(--bg);
  border: var(--border);
  border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: var(--space);
}

.btn {
  font: inherit; font-family: var(--font-display);
  background: var(--accent); color: var(--on-accent);
  border: var(--border); border-radius: var(--radius);
  box-shadow: var(--shadow);
  padding: .8em 1.4em; cursor: pointer;
  text-transform: none; letter-spacing: 0.04em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

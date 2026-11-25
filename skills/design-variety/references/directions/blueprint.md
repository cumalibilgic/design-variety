# blueprint

> Technical drawing: grid paper, dimensions, annotations.

**Best for:** tool, dashboard, landing, blog

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Blueprint | `#0B2A5B` | `#E6F0FF` | `#FFD84D` | `#7FB2FF` | 12.2:1 | 10.1:1 |
| Cyanotype | `#0E3B5E` | `#EAF6FF` | `#9BE7FF` | `#5AA9D6` | 10.6:1 | 8.5:1 |
| Drafting | `#EAF1F8` | `#0B2A5B` | `#C8381A` | `#5B7FA6` | 12.3:1 | 4.6:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **IBM Plex Mono** + body **IBM Plex Sans**
- display **Space Mono** + body **Space Grotesk**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `1px dashed color-mix(in srgb, var(--text) 70%, transparent)` |
| `shadow` | `none` |
| `h_case` | `uppercase` |
| `h_weight` | `400` |
| `h_tracking` | `0.06em` |
| `h_leading` | `1.15` |

## Rules (follow literally)

- Grid-paper background (two layered linear-gradients, 24px / 120px)
- Dashed outlines, dimension lines with arrows and measurements as labels
- Monospace labels like 'FIG. 3', 'REV. B', 'SCALE 1:2'
- Title block (bordered table) in a corner with project, date, version
- Single highlight color for annotations

## Signature ideas (pick one, use it 3+ times)

- A drawing title block in the bottom-right corner
- Dimension lines with arrowheads around key elements
- Registration crosshair marks at the page corners

## Layouts that fit

- **dense-table**: Data table as the hero, KPIs as a thin strip above it (not KPI cards)
- **rail-modules**: Narrow icon rail + modules of mixed sizes, each with its own header style
- **split**: Split screen: fixed left panel, scrolling right panel

## Motion

Line-draw: stroke-dashoffset animations on SVG, 600ms

## CSS starter

Uses the first palette (Blueprint) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;700&family=IBM+Plex+Sans:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #0B2A5B;
  --text: #E6F0FF;
  --accent: #FFD84D;          /* large text, borders, fills only */
  --on-accent: #0B2A5B;      /* text on accent-filled buttons */
  --secondary: #7FB2FF;       /* decorative / muted, never body text */
  --font-display: "IBM Plex Mono", monospace;
  --font-body: "IBM Plex Sans", sans-serif;
  --radius: 0;
  --border: 1px dashed color-mix(in srgb, var(--text) 70%, transparent);
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
  text-transform: uppercase;
  letter-spacing: 0.06em;
  line-height: 1.15;
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
  text-transform: uppercase; letter-spacing: 0.06em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

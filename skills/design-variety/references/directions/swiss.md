# swiss

> International Typographic Style. Grid, hierarchy, objectivity.

**Best for:** landing, dashboard, tool, portfolio

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Swiss Red | `#F5F5F0` | `#111111` | `#E10600` | `#767676` | 17.3:1 | 4.5:1 |
| White Blue | `#FFFFFF` | `#0A0A0A` | `#0047FF` | `#7A7A7A` | 19.8:1 | 6.3:1 |
| Night Swiss | `#0E0E0E` | `#F2F2F2` | `#FF4D00` | `#8A8A8A` | 17.2:1 | 5.8:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Inter Tight** + body **Inter**
- display **Hanken Grotesk** + body **Hanken Grotesk**
- display **Schibsted Grotesk** + body **Schibsted Grotesk**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `1px solid var(--text)` |
| `shadow` | `none` |
| `h_case` | `none` |
| `h_weight` | `700` |
| `h_tracking` | `-0.04em` |
| `h_leading` | `0.92` |

## Rules (follow literally)

- Strict 12-column grid; flush-left, ragged-right text; every element aligns to the grid
- One type family, only 3 sizes, with a huge jump between them
- Flat color only; the accent appears in at most one block per screen
- Thin rules and big numerals are the only ornaments
- No shadows, no radius, no decoration

## Signature ideas (pick one, use it 3+ times)

- Giant numerals (8-14rem) as section markers
- A single accent-colored block that anchors each screen
- Visible column-grid overlay toggled with the 'g' key

## Layouts that fit

- **asym-grid**: Asymmetric 12-col grid; hero text spans 8 cols, offset right, small note bottom-left
- **dense-table**: Data table as the hero, KPIs as a thin strip above it (not KPI cards)
- **split**: Split screen: fixed left panel, scrolling right panel

## Motion

None or a single 150ms opacity transition

## CSS starter

Uses the first palette (Swiss Red) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #F5F5F0;
  --text: #111111;
  --accent: #E10600;          /* large text, borders, fills only */
  --on-accent: #F5F5F0;      /* text on accent-filled buttons */
  --secondary: #767676;       /* decorative / muted, never body text */
  --font-display: "Inter Tight", sans-serif;
  --font-body: "Inter", sans-serif;
  --radius: 0;
  --border: 1px solid var(--text);
  --shadow: none;
  --space: clamp(1rem, 0.6rem + 1.6vw, 2rem);
}

* { box-sizing: border-box; }
html { background: var(--bg); color: var(--text); }
body { margin: 0; font-family: var(--font-body); line-height: 1.6; font-size: 1.0625rem; }
::selection { background: var(--accent); color: var(--on-accent); }

h1, h2, h3 {
  font-family: var(--font-display);
  font-weight: 700;
  text-transform: none;
  letter-spacing: -0.04em;
  line-height: 0.92;
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
  text-transform: none; letter-spacing: 0;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

# neo-skeuo

> Tactile, physical objects: knobs, paper, leather, metal.

**Best for:** tool, landing, dashboard, ecommerce

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Leather | `#2B2118` | `#F1E3CF` | `#D9923B` | `#5A4633` | 12.5:1 | 6.1:1 |
| Aluminum | `#E4E7EB` | `#1D2128` | `#C2410C` | `#9AA3AF` | 13.0:1 | 4.2:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Outfit** + body **Inter**
- display **Sora** + body **DM Sans**

## Tokens

| Token | Value |
|---|---|
| `radius` | `14px` |
| `border` | `1px solid rgba(0,0,0,.25)` |
| `shadow` | `inset 0 1px 0 rgba(255,255,255,.35), 0 2px 6px rgba(0,0,0,.25), 0 12px 28px rgba(0,0,0,.18)` |
| `h_case` | `none` |
| `h_weight` | `700` |
| `h_tracking` | `-0.01em` |
| `h_leading` | `1.1` |

## Rules (follow literally)

- Layered inset/outer shadows to fake real material; one light direction across the whole UI
- Real-feeling controls: toggles, dials, sliders with grooves and highlights
- Subtle noise or grain texture on large surfaces (SVG feTurbulence data-URI)
- Stitching, embossing or engraved labels for headings
- Controls have clear pressed states (inset shadow)

## Signature ideas (pick one, use it 3+ times)

- A rotary dial or slider as the main control, built from CSS
- Engraved (text-shadow highlight) section labels
- Screw heads or stitched borders on panels

## Layouts that fit

- **rail-modules**: Narrow icon rail + modules of mixed sizes, each with its own header style
- **bento**: Bento grid with deliberately unequal tiles (never a uniform card grid)
- **split**: Split screen: fixed left panel, scrolling right panel

## Motion

Physical: 120-200ms ease-out presses, slight overshoot on toggles

## CSS starter

Uses the first palette (Leather) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&family=Inter:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #2B2118;
  --text: #F1E3CF;
  --accent: #D9923B;          /* large text, borders, fills only */
  --on-accent: #2B2118;      /* text on accent-filled buttons */
  --secondary: #5A4633;       /* decorative / muted, never body text */
  --font-display: "Outfit", sans-serif;
  --font-body: "Inter", sans-serif;
  --radius: 14px;
  --border: 1px solid rgba(0,0,0,.25);
  --shadow: inset 0 1px 0 rgba(255,255,255,.35), 0 2px 6px rgba(0,0,0,.25), 0 12px 28px rgba(0,0,0,.18);
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
  letter-spacing: -0.01em;
  line-height: 1.1;
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
  text-transform: none; letter-spacing: -0.01em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

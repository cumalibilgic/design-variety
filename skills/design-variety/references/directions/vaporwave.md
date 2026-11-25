# vaporwave

> 90s-internet nostalgia: sunsets, grids, chrome and windows.

**Best for:** landing, community, game

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Miami | `#130B2B` | `#F5ECFF` | `#FF71CE` | `#01CDFE` | 16.5:1 | 7.7:1 |
| Sunset Grid | `#1A0B2E` | `#FFF1E6` | `#FFB86C` | `#FF4D9D` | 16.8:1 | 10.9:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Righteous** + body **Space Grotesk**
- display **Syncopate** + body **Inter Tight**
- display **Audiowide** + body **DM Sans**

## Tokens

| Token | Value |
|---|---|
| `radius` | `6px` |
| `border` | `2px solid var(--accent)` |
| `shadow` | `0 0 22px color-mix(in srgb, var(--accent) 40%, transparent)` |
| `h_case` | `uppercase` |
| `h_weight` | `400` |
| `h_tracking` | `0.12em` |
| `h_leading` | `1.1` |

## Rules (follow literally)

- Sun-disc with horizontal cut stripes (pink to orange, NOT purple to blue)
- Perspective grid floor made with CSS transform: perspective + repeating gradients
- Retro OS windows with title bars for content panels
- Widely tracked uppercase headings; Japanese katakana decorative text
- Keep body text on solid dark panels for legibility

## Signature ideas (pick one, use it 3+ times)

- A striped sun disc over a perspective grid in the hero
- Draggable-looking window chrome with fake minimize/close buttons
- Katakana ornament text running vertically

## Layouts that fit

- **poster**: Poster composition: one huge headline, tiny supporting text, big empty space
- **overlap**: Overlapping layers: cards that overlap the hero and each other, slight rotation
- **command-center**: Panel mosaic like a control room: mixed densities, status lights, one dominant panel

## Motion

Slow drift: grid floor scrolls endlessly, 8-12s linear

## CSS starter

Uses the first palette (Miami) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Righteous&family=Space+Grotesk:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #130B2B;
  --text: #F5ECFF;
  --accent: #FF71CE;          /* large text, borders, fills only */
  --on-accent: #130B2B;      /* text on accent-filled buttons */
  --secondary: #01CDFE;       /* decorative / muted, never body text */
  --font-display: "Righteous", sans-serif;
  --font-body: "Space Grotesk", sans-serif;
  --radius: 6px;
  --border: 2px solid var(--accent);
  --shadow: 0 0 22px color-mix(in srgb, var(--accent) 40%, transparent);
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
  letter-spacing: 0.12em;
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
  text-transform: uppercase; letter-spacing: 0.12em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

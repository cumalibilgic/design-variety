# bauhaus

> Primary shapes, strong diagonals, poster composition.

**Best for:** landing, portfolio, community, blog

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Bauhaus | `#F2EBDD` | `#111111` | `#E63A2E` | `#F2B705` | 15.9:1 | 3.5:1 |
| Primary Blue | `#F4EFE3` | `#0F1B3D` | `#1B4DB3` | `#E63A2E` | 14.7:1 | 6.6:1 |
| Black Field | `#111111` | `#F2EBDD` | `#F2B705` | `#E63A2E` | 15.9:1 | 10.4:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Jost** + body **Jost**
- display **Josefin Sans** + body **Josefin Sans**
- display **League Spartan** + body **Outfit**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `3px solid var(--text)` |
| `shadow` | `none` |
| `h_case` | `uppercase` |
| `h_weight` | `700` |
| `h_tracking` | `0.02em` |
| `h_leading` | `0.95` |

## Rules (follow literally)

- Red / yellow / blue with black and cream; flat fills only
- Circles, triangles and squares as layout anchors, large and cropped by the edge
- Rotated or vertical text; strong diagonals
- Asymmetric balance; elements bleed off the viewport
- Geometric sans only, tight leading

## Signature ideas (pick one, use it 3+ times)

- A large cropped circle + triangle composition in the hero
- Vertical rotated section labels (writing-mode: vertical-rl)
- Diagonal section dividers via clip-path

## Layouts that fit

- **poster**: Poster composition: one huge headline, tiny supporting text, big empty space
- **asym-grid**: Asymmetric 12-col grid; hero text spans 8 cols, offset right, small note bottom-left
- **overlap**: Overlapping layers: cards that overlap the hero and each other, slight rotation

## Motion

Geometric: shapes slide in on a straight line, 300ms linear/ease-out

## CSS starter

Uses the first palette (Bauhaus) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #F2EBDD;
  --text: #111111;
  --accent: #E63A2E;          /* large text, borders, fills only */
  --on-accent: #111111;      /* text on accent-filled buttons */
  --secondary: #F2B705;       /* decorative / muted, never body text */
  --font-display: "Jost", sans-serif;
  --font-body: "Jost", sans-serif;
  --radius: 0;
  --border: 3px solid var(--text);
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
  text-transform: uppercase;
  letter-spacing: 0.02em;
  line-height: 0.95;
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
  text-transform: uppercase; letter-spacing: 0.02em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

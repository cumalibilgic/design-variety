# comic-pop

> Comic book panels, halftone, speech bubbles.

**Best for:** game, community, landing, ecommerce

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Pop | `#FFF3B0` | `#111111` | `#D90429` | `#0057B8` | 16.8:1 | 4.7:1 |
| Halftone | `#FFFFFF` | `#111111` | `#E01E5A` | `#08A8A3` | 18.9:1 | 4.7:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Bangers** + body **Comic Neue**
- display **Luckiest Guy** + body **Nunito**
- display **Anton** + body **Rubik**

## Tokens

| Token | Value |
|---|---|
| `radius` | `6px` |
| `border` | `3px solid var(--text)` |
| `shadow` | `5px 5px 0 var(--text)` |
| `h_case` | `uppercase` |
| `h_weight` | `400` |
| `h_tracking` | `0.02em` |
| `h_leading` | `1.0` |

## Rules (follow literally)

- Content in comic panels with thick borders and varied sizes (CSS grid with spans)
- Halftone dot pattern (radial-gradient) as shading
- Speech/thought bubbles for tooltips and testimonials
- Action words (POW!) as decorative starbursts, used sparingly
- Headings slightly rotated and uppercase

## Signature ideas (pick one, use it 3+ times)

- Speech-bubble tooltips with a CSS tail
- Starburst badge (clip-path star) for the primary call to action
- Halftone dots fading across the hero background

## Layouts that fit

- **bento**: Bento grid with deliberately unequal tiles (never a uniform card grid)
- **overlap**: Overlapping layers: cards that overlap the hero and each other, slight rotation
- **magazine-grid**: Magazine grid: one large lead story, mixed-size secondary items, dateline strip

## Motion

Punchy: scale(1.06) with 120ms; shake on error

## CSS starter

Uses the first palette (Pop) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bangers&family=Comic+Neue:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #FFF3B0;
  --text: #111111;
  --accent: #D90429;          /* large text, borders, fills only */
  --on-accent: #FFF3B0;      /* text on accent-filled buttons */
  --secondary: #0057B8;       /* decorative / muted, never body text */
  --font-display: "Bangers", sans-serif;
  --font-body: "Comic Neue", sans-serif;
  --radius: 6px;
  --border: 3px solid var(--text);
  --shadow: 5px 5px 0 var(--text);
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
  letter-spacing: 0.02em;
  line-height: 1.0;
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

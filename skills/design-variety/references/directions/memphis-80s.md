# memphis-80s

> 80s Memphis group: confetti shapes, squiggles, loud patterns.

**Best for:** landing, community, ecommerce, game

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Memphis | `#FFF7E6` | `#1A1A1A` | `#E8206F` | `#00A896` | 16.3:1 | 4.0:1 |
| Pool | `#E6FBFF` | `#0B2545` | `#E5386A` | `#F2B705` | 14.4:1 | 3.8:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Rubik Mono One** + body **Work Sans**
- display **Bungee** + body **DM Sans**
- display **Lilita One** + body **Nunito**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `3px solid var(--text)` |
| `shadow` | `5px 5px 0 var(--secondary)` |
| `h_case` | `uppercase` |
| `h_weight` | `400` |
| `h_tracking` | `0.01em` |
| `h_leading` | `1.0` |

## Rules (follow literally)

- Scattered confetti: triangles, zigzags, dots, squiggles as absolutely positioned SVG
- Pattern fills (dots, stripes, checker) behind sections
- Clashing but limited palette; black outlines on everything
- Display type is heavy and uppercase; body plain
- Layouts are loose and crooked on purpose

## Signature ideas (pick one, use it 3+ times)

- A zigzag SVG border between sections
- Confetti shapes drifting around the hero
- Checkerboard or dotted pattern panels

## Layouts that fit

- **overlap**: Overlapping layers: cards that overlap the hero and each other, slight rotation
- **bands**: Full-bleed horizontal bands of alternating color, each with a different internal layout
- **poster**: Poster composition: one huge headline, tiny supporting text, big empty space

## Motion

Jumpy: shapes rotate or wiggle on hover, 200ms steps

## CSS starter

Uses the first palette (Memphis) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rubik+Mono+One&family=Work+Sans:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #FFF7E6;
  --text: #1A1A1A;
  --accent: #E8206F;          /* large text, borders, fills only */
  --on-accent: #FFF7E6;      /* text on accent-filled buttons */
  --secondary: #00A896;       /* decorative / muted, never body text */
  --font-display: "Rubik Mono One", monospace;
  --font-body: "Work Sans", sans-serif;
  --radius: 0;
  --border: 3px solid var(--text);
  --shadow: 5px 5px 0 var(--secondary);
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
  letter-spacing: 0.01em;
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
  text-transform: uppercase; letter-spacing: 0.01em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

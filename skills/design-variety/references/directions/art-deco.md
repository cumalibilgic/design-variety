# art-deco

> 1920s geometry: symmetry, gold lines, fans and sunbursts.

**Best for:** landing, ecommerce, portfolio

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Gatsby | `#0B1F1E` | `#F2E8CF` | `#D4AF37` | `#1E4D4A` | 14.0:1 | 8.1:1 |
| Black Gold | `#0A0A0A` | `#F3E9D2` | `#C9A227` | `#2B2B2B` | 16.4:1 | 8.2:1 |
| Champagne | `#F5EFE0` | `#1B2A2A` | `#8A6A12` | `#2E5E5A` | 13.0:1 | 4.4:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Limelight** + body **Josefin Sans**
- display **Cinzel** + body **Lato**
- display **Marcellus** + body **Jost**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `3px double var(--accent)` |
| `shadow` | `none` |
| `h_case` | `uppercase` |
| `h_weight` | `400` |
| `h_tracking` | `0.15em` |
| `h_leading` | `1.15` |

## Rules (follow literally)

- Strict symmetry; centered axes; stepped/chamfered corners
- Gold double-line frames around content; fan and sunburst motifs in SVG
- Uppercase, widely tracked display type
- Two-tone palette with metallic accent
- Ornamental dividers (diamond with lines) between sections

## Signature ideas (pick one, use it 3+ times)

- A sunburst / fan SVG behind the hero heading
- Stepped-corner frames (clip-path polygon) on cards
- Diamond-and-line divider between every section

## Layouts that fit

- **poster**: Poster composition: one huge headline, tiny supporting text, big empty space
- **bands**: Full-bleed horizontal bands of alternating color, each with a different internal layout
- **filmstrip**: Horizontal scroll-snap filmstrip for the main content

## Motion

Elegant: 600ms fade/scale from 0.98, line-draw on frames

## CSS starter

Uses the first palette (Gatsby) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Limelight&family=Josefin+Sans:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #0B1F1E;
  --text: #F2E8CF;
  --accent: #D4AF37;          /* large text, borders, fills only */
  --on-accent: #0B1F1E;      /* text on accent-filled buttons */
  --secondary: #1E4D4A;       /* decorative / muted, never body text */
  --font-display: "Limelight", serif;
  --font-body: "Josefin Sans", sans-serif;
  --radius: 0;
  --border: 3px double var(--accent);
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
  letter-spacing: 0.15em;
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
  text-transform: uppercase; letter-spacing: 0.15em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

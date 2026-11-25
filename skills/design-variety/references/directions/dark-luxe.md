# dark-luxe

> Quiet luxury. Dark, restrained, expensive.

**Best for:** landing, ecommerce, portfolio

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Midnight Gold | `#0B0B0E` | `#EDE6D6` | `#C8A45C` | `#2A2A31` | 15.8:1 | 8.3:1 |
| Bordeaux | `#14090C` | `#F0E3D8` | `#C9A27A` | `#3A1A22` | 15.5:1 | 8.3:1 |
| Emerald Noir | `#07100D` | `#E8EFE9` | `#B8A25A` | `#14332A` | 16.5:1 | 7.7:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Cormorant Garamond** + body **Montserrat**
- display **Bodoni Moda** + body **Jost**
- display **Italiana** + body **Work Sans**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `1px solid color-mix(in srgb, var(--accent) 45%, transparent)` |
| `shadow` | `none` |
| `h_case` | `none` |
| `h_weight` | `400` |
| `h_tracking` | `0.02em` |
| `h_leading` | `1.1` |

## Rules (follow literally)

- Near-black background, one muted metallic accent; never more than 2 colors on screen
- Thin serif display; small caps labels with 0.25em letter-spacing
- Very large spacing, 1px hairlines, tiny refined details
- Photography full-bleed and desaturated; no icons
- Only slow fades; no bounce, no scale pops

## Signature ideas (pick one, use it 3+ times)

- Hairline gold rules that draw in on scroll
- Letter-spaced uppercase micro-labels above every heading
- A monogram / crest as the logo mark

## Layouts that fit

- **poster**: Poster composition: one huge headline, tiny supporting text, big empty space
- **filmstrip**: Horizontal scroll-snap filmstrip for the main content
- **asym-grid**: Asymmetric 12-col grid; hero text spans 8 cols, offset right, small note bottom-left

## Motion

Slow, cinematic fades and parallax (500-800ms ease-out)

## CSS starter

Uses the first palette (Midnight Gold) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;700&family=Montserrat:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #0B0B0E;
  --text: #EDE6D6;
  --accent: #C8A45C;          /* large text, borders, fills only */
  --on-accent: #0B0B0E;      /* text on accent-filled buttons */
  --secondary: #2A2A31;       /* decorative / muted, never body text */
  --font-display: "Cormorant Garamond", serif;
  --font-body: "Montserrat", sans-serif;
  --radius: 0;
  --border: 1px solid color-mix(in srgb, var(--accent) 45%, transparent);
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
  letter-spacing: 0.02em;
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
  text-transform: none; letter-spacing: 0.02em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

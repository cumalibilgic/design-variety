# soft-organic

> Calm, natural, human. Wellness / craft feeling.

**Best for:** landing, ecommerce, blog, tool

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Clay & Sage | `#EFE6DA` | `#2B2A26` | `#B5573B` | `#7C8C6E` | 11.6:1 | 3.9:1 |
| Moss | `#E9EDE0` | `#1F2A1C` | `#4F7A2C` | `#B7C4A0` | 12.6:1 | 4.3:1 |
| Dusk Clay | `#231C19` | `#F0E4D8` | `#E08A5F` | `#4A3A32` | 13.4:1 | 6.4:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Young Serif** + body **Nunito Sans**
- display **Fraunces** + body **Figtree**
- display **Gloock** + body **Manrope**

## Tokens

| Token | Value |
|---|---|
| `radius` | `28px` |
| `border` | `none` |
| `shadow` | `0 12px 30px rgba(60,40,20,.12)` |
| `h_case` | `none` |
| `h_weight` | `700` |
| `h_tracking` | `-0.01em` |
| `h_leading` | `1.1` |

## Rules (follow literally)

- Earthy desaturated palette: clay, sage, sand, ink-brown; no pure black or white
- Large radii, blob shapes, arch-shaped image masks, grain texture
- Rounded serif headings with relaxed line-height (1.6 body)
- Hand-drawn dividers and leaf/stone illustrations in simple SVG
- Whitespace is calm, never cramped

## Signature ideas (pick one, use it 3+ times)

- Arch-shaped (border-radius: 999px 999px 0 0) image frames
- Wavy SVG section dividers between bands
- Hand-drawn underline on the key word of each heading

## Layouts that fit

- **asym-grid**: Asymmetric 12-col grid; hero text spans 8 cols, offset right, small note bottom-left
- **bands**: Full-bleed horizontal bands of alternating color, each with a different internal layout
- **long-column**: One long narrow column with oversized numbered sections

## Motion

Slow and soft: 400-600ms ease, gentle float on illustrations

## CSS starter

Uses the first palette (Clay & Sage) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Young+Serif&family=Nunito+Sans:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #EFE6DA;
  --text: #2B2A26;
  --accent: #B5573B;          /* large text, borders, fills only */
  --on-accent: #EFE6DA;      /* text on accent-filled buttons */
  --secondary: #7C8C6E;       /* decorative / muted, never body text */
  --font-display: "Young Serif", serif;
  --font-body: "Nunito Sans", sans-serif;
  --radius: 28px;
  --border: none;
  --shadow: 0 12px 30px rgba(60,40,20,.12);
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

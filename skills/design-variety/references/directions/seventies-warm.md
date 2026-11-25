# seventies-warm

> 70s warm: rounded type, earthy oranges, stripes and sunbursts.

**Best for:** landing, ecommerce, blog, community

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Harvest | `#F6E7C8` | `#3B2314` | `#C2410C` | `#E3A72F` | 12.0:1 | 4.2:1 |
| Avocado | `#EFE9CF` | `#2C2A14` | `#B4451F` | `#6B7F2A` | 11.9:1 | 4.5:1 |
| Brown Room | `#2A180F` | `#F6E7C8` | `#F2A33A` | `#C0562B` | 13.9:1 | 8.2:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Bagel Fat One** + body **DM Sans**
- display **Shrikhand** + body **Work Sans**
- display **Abril Fatface** + body **Nunito Sans**

## Tokens

| Token | Value |
|---|---|
| `radius` | `40px` |
| `border` | `none` |
| `shadow` | `none` |
| `h_case` | `none` |
| `h_weight` | `400` |
| `h_tracking` | `-0.01em` |
| `h_leading` | `1.0` |

## Rules (follow literally)

- Warm earth palette; rainbow-stripe motif in 3-4 tones (arcs or horizontal bands)
- Fat, soft display type with tight leading; pill-shaped buttons and tags
- Sunburst and concentric circle backgrounds
- Grain texture overlay, slightly faded photography
- Generous curves everywhere, no hard corners

## Signature ideas (pick one, use it 3+ times)

- Concentric stripe arcs (repeating-radial-gradient) behind the hero
- Pill tags in alternating palette colors
- Wavy stripe dividers between sections

## Layouts that fit

- **bands**: Full-bleed horizontal bands of alternating color, each with a different internal layout
- **asym-grid**: Asymmetric 12-col grid; hero text spans 8 cols, offset right, small note bottom-left
- **magazine-grid**: Magazine grid: one large lead story, mixed-size secondary items, dateline strip

## Motion

Easy and rolling: 400ms ease-in-out, gentle slides

## CSS starter

Uses the first palette (Harvest) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bagel+Fat+One&family=DM+Sans:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #F6E7C8;
  --text: #3B2314;
  --accent: #C2410C;          /* large text, borders, fills only */
  --on-accent: #F6E7C8;      /* text on accent-filled buttons */
  --secondary: #E3A72F;       /* decorative / muted, never body text */
  --font-display: "Bagel Fat One", sans-serif;
  --font-body: "DM Sans", sans-serif;
  --radius: 40px;
  --border: none;
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
  letter-spacing: -0.01em;
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
  text-transform: none; letter-spacing: -0.01em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

# paper-handmade

> Notebook, zine, cut-and-paste collage.

**Best for:** blog, landing, portfolio, community

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Notebook | `#F6F0E0` | `#23231F` | `#D9381E` | `#2F6DB5` | 13.9:1 | 4.1:1 |
| Kraft | `#D9C3A0` | `#2A1F14` | `#A3201A` | `#2E4A7D` | 9.4:1 | 4.4:1 |
| Chalkboard | `#1F2A26` | `#F2F0E6` | `#FFD54A` | `#7DD3C0` | 13.0:1 | 10.5:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Caveat** + body **Courier Prime**
- display **Permanent Marker** + body **Libre Baskerville**
- display **Reenie Beanie** + body **Special Elite**

## Tokens

| Token | Value |
|---|---|
| `radius` | `4px 12px 6px 10px` |
| `border` | `2px solid var(--text)` |
| `shadow` | `3px 4px 0 rgba(0,0,0,.22)` |
| `h_case` | `none` |
| `h_weight` | `400` |
| `h_tracking` | `0` |
| `h_leading` | `1.0` |

## Rules (follow literally)

- Paper texture background, tape strips, pins, torn edges, doodles
- Mixed typefaces like a ransom note; hand-written annotations in the margins
- Slightly crooked layouts; items rotate -3..3 degrees and overlap
- Limited ink colors; highlighter-marker strokes behind key words
- Irregular border-radius to look hand-cut

## Signature ideas (pick one, use it 3+ times)

- Tape pieces (semi-transparent rotated rectangles) holding each card
- Highlighter strokes behind key words (linear-gradient background)
- Margin doodles / arrows with handwritten notes

## Layouts that fit

- **overlap**: Overlapping layers: cards that overlap the hero and each other, slight rotation
- **long-column**: One long narrow column with oversized numbered sections
- **magazine-grid**: Magazine grid: one large lead story, mixed-size secondary items, dateline strip

## Motion

Playful: small rotations on hover, items 'peel' up 2px

## CSS starter

Uses the first palette (Notebook) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&family=Courier+Prime:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #F6F0E0;
  --text: #23231F;
  --accent: #D9381E;          /* large text, borders, fills only */
  --on-accent: #F6F0E0;      /* text on accent-filled buttons */
  --secondary: #2F6DB5;       /* decorative / muted, never body text */
  --font-display: "Caveat", sans-serif;
  --font-body: "Courier Prime", sans-serif;
  --radius: 4px 12px 6px 10px;
  --border: 2px solid var(--text);
  --shadow: 3px 4px 0 rgba(0,0,0,.22);
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
  letter-spacing: 0;
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
  text-transform: none; letter-spacing: 0;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

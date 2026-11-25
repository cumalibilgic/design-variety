# editorial

> Magazine / newspaper. Typography is the design.

**Best for:** blog, landing, portfolio, ecommerce

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Newsprint | `#F4F1EA` | `#161616` | `#D7261E` | `#8A8678` | 16.0:1 | 4.4:1 |
| Ink Night | `#121212` | `#EDE8DC` | `#E8B04B` | `#6F6A5E` | 15.3:1 | 9.6:1 |
| Cream & Forest | `#FBF7EE` | `#1B2A22` | `#2F6B4F` | `#9A8F78` | 14.0:1 | 5.9:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Fraunces** + body **Inter Tight**
- display **Playfair Display** + body **Source Sans 3**
- display **Instrument Serif** + body **Geist**
- display **DM Serif Display** + body **DM Sans**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `1px solid var(--text)` |
| `shadow` | `none` |
| `h_case` | `none` |
| `h_weight` | `700` |
| `h_tracking` | `-0.02em` |
| `h_leading` | `1.02` |

## Rules (follow literally)

- Large serif display, hairline rules (1px) between sections, never boxes
- Multi-column body text on desktop, drop caps, small-caps kickers, pull quotes
- Generous asymmetric margins; numbered sections and datelines
- Almost no color: ink, paper, one accent used sparingly for kickers and links
- Images get captions and credits like a real publication

## Signature ideas (pick one, use it 3+ times)

- A drop cap on the first paragraph of each section
- Oversized pull quotes breaking the column grid
- A dateline / issue-number strip at the top (No. 14 - Winter 2026)

## Layouts that fit

- **magazine-grid**: Magazine grid: one large lead story, mixed-size secondary items, dateline strip
- **long-column**: One long narrow column with oversized numbered sections
- **asym-grid**: Asymmetric 12-col grid; hero text spans 8 cols, offset right, small note bottom-left

## Motion

Subtle; underline reveals on links, one gentle fade on load

## CSS starter

Uses the first palette (Newsprint) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400;700&family=Inter+Tight:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #F4F1EA;
  --text: #161616;
  --accent: #D7261E;          /* large text, borders, fills only */
  --on-accent: #F4F1EA;      /* text on accent-filled buttons */
  --secondary: #8A8678;       /* decorative / muted, never body text */
  --font-display: "Fraunces", serif;
  --font-body: "Inter Tight", sans-serif;
  --radius: 0;
  --border: 1px solid var(--text);
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
  text-transform: none;
  letter-spacing: -0.02em;
  line-height: 1.02;
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
  text-transform: none; letter-spacing: -0.02em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

# newsprint

> Broadsheet newspaper: columns, rules, mastheads.

**Best for:** blog, landing, tool, community

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Broadsheet | `#E8E2D0` | `#1A1A1A` | `#B3261E` | `#6B6552` | 13.4:1 | 5.0:1 |
| Pink Paper | `#FFF1E5` | `#1A1A1A` | `#0F5499` | `#807973` | 15.7:1 | 6.9:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Old Standard TT** + body **Libre Franklin**
- display **UnifrakturCook** + body **Libre Baskerville**
- display **Abril Fatface** + body **Libre Franklin**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `1px solid var(--text)` |
| `shadow` | `none` |
| `h_case` | `none` |
| `h_weight` | `700` |
| `h_tracking` | `-0.01em` |
| `h_leading` | `1.05` |

## Rules (follow literally)

- Masthead with title, date, edition and a double rule underneath
- 3-5 column text with vertical column rules; justified text with hyphenation
- Headline hierarchy: kicker, headline, deck (subhead), byline
- Tiny type in sidebars: weather box, 'inside' index, classified-style ads
- Halftone / grayscale images with captions

## Signature ideas (pick one, use it 3+ times)

- A masthead with a blackletter or heavy-serif title and double rule
- A 'Today / Inside' index box in the sidebar
- Classified-ad-style bordered boxes for calls to action

## Layouts that fit

- **magazine-grid**: Magazine grid: one large lead story, mixed-size secondary items, dateline strip
- **index-rows**: Index/table-of-contents: full-width list rows with hover reveal instead of cards
- **long-column**: One long narrow column with oversized numbered sections

## Motion

None; at most underline on link hover

## CSS starter

Uses the first palette (Broadsheet) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Old+Standard+TT:wght@400;700&family=Libre+Franklin:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #E8E2D0;
  --text: #1A1A1A;
  --accent: #B3261E;          /* large text, borders, fills only */
  --on-accent: #E8E2D0;      /* text on accent-filled buttons */
  --secondary: #6B6552;       /* decorative / muted, never body text */
  --font-display: "Old Standard TT", serif;
  --font-body: "Libre Franklin", sans-serif;
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
  letter-spacing: -0.01em;
  line-height: 1.05;
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

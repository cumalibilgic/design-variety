# playful-geometric

> Bold shapes, stickers, toy-like energy.

**Best for:** landing, community, game, ecommerce, tool

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Sunny | `#FFF1C9` | `#1F1A3D` | `#E8431F` | `#3D5AFE` | 14.7:1 | 3.6:1 |
| Candy | `#FFE3EC` | `#2B1B3D` | `#D61F69` | `#00B8A9` | 13.2:1 | 4.1:1 |
| Night Toy | `#1B1535` | `#FFF4E0` | `#FFC93C` | `#FF5C8A` | 16.0:1 | 11.3:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Fredoka** + body **Nunito**
- display **Baloo 2** + body **Quicksand**
- display **Rubik** + body **Rubik**

## Tokens

| Token | Value |
|---|---|
| `radius` | `20px` |
| `border` | `3px solid var(--text)` |
| `shadow` | `4px 4px 0 var(--text)` |
| `h_case` | `none` |
| `h_weight` | `700` |
| `h_tracking` | `0` |
| `h_leading` | `1.05` |

## Rules (follow literally)

- Big flat color blocks; circles, pills and blobs as layout shapes
- Thick outlines and hard offset shadows, slight rotations (-2 to 3deg) on cards
- Rounded chunky display font, bouncy cubic-bezier easing
- Stickers, badges and hand-drawn squiggles as decoration
- Friendly, jokey microcopy

## Signature ideas (pick one, use it 3+ times)

- Round sticker badges rotated on corners ('New!', '100% fun')
- Squiggle SVG underline under key words
- Buttons that wobble on hover

## Layouts that fit

- **overlap**: Overlapping layers: cards that overlap the hero and each other, slight rotation
- **bands**: Full-bleed horizontal bands of alternating color, each with a different internal layout
- **bento**: Bento grid with deliberately unequal tiles (never a uniform card grid)

## Motion

Bouncy: cubic-bezier(.34,1.56,.64,1), 250-400ms

## CSS starter

Uses the first palette (Sunny) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@400;700&family=Nunito:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #FFF1C9;
  --text: #1F1A3D;
  --accent: #E8431F;          /* large text, borders, fills only */
  --on-accent: #1F1A3D;      /* text on accent-filled buttons */
  --secondary: #3D5AFE;       /* decorative / muted, never body text */
  --font-display: "Fredoka", sans-serif;
  --font-body: "Nunito", sans-serif;
  --radius: 20px;
  --border: 3px solid var(--text);
  --shadow: 4px 4px 0 var(--text);
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
  letter-spacing: 0;
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
  text-transform: none; letter-spacing: 0;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

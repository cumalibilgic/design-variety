# glass-aurora

> Atmospheric depth. Use only when it is truly the right fit.

**Best for:** landing, tool, dashboard

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Aurora | `#0A0F24` | `#EAF0FF` | `#7CF2D4` | `#8B7CFF` | 16.6:1 | 14.0:1 |
| Dusk Glass | `#140B24` | `#F4EAFF` | `#FF9ED1` | `#7C9CFF` | 16.4:1 | 10.0:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Plus Jakarta Sans** + body **Plus Jakarta Sans**
- display **Manrope** + body **Inter**

## Tokens

| Token | Value |
|---|---|
| `radius` | `24px` |
| `border` | `1px solid rgba(255,255,255,.18)` |
| `shadow` | `0 20px 60px rgba(0,0,0,.4)` |
| `h_case` | `none` |
| `h_weight` | `700` |
| `h_tracking` | `-0.02em` |
| `h_leading` | `1.08` |

## Rules (follow literally)

- Blurred color fields behind translucent frosted panels (backdrop-filter: blur(24px))
- ONE glass hero surface; everything else is quiet and solid
- Check text contrast over glass; add a tinted backing layer if needed
- Thin 1px light borders, large soft shadows
- Never purple-to-blue gradient hero; use the palette's accent fields

## Signature ideas (pick one, use it 3+ times)

- Slowly drifting blurred orbs behind the glass
- A frosted floating nav pill
- Inner 1px highlight on the top edge of every glass panel

## Layouts that fit

- **bento**: Bento grid with deliberately unequal tiles (never a uniform card grid)
- **split**: Split screen: fixed left panel, scrolling right panel
- **rail-modules**: Narrow icon rail + modules of mixed sizes, each with its own header style

## Motion

Slow ambient drift (20-40s loops) + 250ms ease interactions

## CSS starter

Uses the first palette (Aurora) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #0A0F24;
  --text: #EAF0FF;
  --accent: #7CF2D4;          /* large text, borders, fills only */
  --on-accent: #0A0F24;      /* text on accent-filled buttons */
  --secondary: #8B7CFF;       /* decorative / muted, never body text */
  --font-display: "Plus Jakarta Sans", sans-serif;
  --font-body: "Plus Jakarta Sans", sans-serif;
  --radius: 24px;
  --border: 1px solid rgba(255,255,255,.18);
  --shadow: 0 20px 60px rgba(0,0,0,.4);
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
  line-height: 1.08;
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

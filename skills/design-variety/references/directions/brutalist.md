# brutalist

> Raw, blunt, honest. Looks like a printed tool, not a startup.

**Best for:** landing, tool, portfolio, blog

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Raw Paper | `#F2F0E6` | `#111111` | `#FF3B00` | `#0038FF` | 16.5:1 | 3.1:1 |
| Hazard | `#FFE600` | `#000000` | `#D00000` | `#000000` | 16.6:1 | 4.5:1 |
| Concrete | `#D9D9D6` | `#0A0A0A` | `#E4002B` | `#0A0A0A` | 14.0:1 | 3.4:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Space Grotesk** + body **JetBrains Mono**
- display **Archivo Black** + body **IBM Plex Mono**
- display **Bricolage Grotesque** + body **Space Mono**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `3px solid var(--text)` |
| `shadow` | `6px 6px 0 var(--text)` |
| `h_case` | `uppercase` |
| `h_weight` | `700` |
| `h_tracking` | `-0.02em` |
| `h_leading` | `0.95` |

## Rules (follow literally)

- Thick 2-4px solid borders on every container; hard offset shadows only, never blur
- Zero radius everywhere; if a radius appears it is one deliberate value, used everywhere
- Headlines huge and uppercase; body in monospace; leading tight
- Expose the structure: visible grid lines, labels like [01], raw HTML-feeling links
- No gradients, no opacity tricks, no glass

## Signature ideas (pick one, use it 3+ times)

- Buttons that physically shift (translate 4px) as their shadow collapses on press
- Bracketed index numbers [01] [02] as the recurring graphic motif
- A raw marquee strip with hard borders

## Layouts that fit

- **asym-grid**: Asymmetric 12-col grid; hero text spans 8 cols, offset right, small note bottom-left
- **index-rows**: Index/table-of-contents: full-width list rows with hover reveal instead of cards
- **poster**: Poster composition: one huge headline, tiny supporting text, big empty space

## Motion

Almost none; crisp instant state changes, the press-shift is the only animation

## CSS starter

Uses the first palette (Raw Paper) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #F2F0E6;
  --text: #111111;
  --accent: #FF3B00;          /* large text, borders, fills only */
  --on-accent: #111111;      /* text on accent-filled buttons */
  --secondary: #0038FF;       /* decorative / muted, never body text */
  --font-display: "Space Grotesk", sans-serif;
  --font-body: "JetBrains Mono", monospace;
  --radius: 0;
  --border: 3px solid var(--text);
  --shadow: 6px 6px 0 var(--text);
  --space: clamp(1rem, 0.6rem + 1.6vw, 2rem);
}

* { box-sizing: border-box; }
html { background: var(--bg); color: var(--text); }
body { margin: 0; font-family: var(--font-body); line-height: 1.6; font-size: 1.0625rem; }
::selection { background: var(--accent); color: var(--on-accent); }

h1, h2, h3 {
  font-family: var(--font-display);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: -0.02em;
  line-height: 0.95;
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
  text-transform: uppercase; letter-spacing: -0.02em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

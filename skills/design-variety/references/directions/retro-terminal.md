# retro-terminal

> CRT / hacker terminal. Functional nostalgia.

**Best for:** tool, dashboard, landing, game, community

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Phosphor | `#08100B` | `#C9F7D2` | `#39FF88` | `#1B3A27` | 16.3:1 | 14.5:1 |
| Amber CRT | `#120C04` | `#FFD79A` | `#FFA21F` | `#3A2A10` | 14.3:1 | 9.7:1 |
| Cool CRT | `#060B14` | `#CFE8FF` | `#4DA3FF` | `#16304F` | 15.6:1 | 7.5:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **VT323** + body **IBM Plex Mono**
- display **JetBrains Mono** + body **JetBrains Mono**
- display **Share Tech Mono** + body **Share Tech Mono**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `1px solid var(--accent)` |
| `shadow` | `0 0 14px color-mix(in srgb, var(--accent) 40%, transparent)` |
| `h_case` | `none` |
| `h_weight` | `400` |
| `h_tracking` | `0` |
| `h_leading` | `1.1` |

## Rules (follow literally)

- Monospace everywhere; the accent is the 'phosphor' color, body text is dimmer
- Prompt-style UI: `> command`, blinking block cursor, ASCII box drawing for panels
- Glow via text-shadow, subtle scanlines via repeating-linear-gradient overlay
- Keyboard-first: visible shortcuts like [F1] Help, working focus rings
- Nothing rounded, no images unless dithered/pixelated

## Signature ideas (pick one, use it 3+ times)

- A boot-sequence line-by-line reveal on first load (skippable)
- ASCII-art logo and ASCII progress bars [#####-----]
- A status bar pinned to the bottom with clock, version and 'online' light

## Layouts that fit

- **command-center**: Panel mosaic like a control room: mixed densities, status lights, one dominant panel
- **rail-modules**: Narrow icon rail + modules of mixed sizes, each with its own header style
- **index-rows**: Index/table-of-contents: full-width list rows with hover reveal instead of cards

## Motion

Stepped: steps() easing, typewriter reveal, blinking cursor

## CSS starter

Uses the first palette (Phosphor) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=VT323&family=IBM+Plex+Mono:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #08100B;
  --text: #C9F7D2;
  --accent: #39FF88;          /* large text, borders, fills only */
  --on-accent: #08100B;      /* text on accent-filled buttons */
  --secondary: #1B3A27;       /* decorative / muted, never body text */
  --font-display: "VT323", monospace;
  --font-body: "IBM Plex Mono", monospace;
  --radius: 0;
  --border: 1px solid var(--accent);
  --shadow: 0 0 14px color-mix(in srgb, var(--accent) 40%, transparent);
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
  text-transform: none; letter-spacing: 0;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

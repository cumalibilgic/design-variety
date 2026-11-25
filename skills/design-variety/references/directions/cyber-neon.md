# cyber-neon

> Night-city HUD. Dense, glowing, technical.

**Best for:** dashboard, tool, game, landing, community

## Palettes (contrast verified)

| Name | bg | text | accent | secondary | text/bg | accent/bg |
|---|---|---|---|---|---|---|
| Neon Magenta | `#0A0614` | `#EDE7FF` | `#FF2E9A` | `#00E5FF` | 16.7:1 | 5.8:1 |
| Cyan Grid | `#050B14` | `#DDF4FF` | `#00E5FF` | `#FF2E9A` | 17.3:1 | 12.8:1 |
| Acid | `#0B0B06` | `#F3F2DC` | `#E6FF00` | `#7C3CFF` | 17.4:1 | 17.5:1 |

Accent is for large text, borders and fills (>= 3:1). Body text always uses `text`.

## Fonts (Google Fonts)

- display **Orbitron** + body **Rajdhani**
- display **Chakra Petch** + body **Space Mono**
- display **Michroma** + body **Exo 2**

## Tokens

| Token | Value |
|---|---|
| `radius` | `0` |
| `border` | `1px solid var(--accent)` |
| `shadow` | `0 0 18px color-mix(in srgb, var(--accent) 50%, transparent)` |
| `h_case` | `uppercase` |
| `h_weight` | `700` |
| `h_tracking` | `0.08em` |
| `h_leading` | `1.1` |

## Rules (follow literally)

- Dark base with 1-2 saturated neon accents; glow only on interactive or key elements
- Angular clipped corners via clip-path polygon; thin bordered panels
- Data readouts with tiny uppercase labels and tabular numbers
- Subtle grid or scanline background, never a gradient hero
- Status chips and corner brackets as ornaments

## Signature ideas (pick one, use it 3+ times)

- Corner-bracket decorations on panels ([ ])
- A live-feeling ticker with fake telemetry
- Glitch (clip + offset) effect on hover for the logo

## Layouts that fit

- **command-center**: Panel mosaic like a control room: mixed densities, status lights, one dominant panel
- **rail-modules**: Narrow icon rail + modules of mixed sizes, each with its own header style
- **bento**: Bento grid with deliberately unequal tiles (never a uniform card grid)

## Motion

Snappy 120-200ms; short glitch flicker; no easing bounce

## CSS starter

Uses the first palette (Neon Magenta) and first font pair; swap in the brief's choices.

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@400;700&display=swap" rel="stylesheet">
```

```css
:root {
  --bg: #0A0614;
  --text: #EDE7FF;
  --accent: #FF2E9A;          /* large text, borders, fills only */
  --on-accent: #0A0614;      /* text on accent-filled buttons */
  --secondary: #00E5FF;       /* decorative / muted, never body text */
  --font-display: "Orbitron", sans-serif;
  --font-body: "Rajdhani", sans-serif;
  --radius: 0;
  --border: 1px solid var(--accent);
  --shadow: 0 0 18px color-mix(in srgb, var(--accent) 50%, transparent);
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
  letter-spacing: 0.08em;
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
  text-transform: uppercase; letter-spacing: 0.08em;
}
.btn:focus-visible, a:focus-visible { outline: 3px solid var(--accent); outline-offset: 3px; }

@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
```

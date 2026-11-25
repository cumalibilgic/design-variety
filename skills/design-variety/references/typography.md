# Typography

All fonts are on Google Fonts. Load with `<link>` and `display=swap`.

## Pairings by mood

| Mood | Display | Body |
|---|---|---|
| Editorial | Fraunces, Instrument Serif, Playfair Display | Inter Tight, Source Sans 3 |
| Brutalist | Space Grotesk 700, Archivo Black, Bricolage Grotesque | JetBrains Mono, IBM Plex Mono |
| Swiss | Inter Tight 800, Hanken Grotesk | same family, lighter |
| Luxe | Cormorant Garamond, Bodoni Moda | Jost, Montserrat 300 |
| Playful | Fredoka, Baloo 2, Rubik 800 | Nunito, Quicksand |
| Technical | Chakra Petch, Orbitron, Michroma | Space Mono, Rajdhani |
| Handmade | Caveat, Permanent Marker | Courier Prime, Libre Baskerville |

## Scale

Use a ratio, not guesses. Default `clamp()` headline for impact:

```css
--step-0: clamp(1rem, 0.95rem + 0.3vw, 1.125rem);
--step-4: clamp(2.5rem, 1.5rem + 5vw, 6rem);   /* hero */
h1 { font-size: var(--step-4); line-height: 0.95; letter-spacing: -0.03em; }
```

## Rules

- Big display type is a design element: let it be 6-12rem on desktop when the direction allows.
- Tight leading on headings (0.9-1.1), relaxed on body (1.5-1.7).
- Small uppercase labels: `letter-spacing: 0.08-0.15em`, 11-13px.
- Use `font-variant-numeric: tabular-nums` for data.
- Limit to 2 families, 3-4 weights.

# Layout archetypes (CSS starting points)

## Split screen
```css
.split { display: grid; grid-template-columns: minmax(320px, 40%) 1fr; min-height: 100vh; }
.split > aside { position: sticky; top: 0; height: 100vh; }
@media (max-width: 800px) { .split { grid-template-columns: 1fr; } .split > aside { position: static; height: auto; } }
```

## Asymmetric grid
```css
.grid { display: grid; grid-template-columns: repeat(12, 1fr); gap: 1.5rem; }
.hero-text { grid-column: 2 / span 8; }
.hero-note { grid-column: 9 / span 4; align-self: end; }
```

## Bento (unequal)
```css
.bento { display: grid; grid-template-columns: repeat(6, 1fr); grid-auto-rows: 140px; gap: 1rem; }
.bento .a { grid-column: span 4; grid-row: span 3; }
.bento .b { grid-column: span 2; grid-row: span 2; }
.bento .c { grid-column: span 2; grid-row: span 1; }
.bento .d { grid-column: span 3; grid-row: span 2; }
```

## Index rows (instead of cards)
```css
.row { display: grid; grid-template-columns: 4rem 1fr auto; padding: 1.25rem 0; border-top: 1px solid currentColor; }
.row:hover { padding-left: 1rem; transition: padding .2s; }
```

## Overlap
```css
.overlap > .card { margin-top: -4rem; position: relative; z-index: 1; transform: rotate(-1.5deg); }
```

## Horizontal filmstrip
```css
.strip { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 1rem; }
.strip > * { flex: 0 0 min(80vw, 520px); scroll-snap-align: start; }
```

## Data table as hero (dashboard)
```css
.kpis { display: flex; gap: 2rem; border-bottom: 1px solid currentColor; padding: .75rem 0; font-variant-numeric: tabular-nums; }
table { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; }
th { text-align: left; position: sticky; top: 0; background: var(--bg); }
td, th { padding: .55rem .75rem; border-bottom: 1px solid color-mix(in srgb, var(--text) 20%, transparent); }
tr:hover td { background: color-mix(in srgb, var(--accent) 12%, transparent); }
```

## Icon rail + mixed modules
```css
.app { display: grid; grid-template-columns: 64px 1fr; min-height: 100vh; }
.rail { display: flex; flex-direction: column; gap: 1rem; padding: 1rem 0; align-items: center; border-right: var(--border); }
.modules { display: grid; grid-template-columns: repeat(12, 1fr); gap: 1rem; padding: 1rem; }
.modules .wide { grid-column: span 8; } .modules .narrow { grid-column: span 4; } .modules .full { grid-column: 1 / -1; }
```

## Control-room panel mosaic
```css
.mosaic { display: grid; grid-template-columns: 2fr 1fr 1fr; grid-template-rows: 2fr 1fr; gap: 8px; height: 100vh; padding: 8px; }
.mosaic .main { grid-row: span 2; }
.panel { border: var(--border); padding: .75rem; position: relative; }
.panel::before { content: attr(data-label); position: absolute; top: -.7em; left: .75rem; background: var(--bg); padding: 0 .4rem; font-size: .7rem; letter-spacing: .12em; text-transform: uppercase; }
```

## Magazine grid
```css
.mag { display: grid; grid-template-columns: repeat(6, 1fr); gap: 1.5rem; }
.mag .lead { grid-column: span 4; grid-row: span 2; } .mag .side { grid-column: span 2; } .mag .wide { grid-column: span 3; }
.mag article + article { border-top: 1px solid currentColor; padding-top: 1rem; }
```

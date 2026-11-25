---
name: design-variety
description: Use when building any website, web app, landing page, dashboard or UI, to avoid the generic "AI look". Picks a random but coherent design direction (palette, fonts, layout, signature detail) before any code is written, so every project looks different.
---

# Design Variety

Left alone, Claude converges on the same design every time: centered hero, purple-blue gradient, Inter, three identical cards, rounded-2xl everything. This skill breaks that habit by **choosing a design brief before writing any code**, and choosing it with randomness instead of taste.

## Workflow (follow in order)

1. **Name the product type** in one word: `landing`, `dashboard`, `portfolio`, `ecommerce`, `tool`, `blog`, `game`, `community`.
2. **Generate a brief.** From the skill folder run:
   ```bash
   python3 scripts/seed.py --type landing --remember
   ```
   - `--type` limits to directions that suit the product (a dashboard never gets a poster layout).
   - `--remember` avoids the last 5 directions used across projects.
   - Optional: `--dark` / `--light`, `--direction <name>`, `--seed N`, `--json`, `--list`.
   - If the user already named a style or gave brand colors/fonts, use theirs instead and skip the random pick. Still do steps 3-6 with their constraints.
3. **Read the direction file** printed at the end of the brief (`references/directions/<name>.md`). It holds the palette table, tokens, rules, signature ideas and a ready CSS starter.
4. **Commit to the brief as tokens.** Put palette, fonts and tokens into CSS variables first (`--bg --text --accent --on-accent --secondary --font-display --font-body --radius --border --shadow`). Everything else derives from these. Load the fonts with the printed Google Fonts URL.
5. **Follow the direction rules literally** (borders, radii, type behaviour, textures). They are concrete on purpose. Build the chosen layout and put the signature element in at least 3 places so it reads as intentional.
6. **Run the checklist** below before finishing.

If the brief clashes with the product (neon cyber for a funeral home), rerun with another seed or `--direction`. Never silently fall back to defaults. If you must bend the brief (accessibility, content, user request), say what you changed and why.

## Rules for every direction

- **Typography first.** Distinctive display font plus quiet body font, loaded from Google Fonts. Never ship with only Inter/Roboto/Arial/system-ui.
- **Hierarchy through contrast**: at least one 3x size jump between headline and body.
- **Palette discipline**: use `text` for body copy. `accent` is for large text, borders and fills (verified >= 3:1); text on accent-filled buttons uses `on_accent`. `secondary` is decorative only.
- **Break the card grid.** At most one uniform row of cards per page; prefer asymmetry, bento, list rows, overlap.
- **Real content.** No lorem ipsum, no "Feature 1". Write specific, on-brand copy.
- **Details**: styled focus states, `::selection`, favicon, empty and error states in the same visual language.
- **Accessibility is not optional**: contrast, visible focus, `prefers-reduced-motion`, tap targets >= 44px.
- **Responsive**: design the 375px layout deliberately, don't just stack.

## Final checklist

- [ ] Could this be mistaken for a generic SaaS template? If yes, push the direction harder.
- [ ] Two distinct font families loaded AND applied?
- [ ] Palette defined once as variables, no stray hardcoded colors?
- [ ] Signature element appears 3+ times?
- [ ] None of the forbidden defaults from the brief are present?
- [ ] Focus states and reduced-motion handled?
- [ ] Looks intentional at 375px and 1440px?

## References

- `references/directions/INDEX.md` - all 20 directions with themes and best-fit product types
- `references/directions/<name>.md` - mini design system per direction (generated from `scripts/data.py`)
- `references/anti-patterns.md` - AI-look tells and what to do instead
- `references/typography.md` - pairings, scale, rules
- `references/layouts.md` - layout archetypes with CSS starting points

## Extending

Add a direction in `scripts/data.py`, then run `python3 scripts/build_docs.py` and `python3 -m unittest discover -s tests` from the repo root. Tests enforce palette contrast (text >= 7:1, accent >= 3:1) and that generated docs are in sync.

# Design systems

## Inspect first

Look for existing tokens, CSS variables, theme providers, utility classes, component libraries, typography, icon conventions, and documentation. Extend before replacing.

## Color system

For a new project, propose a palette justified by brand, theme, audience, and functional needs. Include when relevant:
- Brand colors: primary, secondary, accent.
- Neutral scale: backgrounds, surfaces, borders, text.
- Semantic colors: success, warning, danger, info.
- Interactive states (hover, focus, selected, disabled, error).
- Data/chart and category colors.
- Light and dark variants when required.

Define semantic tokens rather than scattering hex values through code:

```css
:root {
  /* Brand */
  --color-brand-500: #6366f1;
  --color-brand-600: #4f46e5;

  /* Surfaces */
  --color-bg: #ffffff;
  --color-surface: #f8fafc;

  /* Text */
  --color-text: #0f172a;
  --color-text-muted: #475569;
  --color-border: #cbd5e1;

  /* Semantic */
  --color-success: #15803d;
  --color-warning: #a16207;
  --color-danger: #b91c1c;
  --color-info: #0369a1;
  --color-focus: #4f46e5;
}
```

This is a structural example only; do not reuse these values automatically in every project.

Color rules:
- Verify contrast against WCAG 2.2 at the level relevant to the project: at least 4.5:1 for normal text and 3:1 for large text.
- Also check graphical components and meaningful indicators when WCAG criteria apply.
- Never claim contrast compliance without calculating or verifying it.
- Do not convey information through color alone.
- Provide coherent hover, focus, selected, disabled, and error states.
- Avoid arbitrary palettes, excessive accents, and ambiguous semantic colors.
- For dark themes, rework colors for legibility and hierarchy; do not simply invert.

## Typography and layout

Define a reusable system with:
- Font families and fallback stacks.
- A coherent type scale with sizes, weights, line heights, and letter spacing.
- Styles for headings, paragraphs, labels, helper text, and data text.
- Reading widths suited to the content, with wrap and overflow rules.
- Grid, containers, columns, gutters, and margins.
- Spacing scale and density rules.
- Radii, borders, shadows, and elevation levels.
- Composition and responsive hierarchy principles.

Concrete starting points (adapt, do not apply blindly):
- Body line height 1.4–1.6 unitless; large headings 1.1–1.25.
- Measure of 60–75 characters per line for body copy, e.g. `max-width: 68ch`.
- Fluid type with `clamp()` including a `rem` term so browser zoom still works: `font-size: clamp(2rem, 1.5rem + 2.5vw, 3rem)`.
- Size text in `rem`/`em` so user font settings are respected.
- Left-align body text; avoid justified text on the web.
- Load web fonts as WOFF2 with `font-display: swap` (or `optional`) and preload the critical face; subset when the project supports it.

Prefer coherent, adaptive scales. Use relative units, `rem`, `clamp()`, CSS Grid, and Flexbox when relevant. Do not choose the same font or grid for every project.

## Tokens

When useful, establish tokens for:
- Color roles (surface, text, border, primary, accent, status).
- Typography (families, sizes, weights, line heights, letter spacing).
- Spacing scale and layout widths.
- Radii, borders, elevation, and shadows.
- Motion duration/easing and reduced-motion behavior.
- Breakpoints based on layout needs.
- Focus rings and interactive state treatment.

Prefer semantic tokens such as `--color-text-muted` over one-off values scattered across components. Ensure color combinations meet relevant contrast expectations.

## Components

Define variants and states intentionally. Avoid component APIs with too many boolean props or duplicated one-off components. Document unusual design decisions. Reuse components when behavior and semantics are genuinely shared, not merely because two blocks look similar.

## Themes

Support light/dark or brand themes only when requested or justified. Check contrast and state visibility independently in every theme.

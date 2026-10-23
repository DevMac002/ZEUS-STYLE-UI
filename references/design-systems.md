# Design systems

## Inspect first

Look for existing tokens, CSS variables, theme providers, utility classes, component libraries, typography, icon conventions, and documentation. Extend before replacing.

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

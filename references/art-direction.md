# Art direction workflow

## Purpose and scope

For a new or substantially redesigned website or app, settle the visual intent before building the main components. The process should produce a coherent, theme-specific result without adding ceremony to a small, constrained change. For a focused component task, make only the design decisions needed for that component.

Follow the user's current brief, brand, audience, and technical constraints first. The personal profile in [Esteve visual signature](reference-profiles/esteve-visual-signature.md) is a starting point when the project has room for a visual direction; adapt it to the theme. An established client or product identity takes precedence. Ember Grid is an optional alternate direction for fitting technical work.

## 1. Understand the project

Establish what is available about:
- Product or site type, audience, their needs, and context of use.
- Primary goal and action; key journeys, pages, and content.
- Brand personality, existing design system, supplied assets, and visual references.
- Platform, stack, existing architecture, performance, responsive, accessibility, and delivery constraints.

Inspect the existing project before selecting libraries or proposing structural changes. Ask only for missing information that could materially change the design or architecture. If the brief and references are sufficient, proceed with stated assumptions; do not block on secondary preferences.

When the user supplies screenshots or URLs, describe visible traits separately from inference. Use them as inspiration and do not assume permission to copy their layout, words, or assets.

## 2. Explore directions

For a new, open-ended brief, consider several genuinely different approaches internally before choosing. Use these as flexible lenses, not a mandatory menu:
- **Editorial minimalism:** open space, controlled palette, expressive type, strong images, precise hierarchy.
- **Immersive and cinematic:** large visuals, depth, scene transitions, scroll-led narrative, and motion where it serves the story.
- **Creative experimentation:** unusual grids, expressive typography, vivid contrast, organic forms, or novel interactions while keeping the task understandable.
- **Purpose-led modes:** product-focused commerce, functional dashboards, digital brutalism, luxury editorial, or technical minimalism when the subject calls for them.

Combine compatible influences with a clear reason. Do not add visual effects just to make a direction seem distinctive.

Choose the strongest fitting direction and explain its thesis briefly. Recommend one direction by default; present alternatives only when the user requests them or comparing them would materially help the decision. Preserve approval gates for consequential decisions when the user has not already settled them.

## 3. Select and test the direction against the brief

Consider:
- **Relevance:** does the style suit the activity, audience, and goal?
- **Identity:** does it feel specific and recognizable?
- **Clarity:** can people read, scan, and find the important actions?
- **Experience:** does it improve navigation and interaction?
- **Feasibility:** can the stack, assets, devices, and performance budget support it?
- **Coherence:** do color, type, images, shapes, and motion belong together?

Prefer the direction with the best overall fit, not the greatest number of effects. A quiet composition can be more memorable than a busy one.

## 4. Define a concise visual signature

Before implementing the main layout, establish a compact art-direction sheet. Use [templates/design-plan.md](../templates/design-plan.md) for larger or ambiguous work; keep it brief for smaller work.

Specify:
- **Palette:** roles for background, surfaces, text, borders, primary and semantic accents. Derive hues from the brief and brand; never repeat a default palette mechanically.
- **Typography:** families, weights, scale, line height, tracking, and headline treatment; keep readability and language coverage.
- **Composition:** container widths, grid, alignment, whitespace, density, and responsive changes. Avoid repeating the same centered sections and uniform card rows by habit.
- **Surfaces and imagery:** shape, radius, borders, shadows, layering, texture, and image treatment; use only effects that support the selected world.
- **Mood:** light, dark, editorial, luxurious, organic, technical, experimental, or an intentional blend.
- **Signature moments:** choose one to three distinctive visual or interactive moments, grounded in the subject.
- **Anti-patterns:** name the colors, patterns, effects, or layouts that would weaken this specific direction.

## 5. Design the interaction and movement

For a substantial scroll-based experience, sketch the page's progression before implementation. For each important section, note its content and role, initial focal point, scroll response, what moves or stays fixed, transition to the next section, and where movement settles so people can read or interact.

Select only techniques that serve the content:
- Reveals, parallax, scroll-linked transformations, pinned sections, or horizontal galleries when they improve storytelling or product exploration.
- Image masks, crop changes, or typographic reveals when they strengthen hierarchy.
- Short feedback for hover, selection, clicks, state changes, and navigation.
- 3D or camera-like movement only when the product benefits enough to justify its cost.

Adapt movement to the product: commerce needs useful product selection, gallery, variant, and price updates; portfolios can use expressive transitions; dashboards need fast state feedback; editorial pages should support reading. Do not use every technique in one project.

Keep durations and easing coherent. Keep the page responsive to input; do not trap or obstruct scrolling. Respect keyboard interaction and prefers-reduced-motion; remove or simplify nonessential movement while preserving content and state feedback.

## 6. Build a coherent design system

Turn the chosen signature into reusable semantic tokens for colors, type, spacing, sizing, shapes, depth, motion, and breakpoints as appropriate. Build only the components the product needs. Reuse existing components and architecture where practical; do not make every section identical or add a library if the current stack can do the work.

For mobile and platform-specific apps, translate visual intent into native layout and controls rather than shrinking a desktop composition.

## 7. Implement, inspect, and refine

Implement real content and interactions in the detected stack. Inspect in a browser or device-sized view when those tools are available. Check that:
- The result reflects the chosen direction and has a clear hierarchy.
- Images, whitespace, and section rhythm support the content.
- Responsive layouts, forms, controls, and existing behaviors work.
- Keyboard access, focus, reduced motion, readable contrast, and performance receive appropriate review.
- Motion begins and ends intentionally and adds a perceptible benefit.

Fix relevant issues within scope. Report what was actually inspected or run, and what could not be verified. Never claim to have tested a browser or device if no such check was performed.

## Decision sequence

Understand the project → explore directions → select and justify one → define the visual signature → plan meaningful interaction and movement → build the design system → implement → inspect and refine.

Scale the depth to the work. The goal is a distinctive, coherent, responsive, accessible, and feasible interface whose art direction fits its subject.

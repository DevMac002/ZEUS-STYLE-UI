# Frontend engineering

## Stack detection

Inspect project manifests, lockfiles, config files, source extensions, routing, and existing code. Detect framework, language, package manager, styling system, testing tools, and component conventions. Do not introduce a new stack when an existing one is established.

## Implementation rules

- Preserve existing architecture and unrelated behavior.
- Use semantic HTML, meaningful component names, clear boundaries, and project-native patterns.
- Prefer native browser capabilities over dependencies when they are sufficient. Modern CSS often removes the need for JS or libraries: `@container` queries for component-level responsiveness, `:has()` for parent/state styling, `@layer` for predictable cascade order, `:is()`/`:where()` for selector reuse, `clamp()` for fluid type and spacing.
- Avoid duplicated styles, magic numbers, unnecessary abstractions, and premature generalization.
- Keep state local unless sharing is needed.
- Make controls functional and keyboard accessible.
- Use appropriate loading and error handling for asynchronous content.
- Handle long text, missing images, empty collections, and unexpected data.
- Do not fabricate API endpoints, credentials, analytics, or backend behavior.
- Keep changes small enough to review; explain broad refactors before making them.
- Do not modify lockfiles or package manifests except when a justified dependency or script change is needed.
- Use existing lint, formatting, type-check, build, and test commands where available.

## Performance targets (web)

When measuring web performance, the Core Web Vitals "good" thresholds (web.dev, 75th percentile) are:
- LCP ≤ 2500 ms.
- INP ≤ 200 ms.
- CLS ≤ 0.1.

Also relevant: responsive images with defined dimensions, modern formats, lazy loading below the fold, `font-display: swap` (or optional) with preloading of critical fonts, minimal JavaScript, and reduced third-party weight. Report measured values only when actually measured; otherwise state checks as not run.

# Quality assurance

## Verification ladder

Use the strongest available checks in this order:
1. Static review and project-native lint/type checks.
2. Unit, integration, component, or end-to-end tests relevant to the change.
3. Build or production compilation.
4. Browser runtime and console checks.
5. Visual review at narrow, medium, and wide viewports.
6. Screenshot comparison against approved direction or supplied reference, if available.
7. Accessibility tooling plus manual keyboard and focus review.

The actual order may vary with project setup and task scope.

## Checklist

### Visual consistency
- Clear hierarchy and readable typography.
- Consistent spacing, colors, borders, and component variants.
- No arbitrary one-off styles that conflict with tokens.
- Images have appropriate crops, sizes, and fallback behavior.
- Empty/loading/error/success states are designed when relevant.

### Responsive
- No unintended horizontal scrolling or clipped content.
- Navigation and controls work at narrow widths.
- Text and layout reflow naturally.
- Touch and keyboard use remain practical.

### Accessibility
- Semantics, labels, focus, contrast, keyboard operation, and reduced motion reviewed.
- Automated scans are supplemented by manual review when possible.

### Performance
- Avoid unnecessary dependencies and large assets.
- Use responsive image sizing and appropriate formats when possible.
- Avoid expensive effects and needless client-side work.
- Use project-native performance tooling if available.

### Tests and engineering
- Run relevant tests, lint, type checks, and build commands when available.
- Check console/runtime errors when a browser is available.
- Confirm unrelated tests/features were not knowingly broken.
- Do not claim a command passed unless it ran and returned a successful result.

### SEO (contextual)
For public indexable pages, check meaningful titles/descriptions, semantic headings, descriptive links, image alternatives, canonical/indexing behavior where relevant, and structured data only when justified. For authenticated/internal applications, prioritize app metadata and share previews where relevant rather than forcing public SEO requirements.

## Report format

List:
- Check performed.
- Result: pass, fail, partial, or not run.
- Evidence or short explanation.
- Known limitation and next action.

Never turn an unperformed check into a pass.

# Accessibility

Aim for WCAG 2.2 AA where applicable, while being honest that automated checks alone cannot establish conformance.

## WCAG 2.2 AA additions to check

WCAG 2.2 (W3C Recommendation, October 2023) adds criteria beyond 2.1; include them in reviews:
- **2.4.11 Focus Not Obscured (Minimum):** the focused component must not be entirely hidden by sticky headers, footers, or other author content.
- **2.5.7 Dragging Movements:** any drag-based functionality needs a single-pointer alternative (e.g. up/down buttons to reorder).
- **2.5.8 Target Size (Minimum):** pointer targets are at least 24×24 CSS pixels, unless an exception applies (spacing, inline, equivalent control, essential).
- **3.2.6 Consistent Help:** help mechanisms appear in the same relative order across pages.
- **3.3.7 Redundant Entry:** information already entered in the same process is not required again (unless essential).
- **3.3.8 Accessible Authentication (Minimum):** authentication does not rely on cognitive function tests (puzzles, transcription) unless an alternative exists.

## Touch target numbers

- WCAG 2.2 AA minimum: 24×24 CSS px (2.5.8); WCAG 2.1 AAA enhanced: 44×44 CSS px (2.5.5).
- Material Design: 48×48 dp touch targets, ≥8 dp apart.
- Apple HIG: 44×44 pt minimum.
- Prefer the platform guideline when it is stricter than the WCAG minimum.

## Checklist

Check:
- Semantic landmarks, heading order, and meaningful page titles.
- Keyboard operation for all interactive functionality.
- Visible focus indicators, logical focus order, and focus not obscured.
- Accessible names, labels, instructions, and error messages.
- Contrast for text and meaningful UI elements.
- Text resizing, zoom, reflow, and content not hidden by fixed elements.
- Alternative text appropriate to the purpose of images; decorative images should not create noise.
- Reduced-motion preferences and avoidance of flashing content.
- Touch target size and spacing, especially on mobile (numbers above).
- Non-drag alternatives for drag interactions.
- Dialog focus management and escape/close behavior where relevant.
- Status updates for dynamic content when necessary.

Prefer native buttons, links, inputs, and select elements over custom controls. Do not use color as the only way to convey state. Test with keyboard and available automated tools; report limitations.

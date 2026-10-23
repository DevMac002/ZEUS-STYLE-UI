# Accessibility

Aim for WCAG 2.2 AA where applicable, while being honest that automated checks alone cannot establish conformance.

Check:
- Semantic landmarks, heading order, and meaningful page titles.
- Keyboard operation for all interactive functionality.
- Visible focus indicators and logical focus order.
- Accessible names, labels, instructions, and error messages.
- Contrast for text and meaningful UI elements.
- Text resizing, zoom, reflow, and content not hidden by fixed elements.
- Alternative text appropriate to the purpose of images; decorative images should not create noise.
- Reduced-motion preferences and avoidance of flashing content.
- Touch target size and spacing, especially on mobile.
- Dialog focus management and escape/close behavior where relevant.
- Status updates for dynamic content when necessary.

Prefer native buttons, links, inputs, and select elements over custom controls. Do not use color as the only way to convey state. Test with keyboard and available automated tools; report limitations.

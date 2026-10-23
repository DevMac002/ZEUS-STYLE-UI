# Design craft

Opinionated rules for making a page or screen look designed rather than generated. Read after the brief is understood and before proposing concepts. `art-direction.md` says *how to choose*; this file says *what to do*.

## 1. Start from the subject, not from a style

Before any visual decision, write three lines:
- **Subject:** the concrete thing (a parish youth app, a freight-tracking dashboard, a ceramics shop), not the category.
- **Job:** what the person must be able to do in the first 10 seconds.
- **World:** 5 materials, objects, textures or vocabulary from the subject's real world (e.g. paper, wax seal, stained-glass geometry; or pallets, manifests, stencil type).

Every distinctive choice (shape language, palette, imagery, type mood) must trace back to one of these. If a choice traces to nothing, it is a default: change it or justify it.

## 2. Domain → starting direction

Starting points to adapt, never templates. Pick the closest row, then push it away from that domain's cliché.

| Domain | Lean toward | Avoid |
|---|---|---|
| Community, faith, nonprofit | Warm humanist type, real photography of real people, calm contrast, generous tap targets, readable by all ages | Stock hands-and-sunset photos, heavy gold-on-navy "church template" look, tiny light-gray text |
| Fintech, health, legal | Trust through clarity: high contrast, plain labels, restrained color, data legible at a glance | Neon gradients, playful illustration on error or money screens |
| Editorial, culture, portfolio | Type as the main image, asymmetric grid, varied measure, one bold crop | Card grids, uniform thumbnails |
| E-commerce | Product imagery leads; consistent crops; price and action unmistakable; fast scanning | Decorative sections between product and cart |
| SaaS, dashboards, internal tools | Density with order: tables, filters, keyboard paths, quiet chrome, one accent | Marketing-style hero inside the app, oversized cards for tabular data |
| Kids, education | Large type, chunky shapes, clear feedback, color-coded but never color-only | Dense paragraphs, small targets |
| Mobile-first, low-bandwidth markets | System or subsetted fonts, few images, vector shapes, light motion, designed loading and offline states | Hero video, several web-font families, layout that waits on images |

## 3. Typography

Type carries personality. Spend the most design effort here.

- **Pairing logic:** one family is often enough (use weight and size for contrast). With two, make them structurally different: serif + grotesque, or humanist + mono for data. Never two similar sans.
- **Mood → candidates** (Google Fonts; check license and script coverage):
  - Warm, humane: Fraunces, Newsreader, Literata, Source Serif 4, Figtree, Hanken Grotesk
  - Precise, technical: IBM Plex Sans + Plex Mono, Schibsted Grotesk, Archivo
  - Expressive display: Bricolage Grotesque, Gloock, Young Serif, Instrument Serif, Syne
  - Plain, highly legible: Atkinson Hyperlegible, Public Sans, Lexend
  - Non-Latin or heavily accented text: verify coverage first (Noto families when needed)
- **Do not default** to Inter, Roboto, Arial, Space Grotesk or Playfair Display unless the brief or brand requires them.
- **Scale:** pick one ratio and keep it: 1.125 (dense UI), 1.2–1.25 (apps, marketing), 1.333–1.5 (editorial, display-led). Define 6–8 steps as tokens. Skip steps rather than adding off-scale sizes.
- **Measure and rhythm:** body 45–75 characters per line (`max-width: 62ch` as a start). Line height about 1.5 for sans body, 1.55–1.65 for serif, 1.05–1.2 for large headings. Tighten tracking slightly on large display type; open it slightly on small labels.
- **Hierarchy with few tools:** size, weight and color give three levels. Use at most three weights per page.
- **Display type is a design element:** set it large, break lines on meaning, align it to the grid. If the headline is the hero, let it be.
- **Fluid sizes:** `clamp()` with a `rem` term so browser zoom still works.
- **Performance:** at most two families, WOFF2, `font-display: swap`, subset, preload the one critical face, and define a fallback stack close in metrics.

## 4. Color

- **Build palettes from the world list, not from a mood word.** Take colors from the subject's materials, then tune.
- **Structure (4–6 named values):** a base neutral family tinted toward the brand hue (not pure gray), a surface step, one voice color, one action color, plus semantic success/warning/danger. Name tokens by role.
- **Proportion:** roughly 60% base, 30% secondary surfaces and text, under 10% accent. An accent used everywhere stops being an accent.
- **Pure black on pure white is harsh;** a tinted near-black on a slightly warm or cool base reads as intentional. Do not hard-code the same near-black on every project.
- **Contrast is computed, not eyeballed:** run `scripts/contrast.py`. Body text 4.5:1, large text and UI boundaries 3:1. Check every theme and state, including text on images and on the accent color.
- **Dark mode is a separate design:** lift surfaces in steps, desaturate accents slightly, avoid pure black with pure white text.
- **Never color alone:** pair with icon, label, weight or position.

## 5. Layout and composition

- **Pick one structural idea** and carry it through: a strong left axis, a 12-column grid with deliberate asymmetry, a single centered column, a modular dashboard grid. State it in one sentence.
- **Spacing:** one base unit (4 or 8) and a scale of multiples. Space between groups must exceed space within groups; proximity does most of the grouping work and borders are the last resort.
- **Hero options (choose deliberately):** headline-led, product- or image-led, live demo, interactive moment, or no hero (utility pages start with the task). A big number plus gradient accent is the default; use it only if nothing in the subject is more characteristic.
- **Vary section rhythm.** Alternate dense and airy, wide and narrow, text-led and image-led. Identical stacked sections read as a template.
- **Cards are earned:** use a card only for a self-contained, clickable or comparable unit. Otherwise use spacing, rules or alignment.
- **Alignment:** commit. Left-align body text. Center only short, symmetric moments (one statement, a form title).
- **Density:** match the task. Scanning (tables, lists) wants tighter rows; reading and decisions want air.
- **Mobile is a composition, not a squeeze:** reorder content by priority, keep the primary action within thumb reach, targets at least 44px (48dp on Android).

## 6. Shape, depth, imagery

- **One shape language:** choose the radius logic (sharp, soft, pill) and apply it by hierarchy, not one radius everywhere. Nested corners: inner radius = outer radius minus padding.
- **Depth:** choose borders *or* shadow *or* tonal layers as the main device. One soft gray shadow on everything is a tell.
- **Imagery:** real, specific, cropped with intent. With no assets, build typographic, geometric or illustrative systems from the world list instead of empty gray boxes. Give photos one crop, one color grade, one aspect ratio. Check licenses.
- **Icons:** one family, one stroke weight, labeled when meaning is not obvious.

## 7. Motion

- Default to almost none. Choose **one orchestrated moment** (a load sequence, one reveal) and make it good.
- Motion that answers a user action (open, expand, confirm, reorder) is welcome and should show what changed. Roughly 150–250 ms for small feedback, 300–500 ms for larger transitions, ease-out on entry.
- Do not animate every section on scroll or lift every card on hover.
- Respect `prefers-reduced-motion` with a real alternative, not just a disabled effect.

## 8. Words are design

- Name things in user language. Buttons state the result ("Save changes", not "Submit"); one action keeps one name across flow, toast and confirmation.
- Errors say what happened and what to do next, without apology. Empty states invite the next action.
- Write real copy for the real subject. If placeholders are unavoidable, keep them realistic in length and tone so layout problems stay visible.

## 9. Spend boldness in one place

Choose the one memorable element (type treatment, image, color field, interaction). Keep everything else quiet and disciplined. Before delivering, remove one accessory.

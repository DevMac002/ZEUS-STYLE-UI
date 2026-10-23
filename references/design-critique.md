# Design critique

Run this before building (on the plan) and again before delivering (on the result). Fix what fails, then say what changed and why. Never claim a visual check you did not perform; if you cannot render the page, say the visual pass was reasoned from code only.

## A. Plan review (before code)

Compare the plan against the brief. Imagine the same brief given to another designer: would they land on the same palette, fonts and layout? If yes, that part is a default. Revise it.

Check that:
- Every major choice traces to the subject, job or world list (see `craft.md` §1).
- Type, palette and layout each contain one decision that is specific to this project.
- The plan names the single memorable element and what stays quiet around it.

## B. Tells of a generated page

Each one is acceptable when the brief calls for it. Treat them as defaults to question, not rules to obey blindly.

- Cream background with high-contrast serif and a terracotta accent; or near-black with one acid accent.
- Identical rounded cards, one radius everywhere, the same soft shadow under each, gradient washes as decoration.
- Tracked-out ALL-CAPS eyebrow above every heading; one word in a headline italicized or colored for emphasis.
- Numbered markers (01 / 02 / 03) on content that is not a sequence.
- Meta lines joined with middle dots, labels shaped "WORD — fragment", arrows appended to every link.
- Fade-and-slide-up on every section; hover lift on every card.
- Stock-style hero: big number, small label, gradient glow.
- Empty gray image boxes or lorem ipsum hiding layout problems.
- The same section order on every project: hero, three features, testimonials, pricing, footer.

## C. Result review (before delivery)

1. **Squint test.** Blur or shrink the view mentally or with a screenshot: is there one clear focal point, then a clear second? If everything has equal weight, hierarchy failed.
2. **Grayscale test.** Remove color: does hierarchy and state still read?
3. **Content stress.** Try the longest title, a missing image, an empty list, a very long word, 200% text size.
4. **Viewport sweep.** Narrow (about 360px), medium (about 768px), wide (about 1440px). Layout should be recomposed, not just scaled.
5. **State sweep.** Default, hover, focus, active, disabled, loading, empty, error, success where applicable.
6. **Consistency.** Same spacing steps, radii, type steps and icon style across screens; no off-scale values.
7. **Remove one accessory.** Delete the decorative element whose absence nobody would miss.

## D. Scorecard

Score each 0 (fails), 1 (acceptable), 2 (strong). Report it briefly with one line of evidence per dimension. Anything at 0 must be fixed before delivery; anything at 1 gets a note.

| Dimension | Question |
|---|---|
| Concept | Does the design clearly belong to this subject? |
| Hierarchy | Is the first and second thing to see obvious? |
| Typography | Is type deliberate, readable and consistent? |
| Color | Is the palette purposeful, proportioned and contrast-checked? |
| Layout | Is there one structural idea, with varied rhythm? |
| Detail | Are states, spacing, alignment and shapes coherent? |
| Restraint | Is boldness concentrated in one place? |
| Usability | Can the main task be done fast, on touch and keyboard? |

Do not average the scores into a single number; the lowest dimension matters most.

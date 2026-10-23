# Reference profile — Ember Grid

**Status:** active house direction
**Source:** supplied Pinterest pin `https://pin.it/6U385hiZ6` (canonical: `https://it.pinterest.com/pin/43136108928305399/`), a screenshot of Gcore's "Inference at the Edge" landing page. Judge the screenshot, not the current Gcore site; the live page may differ.
**Use for:** AI infrastructure, edge/cloud, developer tools, data platforms, security, and technical B2B products. Adapt it for adjacent subjects when the brand and audience allow.
**Not:** a template, a license to reuse Gcore trademarks, copy, or assets, or a reason to ignore the brief.

## Visual thesis

A dark control plane lit by a single ember light. The page should feel calm, expensive, and technical — not "AI neon". One warm accent does the work; everything else is near-black, warm off-white, and thin light.

The reference works because it is restrained:

- One dominant light source, not a rainbow of gradients.
- One signature visual (the network constellation), not a collage of effects.
- One accent color, used for emphasis and state, not for decoration everywhere.
- Strong type and negative space carry the composition; the glow only supports them.

## What the reference actually shows

Observed from the supplied screenshot:

- Near-black canvas with a warm orange flare entering from the upper right and a softer ember wash near the lower edge.
- Thin, translucent top navigation: small mark at left, compact links in the center, login and a solid orange CTA at right.
- Centered hero: a small pill badge, a short two-line headline in a tight grotesque, two lines of muted supporting copy, and two CTAs (solid orange primary, ghost secondary).
- A network/constellation hero visual: a central circular glass hub, five to seven satellite nodes, thin connection lines, and small traveling light pulses. The diagram explains the product (edge inference / distributed compute), so it is not arbitrary decoration.
- Dark glass surfaces with 1px light borders, modest 12–16px radii, and a faint top-edge highlight. No heavy drop shadows.
- Small uppercase or mono labels for technical texture; body copy stays quiet and readable.
- Generous vertical spacing; the page breathes instead of filling every row with cards.
- The palette is warm, not blue-violet: black, bone white, warm gray, ember orange.

## Tokens

### Color

| Role | Hex | Notes |
|---|---|---|
| Canvas | `#070708` | Page background, near-black but not pure black |
| Base | `#0B0B0D` | Sections, nav, solid surfaces |
| Surface | `#111114` | Panels, cards |
| Elevated | `#17171B` | Hovered panels, popovers |
| Line | `rgba(255,255,255,0.08)` | Default 1px border; raise to 0.14 for hover |
| Text | `#F4F1EC` | Warm off-white, not `#FFFFFF` |
| Muted | `#A7A29B` | Secondary copy, labels |
| Ember | `#FF5A1F` | Primary accent, active state, key line |
| Ember hot | `#FF8A3D` | Glow, focus ring, highlighted text |
| Ember deep | `#B8320B` | Pressed state, deep gradient stop |
| Success | `#4ADE80` | Use sparingly; not part of the house palette |
| Warning | `#FBBF24` | Use sparingly; not part of the house palette |
| Danger | `#F87171` | Use sparingly; not part of the house palette |

Contrast checks (computed with `scripts/contrast.py`):

- `#F4F1EC` on `#070708`: 17.87:1 — pass.
- `#A7A29B` on `#070708`: 7.94:1 — pass.
- `#FF5A1F` on `#070708`: 6.46:1 — pass for text and UI.
- `#0B0B0D` on `#FF5A1F`: 6.31:1 — pass for normal text. Use dark text on the orange button.
- `#FFFFFF` on `#FF5A1F`: 3.12:1 — fails for normal text. If white text is required, use `#C2410C` (5.18:1) or `#B8320B` (6.00:1) as the button background.
- `#FF8A3D` on `#070708`: 8.59:1 — pass; good for focus rings and small accents.

### Type

- **Display:** Schibsted Grotesk (OFL) or Instrument Sans. Use a tight, slightly technical grotesque. Do not default to Inter when a more distinctive open alternative fits.
- **Body:** Instrument Sans, Figtree, or the project's existing sans. One body family is enough.
- **Mono:** IBM Plex Mono for eyebrow labels, metrics, version tags, and small technical annotations.
- **Display scale:** `clamp(3.25rem, 7vw, 6.5rem)`, line-height `0.95`, letter-spacing `-0.04em`, weight 600–700.
- **Section heading:** `clamp(2rem, 4vw, 3.5rem)`, line-height `1.05`, letter-spacing `-0.03em`.
- **Body:** `1rem`, line-height `1.6`, max measure `65ch`.
- **Label:** `0.75rem`, uppercase, letter-spacing `0.12em`, mono, muted or ember.
- **Rule:** two families plus mono at most. Do not mix three display voices.

### Shape and spacing

- Base spacing unit: `8px`; use a 4/8/12/16/24/32/48/64/96/128 scale.
- Page max width: `1200px`; gutters `clamp(20px, 4vw, 48px)`.
- Radii: `10px` for buttons and inputs, `14–16px` for panels, `999px` for badges only. Do not make every surface a pill.
- Borders: 1px, low-opacity white. Add a subtle inner top highlight instead of a heavy shadow.
- Shadows: large, soft, low-opacity black only for floating layers; no glowing boxes around every card.
- Grid: 12 columns, `24px` gap. Break the grid only when the content justifies it.

### Background

Use a near-black base and at most two warm radial washes:

```css
background:
  radial-gradient(900px 600px at 72% -8%, rgba(255, 90, 31, 0.30), transparent 60%),
  radial-gradient(700px 500px at 18% 110%, rgba(184, 50, 11, 0.16), transparent 60%),
  #070708;
```

Add optional grain at 2–3% opacity and a soft vignette. Do not stack purple, blue, cyan, and orange gradients. If the glow is removed, the layout must still read.

## Layout

### Navigation

- Height 64–72px; full-width with a max-width inner shell.
- Transparent at the top; switch to `rgba(7,7,8,0.72)` with `backdrop-filter: blur(16px)` and a 1px bottom border after scroll.
- Left: compact mark plus wordmark. Center: 4–6 short links. Right: login or secondary link, then one solid ember CTA.
- Link size 13px; muted by default, text color on hover/active. Focus ring visible.

### Hero

- Centered composition, max-width 820–900px.
- Top padding 120–160px on desktop, 72–96px on mobile.
- Eyebrow pill: mono uppercase, 1px border, small ember dot or label. Keep it factual ("Edge inference", "Now in beta"), not vague.
- H1: two lines maximum on desktop; do not force a line break that breaks at 320px.
- Subcopy: two lines maximum, 56–64ch, muted.
- CTA row: primary solid ember, secondary ghost; 12px gap; stack on narrow screens.
- One trust row maximum (logos, a metric, or a short proof line). Do not add three competing proof strips.

### Signature visual

Use a network/constellation diagram only when it explains the product's topology, distribution, or intelligence model:

- Central hub: 120–160px circle, glass surface, 1px border, soft ember rim.
- Satellites: 5–7 nodes, 48–64px, 1.5px monochrome icons; ember only on the active node.
- Connections: 1px lines at 25–45% ember opacity; one traveling pulse per line, not a constant strobe.
- Depth: two or three blur layers behind the diagram, not twenty floating particles.
- If the product is not networked or distributed, replace the diagram with a real product view, a map, a timeline, or a data visualization. Do not use a fake network because it looks "AI".

### Sections

- Vertical rhythm: 96–160px between major sections.
- Alternate dense and airy sections; do not repeat the same three-card row down the page.
- Use panels only to group related information. A panel must earn its border by improving scanability.
- Feature sections: one strong claim, one concrete explanation, one visual. Avoid icon + heading + paragraph repeated six times without variation.

## Components

### Primary button

```css
background: #FF5A1F;
color: #0B0B0D;
border: 1px solid rgba(255, 255, 255, 0.08);
border-radius: 10px;
padding: 12px 20px;
font-weight: 600;
```

Hover: raise the ember to `#FF6A2E` and lift 1px. Active: `#B8320B`. Focus: 2px `#FF8A3D` ring with 2px offset. Do not rely on glow alone.

### Ghost button

Transparent background, `1px solid rgba(255,255,255,0.16)`, text `#F4F1EC`, same radius and padding. Hover: border `0.28` opacity and background `rgba(255,255,255,0.04)`.

### Panel

```css
background: linear-gradient(180deg, rgba(255,255,255,0.045), rgba(255,255,255,0.015));
border: 1px solid rgba(255,255,255,0.08);
border-radius: 16px;
box-shadow: inset 0 1px 0 rgba(255,255,255,0.06);
```

No 40px blurred colored shadow. No glass panel on top of another glass panel.

### Badge

Mono, 11–12px, uppercase, `1px solid rgba(255,255,255,0.12)`, `border-radius: 999px`, padding `6px 10px`, muted text, optional ember dot. One badge per hero.

### Navigation link

13px, weight 500, muted; hover to text; active gets a 1px underline or a small ember dot. Do not make every link a pill.

## Motion

- One orchestrated page load: background wash fades in, H1 and copy rise 8–12px, network lines draw, nodes stagger in. Total 600–900ms; stagger 60–90ms.
- Ambient network pulse: 6–10s cycle, low amplitude. Node drift: ±4px over 8–12s. Do not animate every element at once.
- Hover: 120–180ms ease-out; buttons lift 1px; nodes increase rim light; panels raise border opacity. No bounce, no scale above 1.02.
- Scroll: reveal sections once, 12–16px rise, 400–600ms. Do not replay on every scroll direction.
- Reduced motion: remove ambient pulses, line drawing, drift, and scroll reveals. Keep static diagram and instant state changes. Respect `prefers-reduced-motion`.

## Copy

- Short, declarative, concrete. Name the thing, the place, and the benefit.
- Good tone: "Inference at the edge. Run models close to users. Ship in minutes."
- Avoid "unleash", "revolutionize", "supercharge", "next-gen", "seamless", "game-changing" unless the claim is literal and proven.
- No invented metrics, customer logos, certifications, or benchmarks. If a number is used, give its source or label it as illustrative.
- Technical texture comes from specificity, not jargon density.

## Accessibility

- Body text at least 4.5:1; large text at least 3:1; UI boundaries and focus indicators at least 3:1.
- Orange primary button: use `#0B0B0D` text at `#FF5A1F`, or darken the orange for white text.
- Focus ring: 2px `#FF8A3D`, 2px offset, visible on both near-black and ember surfaces. Never remove focus styles.
- Do not use ember alone to signal status; pair it with text, an icon, or a shape change.
- Decorative network diagrams: `aria-hidden="true"`. Informative diagrams: provide a text summary and accessible labels for nodes.
- Glow must never sit directly behind small text without a scrim; keep copy on a solid or sufficiently opaque surface.
- Check at 320px, 768px, 1024px, and 1440px. The hero must not overflow or clip.
- Honor reduced motion, zoom to 200%, and keyboard-only navigation.

## Do

- Use one accent color and one signature visual.
- Keep the canvas warm near-black, not pure black.
- Use warm off-white text, thin borders, and generous negative space.
- Make the network diagram explain something real.
- Write specific technical copy.
- Let the type and composition carry the page when the glow is removed.

## Do not

- Use purple/blue "AI" gradients, robot heads, brains, or sparkle icons.
- Stack six glass cards or put a glow on every element.
- Use pure `#000000` and `#FFFFFF` as the whole palette.
- Copy Gcore's logo, layout, copy, or assets one-to-one.
- Use white text on `#FF5A1F` for normal-size text.
- Add a fake terminal window, fake metrics, or fake customer logos.
- Use glassmorphism as a substitute for hierarchy.
- Apply the direction to a brand whose identity, audience, or accessibility needs clearly conflict with it.

## Adaptation rules

- **Adjacent technical products:** keep the near-black canvas, single accent, tight display type, and thin borders; change the accent only if the brand requires it.
- **Fintech, health, legal, or public-sector products:** keep the calm structure and strong hierarchy, but reduce the cinematic glow and use the brand's palette. Do not force ember.
- **Light brands:** invert the surfaces to warm paper and ink, keep one ember accent and the same type discipline. The direction is a set of relationships, not a fixed dark theme.
- **Content-heavy products:** keep the grid, typography, and surface treatment; drop the network hero and use real product UI or data.
- **Existing brand system:** preserve the brand. Use Ember Grid only for layout, type scale, spacing, and restraint, not for replacing established colors.

## Acceptance checklist

- [ ] One accent color; no second decorative hue.
- [ ] H1 remains readable at 320px with no overflow.
- [ ] Primary CTA text meets 4.5:1 contrast.
- [ ] Focus ring is visible on canvas and on ember.
- [ ] Network diagram is decorative or has a text alternative.
- [ ] Reduced motion removes ambient animation.
- [ ] Layout still works with the glow removed.
- [ ] No Gcore trademarks, copy, or assets are reproduced.
- [ ] The direction fits the subject; deviations are deliberate and documented.

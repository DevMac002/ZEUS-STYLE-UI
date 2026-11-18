# Scroll cinematography, depth and scroll-coupled physics

Field-tested guidance from a motion-led brand site (canned juice, Abidjan, 2026). Read it with [creative-frontier.md](creative-frontier.md) when a website should feel like a film the visitor directs by scrolling: product launches, drink and food brands, events, portfolios. Skip it for utilities, dashboards and dense apps.

## 1. Pick the motion style from the subject

Start from the sector, then keep one style (two at most) for the whole site. Durations and easings are starting points.

| Style | Typical subjects | Rhythm | Signature moves | Palette and type |
|---|---|---|---|---|
| Cinematic luxury | hotels, fine dining, real estate, lounges | slow, 1.0–1.6 s, `power3.out` / `expo.out` | slow zoom-out hero, line-by-line masked titles, curtain image reveals, light parallax | deep neutrals + one metal accent, refined serif + thin sans |
| Vibrant energy | events, youth churches, music, sport, drinks | fast, 0.4–0.7 s, `back.out(1.6)` / `power4.out` | kinetic type, crossing marquees, pinned horizontal track, countdown | saturated, high contrast, heavy condensed or rounded display |
| Precise tech | startups, fintech, SaaS, apps | 0.3–0.6 s, `power2.out` | bento reveals, 3D tilt + pointer glow cards, counters, pinned phone mock-up | dark base + one luminous accent, geometric sans |
| Human warmth | NGOs, churches, health, education | soft, 0.8–1.0 s | gentle fades of real people, impact counters, scroll timeline | warm earth tones, rounded sans + serif quotes |
| Editorial bold | portfolios, agencies, fashion, photographers | mixed | giant type, word-by-word scrub text, cursor-following previews, masked image openings | black/white + one accent, expressive grotesque |
| Fluid commerce | shops, delivery, product brands | 0.25–0.5 s | product hover swap, bouncing add-to-cart, floating hero product, sticky mobile CTA | brand-led |

Choose 3–5 signature moments (hero, one pinned scene, a transition, the final CTA). Everything else gets a sober reveal.

## 2. Camera grammar on scroll

Treat each pinned section as a shot. The scroll is the camera operator. Name the shot before coding it.

| Shot | What the visitor sees | Implementation hint (GSAP + ScrollTrigger, `scrub: 1`) |
|---|---|---|
| Extreme close-up → pull back | Opens on the product label filling the screen, then reveals the full scene | `set(el,{scale:2.7, y:'-12vh'})` then `to(el,{scale:1, y:0})` in a pinned timeline |
| Rack focus | Secondary objects go from blurred to sharp as they arrive | `from(items,{scale:.3, filter:'blur(14px)', autoAlpha:0, stagger:.04})` |
| Dive / push-in | The camera enters a detail (logo, flower on the label) that becomes the next scene | set `transformOrigin` on the detail's coordinates (measure them on the image), scale to ~11, cross-fade to the detail's own visual |
| Iris transition | A circle opens from the previous scene into the next | `clipPath: 'circle(0% at 50% 50%)' → 'circle(80% …)'`, or scrub the next section's own clip-path as it enters |
| Orbit / dolly-in | Product slides in from the side and rotates into place while copy assembles | `from(art,{x:±25vw, scale:1.35})` + `from(product,{rotate:±25, yPercent:30})` + staggered copy with blur |
| Travelling with motion blur | Horizontal pinned track whose cards skew with scroll speed | `quickTo(track,'skewX')` fed by `clamp(-8,8, self.getVelocity()/-250)`; images inside zoom via `containerAnimation` |
| Ken Burns wide shot | Full-bleed image slowly zooms out while text lights up word by word | image `scale:1.6 → 1`, words `opacity:.1 → 1` with stagger, pinned |
| Zoom-out on a number | A giant figure shrinks into place, then supporting stats arrive | `from(mega,{scale:4, filter:'blur(6px)'})` |
| Crane tilt | A product shot tips toward the viewer | parent `perspective:1200px`, image `rotateX:55 → 0`, `transformOrigin:'50% 100%'` |
| End credits | Letterbox bars close, products drop in, "FIN" | bars `height:0 → 11vh`, products `bounce.out` |

Extras that sell the camera feeling: a pointer-driven parallax on hero objects (desktop only), a marquee whose speed follows scroll velocity, a gradient progress bar.

Do not add a fake camera HUD (REC dot, timecode, viewfinder corners) unless the user asks: it reads as gimmick and competes with content. Camera *movement* is the effect, not camera *chrome*.

On mobile keep the hero and the one key scene pinned; turn horizontal tracks into vertical stacks and unpin long sections.

## 3. Depth through colour, not flat fills

- Replace flat section backgrounds with 2–3 layer radial gradients that stay inside the brand's colour families (for a bissap/pineapple brand: raspberry → plum, cream → gold → mango).
- Add 3–6 large blurred colour orbs per section (`filter: blur(50px)`, radial gradient to transparent) and give each a different scroll parallax speed. Different speeds = perceived depth. Put them in an `isolation: isolate` section with `z-index:-1`, so they never cover text.
- A very light SVG-noise grain over the whole page (`opacity ≈ .07`, `mix-blend-mode: overlay`) removes the plastic look of large gradients.
- Use gradient text on one or two display titles, glassy cards (`backdrop-filter`, translucent border) on dark scenes, and a multi-colour progress bar.
- Keep text plainly readable: verify contrast on the darkest and lightest point of a gradient behind body copy.

## 4. Scroll-coupled physics: the pour scene

Pattern: a product is tilted by the scroll and its contents pour, hit the ground, splash and land on the "screen", then run down it.

Layers (inside one pinned section):
1. Background and floor line (`FL ≈ 84%` of the height).
2. `canvas#cv` for stream and puddles, with an SVG goo filter (`feGaussianBlur stdDeviation 7` + `feColorMatrix … 0 0 0 24 -10`) so particles merge into liquid.
3. The product image, rotated by GSAP around `transformOrigin: '50% 80%'`.
4. `canvas#scr` on top (`pointer-events:none`) as the "glass": stains, drops, ripples and highlights, plus an offscreen trail canvas that fades slowly (`destination-out` with alpha ≈ .003 per frame).

Make it 100 % scroll-driven, not time-driven:
```js
// in the pinned ScrollTrigger
onUpdate: s => { velT = Math.max(velT, Math.min(Math.abs(s.getVelocity()) / 900, 1.6)); go(); }
// each frame
velT *= .9; vel += (velT - vel) * .4; if (vel < .03) vel = 0;
const tilt = clamp(0, 1, (Math.abs(rotationDeg) - 70) / 35);
emit(Math.min(tilt * vel, 1.2) * (isSmall ? 6 : 10));   // nothing comes out when the visitor stops scrolling
```
Compute the mouth from the element's layout box plus GSAP `x`, `y`, `rotation` around the same transform origin; the stream velocity follows the can's axis.

Physics: gravity ≈ .38 px/frame²; on floor impact add volume to that liquid's puddle (`rx = 30 + sqrt(volume) * 5`, flat ellipse), spawn 2–4 small splash particles upward, sometimes a ripple ring, and with a probability scaled by scroll speed a screen splat.

Screen splat: grows for ~6 frames, then is painted onto the trail canvas as an irregular blob (smoothed noisy polygon), elongated satellite droplets, a curved white highlight, then 1–3 drops start below it. Drops stick for a random time, slide with accelerating speed, wobble slightly, shrink, leave a trail, and sometimes pause again. Draw drops as teardrops, not circles: circles plus small dark dots read as faces.

Add interaction: on desktop, hovering wipes the glass (radial `destination-out`); a click or tap splashes at that point. Show a one-line hint after the first splat.

Several liquids: give each source its own colour set, puddle, stain and drip colours; the goo filter merges them where they meet.

Performance and safety: cap particles (≈ 400 mobile / 800 desktop), clamp DPR to 1.5, run the rAF loop only while the scene is active or particles remain, clear on re-entry, fade the glass quickly when leaving. Under `prefers-reduced-motion` skip the simulation and keep the still product and copy.

## 5. Product imagery without photos: honest 3D renders

When a client has no photography and the brief needs realism, render the product in 3D rather than drawing it flat. Present the result as 3D renders, never as photos, and keep brands fictional unless the client provides theirs.

Pipeline that worked (Blender `bpy` from pip, Cycles on CPU, ≈ 20 s per 720×1280 can at 48–64 samples):
1. Design the label as HTML at the cylinder's unwrapped ratio (2π r : label height, e.g. 2400×1146 px) and screenshot it with a headless browser. Put the front face at 50 % width, legal text, nutrition table and barcode on the back.
2. Build the can by lathing a profile (rim, neck, body, base) into a mesh, smooth shading, plus a tab and rivet.
3. Map the label with object coordinates in the shader: `u = atan2(y, x) / 2π + .5`, `v = (z - z0) / (z1 - z0)`, mask outside `0..1` to brushed aluminium (metallic 1, roughness .2).
4. Condensation: a few hundred flattened spheres with a water material (transmission 1, IOR 1.33), concentrated on the camera-facing side, plus a faint noise bump on the label.
5. Studio light: large key softbox, two tall rim strips, one thin front strip for the vertical highlight, low top fill; a dim warm world so the metal has something to reflect.
6. Colour management: `Standard` view with exposure around −0.75 kept brand colours saturated; AgX washed them out on bright scenes.
7. Shadow catcher planes for grouped scenes, transparent film, export PNG → WebP (q ≈ 82) and crop transparent margins.

Fruit, flowers and glasses are possible procedurally (petals from a polar grid with a colour ramp and radial "vein" noise, fruit slices from a cylinder with radial fibres, glasses by lathe with a translucent liquid) but read more stylised than the product. Say so.

## 6. Pitfalls already paid for

- GSAP and the CSS `translate` property: animating `yPercent` on an element centred with `translate: -50% -50%` replaces the centring. Animate `y` in `vh`/px instead, or centre with GSAP `xPercent/yPercent` only.
- `<img width height>` with only `width: 100%` in CSS stretches the image; always add `height: auto`.
- A CDN that the test browser cannot reach silently disables every animation. In headless checks, route the CDN URLs to local copies of the same versions.
- Velocity-driven effects only appear with real wheel input in tests (`mouse.wheel` in small steps); `scrollTo` gives zero velocity.
- When several triggers share a section, find the pinned one (`t.pin`) before reading `start`.
- Measure transform origins on the actual image (e.g. the flower sits at 44 % of the can render's height), not by guess.

## 7. Delivery checklist for this kind of site

- One style, 3–5 signature shots, each with cause → behaviour → visible result.
- The primary CTA is visible without scrolling and repeated at the end; sticky WhatsApp/call button on mobile in West African markets.
- Animate only `transform`, `opacity`, `clip-path` and filters on small elements; hero text and image stay visible if JS fails (initial hidden states set by JS).
- Lazy-load everything below the hero; total motion JS ≈ under 120 kB gzip.
- Desktop 1440 px and mobile 375–390 px captured across the whole scroll before delivery; report only what was captured.
- `prefers-reduced-motion`: no smooth scroll, no scrub, no simulation; simple fades.

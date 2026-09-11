# Teschev

Finished static Russian-language product landing page. Authored source and deployable files live in `dist/`; no application dependencies or build step.

## Preview

`python -m http.server 5173 --bind 127.0.0.1 --directory dist`

## Verified product and offer

Type 2, up to 3.5 kW, 220 V single phase, 8/10/13/16 A, LCD, delayed start, approximately 3.5 m cable. Price supplied by seller: **350 BYN**. No fabricated reviews, ratings, discounts, delivery estimates, IP rating or specific protections. Bag shown in supplied photography is explicitly not confirmed as included.

## Before sales launch

- Replace contact, delivery, warranty, seller and privacy placeholders in `dist/index.html` and `dist/app.js`.
- Forms are deliberately **not connected**, as requested. They validate fields and show an honest not-sent state. No contact information is persisted locally or sent externally.
- When a lead receiver is provided, configure `leadEndpoint` in `dist/config.js`. It must accept JSON via HTTPS (or `/api/` same-origin), validate and durably save the lead, and return `{ "ok": true }` only after receipt. Add rate limiting, abuse protection, retention policy and seller-approved privacy content at integration time. Success is shown only on a successful confirmed response.
- Telegram remains disconnected. No invented contact links are emitted.
- Update canonical, Open Graph URL, sitemap, robots and schema origin when adding a custom domain. The current deployment is private for owner review.

## Validation

`python finalize_site.py` updates the Product/Offer and FAQ schema from the visible FAQ. `python validate_site.py` checks image sizing/alt, local resources, anchors, unique IDs, one H1, prices and JSON-LD. `node --check dist/app.js` checks script syntax.

The September 11 revision was checked in Chromium at 360, 390, 768, 1024 and 1440 px with no horizontal overflow. Current selection, form opening, FAQ, video pause/resume and offscreen pause passed. Reduced motion keeps the poster without requesting video. No Lighthouse scores have been claimed.

The latest September 11 revision removes all video from the page and uses a static display photograph with four parameter rows. The current selector's photo remains hidden below 768 px. New supplied photographs illustrate connection, the quiet charging section and compatibility. The connection photograph extends to the right viewport edge; the four headline specifications are centered. Compatibility uses a large photograph on the left, copy on the right and brand examples underneath. FAQ shares the specifications' full-width heading and two-column desktop structure; both become one column on mobile.

Removed the hero eyebrow, hero trust line and bottom caption, scenario carousel, delayed-start promotional note, old product-film control, repeated dark offer block, current-photo caption and kit section. Delayed start remains in the confirmed specifications and FAQ. Price remains 350 BYN and lead submission remains disconnected. Latest layout and interactions checked in an isolated Chromium context at 360, 390, 768, 1024, 1440 and 1920 CSS pixels.

Optional WebMCP tools share the visible current selector and form opener, without submitting data. No supported WebMCP validation context was available; these optional registrations have not been runtime-verified.

## Assets

Only supplied product photography and one supplied product video are used. Responsive WebP derivatives are in `dist/assets`. Manrope is licensed under SIL Open Font License; see `dist/assets/OFL.txt`. Sources are referenced by `prepare_assets.py`; they are not required to serve the site.

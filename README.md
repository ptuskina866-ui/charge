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

No Lighthouse scores or browser QA have been claimed. Responsive breakpoints cover 360, 390, 768, 1024 and large desktop widths. Reduced motion, keyboard-friendly native dialogs and accordions, reserved image sizes, local variable font and a lazy user-initiated muted video are implemented.

Optional WebMCP tools share the visible current selector and form opener, without submitting data. No supported WebMCP validation context was available; these optional registrations have not been runtime-verified.

## Assets

Only supplied product photography and one supplied product video are used. Responsive WebP derivatives are in `dist/assets`. Manrope is licensed under SIL Open Font License; see `dist/assets/OFL.txt`. Sources are referenced by `prepare_assets.py`; they are not required to serve the site.

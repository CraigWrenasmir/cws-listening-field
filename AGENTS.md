# CWS / First Studies

This is Craig Warren Smith's piano library, developed with Maple. Preserve the approved Listening Field design and the source music.

- Read `data/STYLE.md` before composing or engraving. Straight piano, two hands, sweet melancholy, warm isolation, gentle impressionist flow and independent voices. Velvet Estuary is the primary reference.
- Every composition needs a two-word title, the next CWS opus number and a documented musical ancestor. Compose complete pieces deliberately; do not fill the catalogue with arbitrary note permutations.
- Maximum four printable pages and the provisional ceiling of 256 sounded pitch onsets. Count each chord pitch and repeated attack; exclude tied continuations.
- Retain CWS / FIRST STUDIES, title, opus and conventional musical markings. No subtitles, dedication line or prose playing instructions on the score. Preserve numeric composition stamps across revisions.
- Preserve existing recordings unless a musical/audio change is requested. New recordings use the warm-room settings in `data/library_style.json`.
- Explicit bar definitions are in `scripts/compose.py`, `scripts/new_pieces.py` and `scripts/dream_pieces.py`. Select opus numbers when running the music pipeline so an addition does not regenerate approved earlier pieces.
- Run the relevant music validation and render/inspect every changed PDF page. `scripts/prepare_library.py` packages the gallery and downloads after those checks.
- Run `npm run check`, `npm test` and `npm run build` for website changes. The UI tests use a DOM harness with simulated audio; do not describe them as browser or acoustic listening tests.
- Work and QA output belongs in ignored `work/`; never commit virtual environments, sample banks, credentials or local machine paths.
- Keep the museum-like presentation, freely rotatable sculptures, complete audio, readable notation, musical-family navigation and text index. Respect reduced motion and keep keyboard alternatives to dragging.
- The collection playlist follows the editorial order in `src/app.js`. Include every catalogue work once, and review the listening order when adding compositions. Keep pause, skip, score synchronisation, error recovery and the final stop intact.
- The primary public gallery is GitHub Pages at https://craigwrenasmir.github.io/cws-listening-field/. Pages publishes the root of `main` automatically after pushes. Preserve `.nojekyll` and relative asset URLs. Run the checks before pushing; verify the Pages build and public assets afterwards. The earlier Sites deployment recorded in `.openai/hosting.json` is a separate copy, not the requested primary host; do not redirect publishing back to Sites. The intended eventual custom address is a subdomain of wrenasmir.com; its specific subdomain and DNS are not configured.

For the continuing Op. 7–300 commission, read and update `data/PROGRESS.md` after every completed piece. Preserve sleep/resume checkpoints, and distinguish completed checks, public deployment and Craig's listening approval.

# Hosting the Listening Field

The primary public gallery is [GitHub Pages](https://craigwrenasmir.github.io/cws-listening-field/), published directly from this repository.

Repository Settings → Pages uses **Deploy from a branch**, **main**, **/ (root)**. The gallery is already static at the repository root; `.nojekyll` tells Pages to serve it without Jekyll processing. No custom workflow, API key or hosting account is required.

For updates, run `npm run check`, `npm test` and `npm run build`, then push the validated source and music assets to `main`. GitHub Pages automatically publishes that revision. Wait for the repository's Pages build to succeed and verify the public gallery, recordings and score downloads. The `dist/` directory remains an optional portable build for other static hosts; GitHub Pages serves the root source files directly.

All asset URLs are relative, so the same build can run at a domain root, a GitHub Pages project path or the selected `wrenasmir.com` subdomain. Each work has a fragment address such as `#cws-op-004-tidal-orchard`; no server rewrite rule is needed for those links.

The host should serve `.json` as JSON, `.svg` as SVG, `.pdf` as PDF and `.mp3` as MPEG audio. HTTP range requests are useful for seeking within recordings. No server runtime, database, secret or environment variable is needed for playback.

An earlier copy remains on Sites at https://cws-listening-field.wrenasmir.chatgpt.site. `.openai/hosting.json` preserves that copy's project binding. It is separate from the primary GitHub Pages deployment and does not update when GitHub changes. Future publishing should target GitHub Pages unless Craig requests otherwise.

No custom domain or DNS changes are configured. The eventual `wrenasmir.com` subdomain can be connected to GitHub Pages later.

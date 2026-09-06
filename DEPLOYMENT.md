# Hosting the Listening Field

The deployable site is static. Build it with `npm ci && npm run build`, then upload the contents of `dist/` to the chosen host. `index.html` belongs at that host's document root.

All asset URLs are relative, so the same build can run at a domain root, a GitHub Pages project path or the selected `wrenasmir.com` subdomain. Each work has a fragment address such as `#cws-op-004-tidal-orchard`; no server rewrite rule is needed for those links.

The host should serve `.json` as JSON, `.svg` as SVG, `.pdf` as PDF and `.mp3` as MPEG audio. HTTP range requests are useful for seeking within recordings. No server runtime, database, secret or environment variable is needed for playback.

The GitHub repository is public. Website deployment and subdomain/DNS configuration remain a separate step. No custom domain, GitHub Pages configuration or publishing workflow is enabled by this initial push.

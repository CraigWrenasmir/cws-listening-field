# Hosting the Listening Field

The deployable site is static. Build it with `npm ci && npm run build`, then upload the contents of `dist/` to the chosen host. `index.html` belongs at that host's document root.

All asset URLs are relative, so the same build can run at a domain root, a GitHub Pages project path or the selected `wrenasmir.com` subdomain. Each work has a fragment address such as `#cws-op-004-tidal-orchard`; no server rewrite rule is needed for those links.

The host should serve `.json` as JSON, `.svg` as SVG, `.pdf` as PDF and `.mp3` as MPEG audio. HTTP range requests are useful for seeking within recordings. No server runtime, database, secret or environment variable is needed for playback.

The public gallery is hosted with Sites at https://cws-listening-field.wrenasmir.chatgpt.site. The public GitHub repository remains the source of record. The same committed source is pushed to the site's deployment repository before packaging and publishing. `.openai/hosting.json` binds this checkout to its existing Site and declares `dist/` as static output; reuse that project when updating it.

For updates, run the checks and build, push the validated source to GitHub and the Site source branch, package with the Sites hosting helper, save the version and publish it to the existing public audience. Source credentials are temporary and must never be saved in the repository. GitHub pushes do not trigger deployment automatically.

No custom domain, DNS changes or GitHub Pages workflow is configured. The eventual `wrenasmir.com` subdomain can be connected later; the static build can also move to another host without changing the music library.

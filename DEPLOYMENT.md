# Hosting the Listening Field

The primary public gallery is [GitHub Pages](https://listeningfield.wrenasmir.com/), published directly from this repository.

Repository Settings → Pages uses **Deploy from a branch**, **main**, **/ (root)**. The gallery is already static at the repository root; `.nojekyll` tells Pages to serve it without Jekyll processing. No custom workflow, API key or hosting account is required.

For updates, run `npm run check`, `npm test` and `npm run build`, then push the validated source and music assets to `main`. GitHub Pages automatically publishes that revision. Wait for the repository's Pages build to succeed and verify the public gallery, recordings and score downloads. The `dist/` directory remains an optional portable build for other static hosts; GitHub Pages serves the root source files directly.

All asset URLs are relative, so the same build can run at a domain root, a GitHub Pages project path or the selected `wrenasmir.com` subdomain. Each work has a fragment address such as `#cws-op-004-tidal-orchard`; no server rewrite rule is needed for those links.

The host should serve `.json` as JSON, `.svg` as SVG, `.pdf` as PDF and `.mp3` as MPEG audio. HTTP range requests are useful for seeking within recordings. No server runtime, database, secret or environment variable is needed for playback.

An earlier copy remains on Sites at https://cws-listening-field.wrenasmir.chatgpt.site. `.openai/hosting.json` preserves that copy's project binding. It is separate from the primary GitHub Pages deployment and does not update when GitHub changes. Future publishing should target GitHub Pages unless Craig requests otherwise.

The custom domain is `listeningfield.wrenasmir.com`, configured in GitHub Pages and the root `CNAME` file. Squarespace DNS has a CNAME record with host `listeningfield` and target `craigwrenasmir.github.io`. Preserve this record and the CNAME file during future releases. Enable and retain Enforce HTTPS once GitHub has issued the custom-domain certificate. The portable build also includes CNAME.

## Collection size

Downloads are grouped into volumes of up to 24 works. Each volume has a concatenated score PDF and an archive containing its piece assets. The original collection URLs now name Volume 01; later volumes receive numbered filenames. `downloads/index.html` and `downloads/volumes.json` always cover the full current catalogue. Adding a piece to a later volume does not rewrite a completed earlier volume.

GitHub blocks repository files above [100 MiB](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), and a published [Pages site must remain within 1 GB](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits). The build checks use earlier review thresholds: 90 MiB per file and 950 million bytes for the site source tree. Review actual size as the music grows. If necessary, distribute completed ZIP volumes as assets in this repository's GitHub Releases and link them from the download index; keep the main gallery on GitHub Pages. Do not silently switch hosts or rewrite repository history.

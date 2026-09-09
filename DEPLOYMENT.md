# Hosting the Listening Field

The primary public gallery is [GitHub Pages](https://listeningfield.wrenasmir.com/), published directly from this repository.

Repository Settings → Pages uses **Deploy from a branch**, **gh-pages**, **/ (root)**. The source, composition definitions and all music assets stay on **main**. The publication branch contains only the checked static build, with `.nojekyll` and the existing CNAME.

For updates:

1. Finish the selected music pipeline and visual score review. Run `npm test` and `npm run build` (which includes `npm run check`).
2. Commit the source and music assets. The build must match that clean commit exactly.
3. Make every archive with `zip_url` in `downloads/volumes.json` available at its exact GitHub Release URL. Tags are `volume-N`; upload the matching `CWS_Volume_NN.zip`. Create a new tag at the reviewed source commit before creating its Release. Growing volumes retain their URL; replace the asset only when its membership changes. Preserve closed volume assets.
4. Run `node scripts/publish-pages.mjs --publish`. It verifies the build against committed blobs, verifies each external archive byte for byte, then advances `main` and `gh-pages` together with a non-forced atomic push. Without `--publish`, it prepares the snapshot without changing remote refs.
5. Wait for the Pages build for the returned **pagesCommit**, then compare deployed gallery data, all new scores/audio and download assets against the tested files. Record both source and Pages commits. Keep HTTPS enforced.

On the initial migration to this flow, set Pages to `gh-pages` after that branch exists, then request one Pages build (`gh api -X POST repos/CraigWrenasmir/cws-listening-field/pages/builds`). There is no custom Actions workflow or additional hosting service. The publication branch reuses the source blobs and has its own append-only commit history; the source branch history is preserved.

Gallery asset URLs are relative, so the same build can run at a domain root, a GitHub Pages project path or the selected `wrenasmir.com` subdomain. Each work has a fragment address such as `#cws-op-004-tidal-orchard`; no server rewrite rule is needed for those links.

The host should serve `.json` as JSON, `.svg` as SVG, `.pdf` as PDF and `.mp3` as MPEG audio. HTTP range requests are useful for seeking within recordings. No server runtime, database, secret or environment variable is needed for playback.

An earlier copy remains on Sites at https://cws-listening-field.wrenasmir.chatgpt.site. `.openai/hosting.json` preserves that copy's project binding. It is separate from the primary GitHub Pages deployment and does not update when GitHub changes. Future publishing should target GitHub Pages unless Craig requests otherwise.

The custom domain is `listeningfield.wrenasmir.com`, configured in GitHub Pages and the root `CNAME` file. Squarespace DNS has a CNAME record with host `listeningfield` and target `craigwrenasmir.github.io`. Preserve this record and the CNAME file during future releases. Enable and retain Enforce HTTPS once GitHub has issued the custom-domain certificate. The portable build also includes CNAME.

## Collection size

Downloads are grouped into volumes of up to 24 works. Each volume has a concatenated score PDF and an archive containing its piece assets. The original collection URLs now name Volume 01; later volumes receive numbered filenames. `downloads/index.html` and `downloads/volumes.json` always cover the full current catalogue. Adding a piece to a later volume does not rewrite a completed earlier volume.

GitHub blocks repository files above [100 MiB](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github), and a published [Pages site must remain within 1 GB](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits). The build checks use earlier review thresholds: 90 MiB per file and 950 million bytes for the actual publication file set. Review actual size as the music grows. If necessary, distribute completed ZIP volumes as assets in this repository's GitHub Releases and link them from the download index; keep the main gallery on GitHub Pages. Do not silently switch hosts or rewrite repository history.

The portable `dist/` build is also the exact Pages publication. It excludes build scripts, the full source catalogue, raw per-piece JSON (retained in the repository and complete ZIPs), and ZIPs with an external Release URL. `library.json`, series metadata, every public individual PDF/MP3/MIDI/MusicXML/SVG, all combined score PDFs and original Volume 1–10 archives remain on Pages. `scripts/site-distribution.mjs` is shared by the size check, build and publisher; `scripts/test-site-distribution.mjs` checks complete runtime/download coverage. Never raise the size guard as a substitute for reviewing distribution.

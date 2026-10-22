# dwg7/waterloo — working rules

A small repository. Work through to the end without stopping. Stop and ask the user only where marked **STOP**.

## What this is

A GitHub Pages site (`docs/`) that shows the high-resolution (about 5 cm) drone image of Waterloo, Sierra Leone, from the new OpenAerialMap (OAM) as PMTiles, with Overture Maps vectors on top, using MapLibre GL JS. This is a dwg7 activity. It is not an official OAM or HOT project.

Two goals:

1. **Try the new OAM PMTiles feature for real and record the facts** in `docs/oam-pmtiles.md`.
2. **Thank the people who made the image**, with accurate credit (`docs/credits.html`, `README.md`).

Background: UNopenGIS/7 issues #1023 (and #1019).

## The image (re-verify at the start of each task)

- OAM ID `6aae46379ed4c3b5f2d117f9`; API: `https://api.openaerialmap.org/meta/6aae46379ed4c3b5f2d117f9`; STAC: `https://api.imagery.hotosm.org/stac/collections/openaerialmap/items/6aae46379ed4c3b5f2d117f9`
- Waterloo, Sierra Leone; acquired 2026-02-07 to 2026-06-03; registered in OAM 2026-09-19
- DJI Mini 5 Pro, about 5 cm; provider HOT; license CC BY-SA 4.0; source GeoTIFF about 4.7 GB
- New OAM: `https://imagery.hotosm.org/browse?lat=8.3302&lon=-13.0693&zoom=17.2&selected_id=6aae46379ed4c3b5f2d117f9`
- uMap: `https://umap.hotosm.org/en/map/waterloo-open-drone-imagery_6651`

## Tasks

1. Get the PMTiles from new OAM (packager API), download it once, and record everything in `docs/oam-pmtiles.md`: URL and steps, size, SHA-256, date, `pmtiles show` output (tile format, zoom, bounds, metadata), what went as expected, what was hard, what is unknown. Separate fact from guess. Write as a calm, specific report from someone who tried it. Not as criticism.
2. Place the PMTiles on stars (stars.optgeo.org). **STOP** and ask the user if the way to place it (location, martin config, access) is unclear.
3. `docs/index.html`: MapLibre GL JS + pmtiles library, versions pinned in the CDN URL, no build step. Layers: OAM imagery (from stars), Overture buildings (`https://stars.optgeo.org/overture_buildings/{z}/{x}/{y}`; read the TileJSON for source-layer names and zoom range), optionally other Overture themes already on stars (never create new ones). Start on Waterloo. Let the user compare imagery and buildings (opacity or show/hide). Always show attribution on the map.
4. `docs/credits.html` and `README.md`: image credit (provider, dates, aircraft, resolution, CC BY-SA 4.0 with link to the legal text, link to the OAM page); tiles we distribute are also CC BY-SA 4.0 and we say the format was changed to PMTiles; Overture license and attribution per theme (include "© OpenStreetMap contributors" where OSM-derived data is included), following Overture's official guidance; sincere, concrete thanks. Only facts that can be verified in public information. Personal names only as far as OAM or HOT publish them. Plain English: short sentences, no idioms. Japanese notes are welcome.

## Rules

- **Do not contact anyone outside.** No messages to OAM or HOT people, no GitHub issues or comments. The user checks and sends. Drafts go in `drafts/` (must be fine to be public).
- **No annotations that identify a person from the imagery.** No marks or text pointing to houses or people. Just show the map.
- **Mind the load on servers.** Do not download big files repeatedly. Download once, then use the local copy. Do not hammer the packager API.
- **Pin versions.** MapLibre GL JS and pmtiles are pinned in the CDN URL.
- Commit author email must be `18297+hfu@users.noreply.github.com`.
- Reply to the user in Japanese (polite). Repository content is English (Japanese notes allowed).

## Documents

- `README.md`: what this repo is (English, easy). First lines say this is a dwg7 activity and not official OAM or HOT. Link to the map page, credits, thanks, and #1023.
- `DECISIONS.md`: what was decided and why.

## Done means

GitHub Pages is set to publish from `docs/`, the page opens, and the user gets a report: key points of `docs/oam-pmtiles.md`, the public URL, and what could not be verified.

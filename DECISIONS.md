# Decisions

## 2026-10-15: Try the OAM packager API first
The new OAM offers a "tilepack" API (`packager.imagery.hotosm.org`). We tried it before making anything ourselves, because the goal is to test the new OAM feature. Results are in `docs/oam-pmtiles.md`.

## 2026-10-19: Make our own PMTiles for the map
The OAM file works, but its highest zoom is 20 (256 px tiles, about 15 cm/px) because of the tile-count limit. The source is about 5 cm. To show the detail, we make a second file from the same OAM source image:
- WebP, 512 px tiles, z10 to z21, same specification as `freetown-mapterhorn` on stars.
- Tool: GDAL `gdal raster tile` (single source image). The patched Mapterhorn pipeline used for freetown exists only on another machine's local clone, so we could not reuse it. We kept the specification, not the tool.
- We keep the OAM file as a comparison. The OAM image stays the source, and the thanks to OAM, HOT and the people behind the image do not change.

## Licence of the tiles we serve
CC BY-SA 4.0, the same as the source image. We state that the format was changed (GeoTIFF to PMTiles) and that tiles were resampled.

## Files stay outside the repository
Large files (GeoTIFF, tiles, PMTiles) are not committed. They live in `/Users/hfu/waterloo-data/` and on stars. The repository holds code, docs and records only.

## Not done on purpose
- No contact with OAM or HOT people. Drafts go to `drafts/` for the maintainer to send.
- No marks or notes that point to people or houses on the imagery.

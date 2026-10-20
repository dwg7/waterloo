# Trying the new OAM PMTiles feature (work in progress)

Last updated: 2026-10-19 (UTC).

Report by dwg7. This is a trial report, not criticism. Facts and guesses are kept apart.
Image: OAM ID `6aae46379ed4c3b5f2d117f9` (Waterloo, Sierra Leone).

## Facts (2026-10-15, UTC)
- Packager API (documented at https://packager.imagery.hotosm.org/): `POST /tilepacks/{id}?format=pmtiles`; poll with POST.
- A plain GET on that URL returns the help text (HTTP 200), not the job status.
- No PMTiles asset existed in the STAC item before the request.
- Default request failed (HTTP 409) after about 30 s: "tile count 975300 exceeds MAX_TILE_COUNT=150000; rerun with a lower max_zoom".
- The OAM web button does not send zoom values (read from the page's JavaScript), so this image cannot be packed from the web UI. This is from reading the code, not from clicking the button.
- Sending only `max_zoom` gives HTTP 400: "min_zoom and max_zoom must both be set".
- `min_zoom=10&max_zoom=20` was accepted. Status was `in_progress` from 19:32 to 20:17, then `ready` (about 45 minutes).
- Result URL: https://oin-hotosm-temp.s3.us-east-1.amazonaws.com/6aae384b9ed4c3b5f2d0feaf/0/6aae384b9ed4c3b5f2d0feb0_z10-20.pmtiles

## The downloaded file (2026-10-19, UTC)
- Downloaded once with curl from the URL above: 19:30 to 19:33, 715,676,732 bytes (about 716 MB), about 153 s, HTTP 200 without authentication.
- SHA-256: \`c99b5a0cc1e8cd51e314a4ba8658328fdb59ef47db1cae32ba595a3ced8cc839\`
- \`pmtiles show\`: spec version 3; tile type webp; bounds -13.085693,8.300940 to -13.014251,8.375350 (same as the OAM metadata bbox); min zoom 10, max zoom 20; center -13.049972,8.338145 (center zoom 10); 41,510 tiles; clustered; internal compression gzip; tile compression none; metadata has only \`name\` (the OAM ID), \`format\` webp, \`minzoom\`, \`maxzoom\`. No attribution, license or description in the metadata.
- Tile size: I extracted one tile (z18) and read its WebP header: 256 x 256 px. (Checked on one tile only.)

## As expected
- The API is open (no sign-in), documented on its root page, and the result is a normal PMTiles v3 file that standard tools read.
- Bounds and zoom range match the request.

## Hard
- Default settings fail for this image (975,300 tiles > 150,000), and the web button has no zoom option, so this image cannot be packed from the web page (from reading the page code; I did not press the button).
- Poll must be POST; GET returns help text.
- About 45 minutes with only \`in_progress\` as status.
- With the limit, the highest zoom is 20. At 256 px this is about 14.7 cm/px, coarser than the 5 cm source.
- The license is not in the PMTiles metadata. (The STAC item says CC-BY-SA-4.0; the old API top level says "CC-BY 4.0", which looks like a provider-level value. I did not confirm this.)

## Guesses (not verified)
- 975,300 tiles matches 256 px tiles up to z22 by my own estimate.
- Why the build took 45 minutes is unknown.

## Not yet done
- Whether a self-made 512 px, z21 WebP file is better in practice.
- Placement on stars, map page, credits, README, DECISIONS.md, GitHub Pages.

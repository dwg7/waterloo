# Trying the new OAM PMTiles feature (work in progress)

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

## Guesses (not verified)
- 975,300 tiles matches 256 px tiles up to z22 by my own estimate. z21 would still be over the limit, so z20 (about 14.7 cm/px) is the highest allowed. Native is about 5 cm.

## Not yet done
- Download, SHA-256, `pmtiles show` (tile format, tile size, bounds, metadata).
- Placement on stars, map page, credits, README, DECISIONS.md, GitHub Pages.

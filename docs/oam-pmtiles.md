# Trying the new OAM PMTiles feature (work in progress)

Last updated: 2026-10-22 (UTC).

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

## Our own file (for comparison)
Because the OAM file stops at z20 (256 px), we made a second file from the same source GeoTIFF
(downloaded once from OAM: 4,728,337,191 bytes, SHA-256 `431493ff4900b4bfb05ee786f5f88519eb6f5fcc33ad80f3f9f9880049ba8130`, YCbCr JPEG, 156606 x 163849 px, EPSG:32628, with overviews and a mask):
- Tool: GDAL 3.13 `gdal raster tile` (WebP quality 85, 512 px, z10 to z21, Lanczos, 4 threads, 8 GB RAM machine). It took 2 h 09 min.
- 164,378 tiles, 7.2 GB as files, 7.4 GB as PMTiles (`tools/tiles_to_pmtiles.py`). `pmtiles verify` passed.
- SHA-256 of the PMTiles: `1e3c5bdf124d8df946291298513cc6da682c471960147c732c152c57548a4fdf`
- Looking at tiles and the map, buildings and roads are clear at z19, and z21 is a little soft but usable. Overture building outlines line up with the imagery.
- This is about 10 times larger than the OAM file (716 MB), because it has two more zoom levels with 4 times more pixels per level.
- It is served from stars as `waterloo-oam` (Martin) after an rsync with matching SHA-256.

## Note about reading PMTiles from a web page
`depot.optgeo.org` (stars) answers byte-range GET requests, but answers the browser's CORS pre-check (OPTIONS with `Range`) with 405, so a page on another origin cannot use the pmtiles library on it directly. Our map uses the Martin XYZ tiles instead. (This is about stars, not OAM.) Update 2026-10-24: the stars maintainers have since fixed this, and we confirmed OPTIONS 204 and Range 206. They also saw a Range request answered with 200 (the whole file) a few times via Cloudflare; the cause is unknown.
The OAM file URL (S3) was not tested for CORS from a browser.

## Not yet done
- Browser access (CORS) to the OAM-made file on S3.
- Why the OAM build takes 45 minutes.

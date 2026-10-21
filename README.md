# waterloo

**This is an activity of dwg7. It is not an official project of OpenAerialMap (OAM) or HOT.**

We show a high-resolution drone image of Waterloo, Sierra Leone on a web map, together with Overture Maps buildings.
The image comes from the new [OpenAerialMap](https://imagery.hotosm.org/). We use it as PMTiles.

- Map: https://dwg7.github.io/waterloo/
- Credits and thanks: [docs/credits.html](https://dwg7.github.io/waterloo/credits.html)
- Our trial notes on the OAM PMTiles feature: [docs/oam-pmtiles.md](docs/oam-pmtiles.md)
- Background: [UNopenGIS/7 #1023](https://github.com/UNopenGIS/7/issues/1023) (and #1019)

## Why

People at OAM said the PMTiles feature is something you must try to understand.
So we tried it, and we wrote down what happened as facts. The notes are a report from someone who tried it.
They are not criticism.

## The image

| | |
|---|---|
| Title | Waterloo, Sierra Leone |
| Provider | HOT |
| Acquired | 2026-02-07 to 2026-06-03 |
| Aircraft | DJI Mini 5 Pro |
| Size of a pixel | about 5 cm |
| Added to OAM | 2026-09-19 |
| License | [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) |
| OAM page | [OAM](https://imagery.hotosm.org/browse?lat=8.3302&lon=-13.0693&zoom=17.2&selected_id=6aae46379ed4c3b5f2d117f9), ID `6aae46379ed4c3b5f2d117f9` |

We changed the format (GeoTIFF to PMTiles). The tiles we serve are also CC BY-SA 4.0.
See [credits](docs/credits.html) for details.

## What is here

- `docs/index.html` – the map (MapLibre GL JS 5.6.0 and pmtiles 4.3.0 from a CDN, no build step)
- `docs/credits.html` – credits, licenses, thanks
- `docs/oam-pmtiles.md` – what we found when we tried the OAM PMTiles feature
- `tools/tiles_to_pmtiles.py` – packs a `z/x/y.webp` folder into one PMTiles file
- `CLAUDE.md`, `DECISIONS.md` – working rules and decisions

Large files (the GeoTIFF and the PMTiles) are not in this repository. The imagery is served from stars.optgeo.org.

## Thank you

To the people who flew and processed this survey; to HOT, who shared it under an open license;
to the people who built the new OAM; to OpenStreetMap and Overture Maps contributors.
Details are on the [credits page](docs/credits.html).

## Overture Maps

Buildings and roads: © Overture Maps Foundation, © OpenStreetMap contributors (ODbL).
See the [Overture attribution page](https://docs.overturemaps.org/attribution).

---

日本語：dwg7 の活動です（OAM・HOT の公式なものではありません）。シエラレオネ・ウォータールーの約 5 cm のドローン画像（HOT 提供、CC BY-SA 4.0）を、新しい OAM から PMTiles として取り出して試し、Overture の建物と重ねて表示します。試した結果は `docs/oam-pmtiles.md` に事実として記録しています。

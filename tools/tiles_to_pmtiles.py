#!/usr/bin/env python3
"""Pack a z/x/y.webp directory (from `gdal raster tile`) into one PMTiles v3 file.

Usage: tiles_to_pmtiles.py TILE_DIR OUT.pmtiles
Tiles are written in Hilbert (tile id) order, as the PMTiles writer requires.
"""
import json, math, os, sys
from pmtiles.tile import zxy_to_tileid, TileType, Compression
from pmtiles.writer import Writer

src, out = sys.argv[1], sys.argv[2]
tiles = []
for z in sorted(int(d) for d in os.listdir(src) if d.isdigit()):
    for x in os.listdir(f"{src}/{z}"):
        if not x.isdigit():
            continue
        for f in os.listdir(f"{src}/{z}/{x}"):
            if f.endswith(".webp"):
                tiles.append((zxy_to_tileid(z, int(x), int(f[:-5])), z, int(x), int(f[:-5])))
tiles.sort()
minz, maxz = tiles[0][1], max(t[1] for t in tiles)

def lonlat(z, x, y):
    n = 2 ** z
    return (x / n * 360 - 180, math.degrees(math.atan(math.sinh(math.pi * (1 - 2 * y / n)))))
top = [t for t in tiles if t[1] == maxz]
w, n_ = lonlat(maxz, min(t[2] for t in top), min(t[3] for t in top))
e, s = lonlat(maxz, max(t[2] for t in top) + 1, max(t[3] for t in top) + 1)

meta = json.load(open(sys.argv[3])) if len(sys.argv) > 3 else {}
meta.update({"format": "webp", "minzoom": str(minz), "maxzoom": str(maxz)})
with open(out, "wb") as fo:
    wr = Writer(fo)
    for tid, z, x, y in tiles:
        with open(f"{src}/{z}/{x}/{y}.webp", "rb") as f:
            wr.write_tile(tid, f.read())
    wr.finalize({
        "tile_type": TileType.WEBP, "tile_compression": Compression.NONE,
        "min_zoom": minz, "max_zoom": maxz,
        "min_lon_e7": int(w * 1e7), "min_lat_e7": int(s * 1e7),
        "max_lon_e7": int(e * 1e7), "max_lat_e7": int(n_ * 1e7),
        "center_zoom": 17, "center_lon_e7": int((w + e) / 2 * 1e7), "center_lat_e7": int((s + n_) / 2 * 1e7),
    }, meta)
print(len(tiles), "tiles", minz, maxz, (w, s, e, n_))

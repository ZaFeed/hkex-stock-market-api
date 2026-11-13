"""Normalize HK cash-stock identifiers and check the public ZaFeed sample directory."""
import json
import re
import sys
from urllib.request import Request, urlopen

def normalize(raw):
    code = raw.strip().upper().removeprefix("HKEX:")
    if not re.fullmatch(r"[0-9]{1,5}", code) or not int(code):
        raise ValueError(f"Expected a one- to five-digit HKEX code: {raw!r}")
    return f"HKEX:{code.zfill(5)}"

def main(argv):
    try:
        symbols = [normalize(raw) for raw in (argv or ["700", "00005", "HKEX:09988"])]
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    request = Request("https://www.zafeed.com/api/v1/public/symbols", headers={"User-Agent": "ZaFeed-HKEX-Example/1.0"})
    with urlopen(request, timeout=15) as response:
        listed = {row["api"] for row in json.load(response)["data"] if row["m"].upper() == "HK"}
    print(json.dumps([{"symbol": s, "inSampleCatalog": s in listed} for s in symbols], indent=2))

if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/env python3
"""Download the app's Google Fonts once and bundle them for offline use.

Run with internet access from the repo root:  python3 scripts/fetch-fonts.py
Writes woff2 files and fonts.css into app/src/main/assets/www/fonts/.
"""
import pathlib
import re
import urllib.request

CSS_URL = (
    "https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500"
    "&family=Instrument+Sans:wght@400;500;600&family=Instrument+Serif&display=swap"
)
OUT = pathlib.Path(__file__).resolve().parent.parent / "app/src/main/assets/www/fonts"
# A modern browser User-Agent makes Google return woff2 files.
UA = "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 Chrome/124.0 Mobile Safari/537.36"


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    css = get(CSS_URL).decode("utf-8")
    urls = sorted(set(re.findall(r"url\((https://[^)]+\.woff2)\)", css)))
    for i, url in enumerate(urls, 1):
        name = f"font-{i:02d}.woff2"
        (OUT / name).write_bytes(get(url))
        css = css.replace(url, name)
        print(f"saved {name}")
    (OUT / "fonts.css").write_text(css, encoding="utf-8")
    print(f"wrote {OUT / 'fonts.css'} ({len(urls)} font files)")


if __name__ == "__main__":
    main()

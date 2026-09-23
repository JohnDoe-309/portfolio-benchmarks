#!/usr/bin/env python3
"""Merge pipe-delimited research rows into data/sites.json and regenerate the README tables.

Rows look like:
    name | url | who | take | leave | YYYY-MM-DD

Usage:
    python3 scripts/ingest.py --category top --segment "Craft showpieces" rows.txt
    python3 scripts/ingest.py --render          # regenerate README from data only

Dedupe is by normalised URL, so re-running an ingest is safe.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
from urllib.parse import urlsplit

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "sites.json"
README = ROOT / "README.md"
BEGIN, END = "<!-- BEGIN:tables -->", "<!-- END:tables -->"

CATEGORIES = {
    "top": "Top personal portfolios",
    "peers": "Operators, PMs and builders like me",
    "freelancers": "Freelancers and fractional consultants",
    "alumni": "BITS Pilani and IIT alumni",
}


def norm(url: str) -> str:
    parts = urlsplit(url if "://" in url else f"https://{url}")
    host = parts.netloc.lower().removeprefix("www.")
    path = parts.path.rstrip("/")
    return f"{host}{path}"


def load() -> dict:
    if DATA.exists():
        return json.loads(DATA.read_text())
    return {"updated": "", "count": 0, "sites": []}


def parse_rows(text: str) -> list[dict]:
    rows = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("|---"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 5 or not re.search(r"https?://|\w+\.\w", parts[1]):
            continue
        name, url, who, take = parts[0], parts[1], parts[2], parts[3]
        leave = parts[4] if len(parts) > 4 else ""
        checked = parts[5] if len(parts) > 5 else ""
        if not url.startswith("http"):
            url = f"https://{url}"
        rows.append({"name": name, "url": url, "who": who, "take": take,
                     "leave": None if leave in {"", "—", "-"} else leave, "last_checked": checked})
    return rows


def ingest(path: pathlib.Path, category: str, segment: str) -> tuple[int, int]:
    if category not in CATEGORIES:
        sys.exit(f"unknown category {category!r}; pick one of {', '.join(CATEGORIES)}")
    db = load()
    seen = {norm(s["url"]) for s in db["sites"]}
    added = skipped = 0
    for row in parse_rows(path.read_text()):
        key = norm(row["url"])
        if key in seen:
            skipped += 1
            continue
        seen.add(key)
        db["sites"].append({**row, "category": category, "segment": segment})
        added += 1
    db["count"] = len(db["sites"])
    DATA.write_text(json.dumps(db, indent=2, ensure_ascii=False) + "\n")
    return added, skipped


def render() -> int:
    db = load()
    out = [f"_{db['count']} sites, all fetched and confirmed loading on the date in each row._\n"]
    for key, title in CATEGORIES.items():
        sites = [s for s in db["sites"] if s.get("category") == key]
        if not sites:
            continue
        out.append(f"\n## {title} · {len(sites)}\n")
        for segment in dict.fromkeys(s.get("segment", "") for s in sites):
            in_segment = [s for s in sites if s.get("segment", "") == segment]
            if segment:
                out.append(f"\n### {segment}\n")
            out.append("\n| Site | Who | Take | Leave | Checked |\n|---|---|---|---|---|")
            for s in sorted(in_segment, key=lambda x: x["name"].lower()):
                out.append(
                    f"| [{s['name']}]({s['url']}) | {s['who']} | {s['take']} | {s['leave'] or '—'} | {s['last_checked']} |"
                )
            out.append("")
    body = "\n".join(out)
    text = README.read_text()
    start, end = text.index(BEGIN) + len(BEGIN), text.index(END)
    README.write_text(text[:start] + "\n" + body + "\n" + text[end:])
    return db["count"]


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("rows", nargs="?", type=pathlib.Path)
    ap.add_argument("--category", default="")
    ap.add_argument("--segment", default="")
    ap.add_argument("--render", action="store_true")
    args = ap.parse_args()
    if args.rows:
        a, s = ingest(args.rows, args.category, args.segment)
        print(f"added {a}, skipped {s} duplicates")
    total = render()
    print(f"README rendered with {total} sites")

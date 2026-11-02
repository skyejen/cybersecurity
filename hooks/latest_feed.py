"""Build-time hook: emits `latest.json` at the site root.

A small feed of the most recently added write-ups (title, URL, date, section),
read straight from each write-up's meta block, so it is always current. Served
at https://skyejen.github.io/cybersecurity/latest.json and consumed by the
"Recently added" section on the main landing page (skyejen.github.io).

A write-up is any page under `learning/` that carries a `**Date:**` meta line;
hub/index pages don't, so they're skipped automatically.

NOTE: hook changes need a `mkdocs serve` RESTART to take effect. Fresh builds
(including CI deploys) always pick them up.
"""
import json
import re
from datetime import date
from pathlib import Path

_ICON = re.compile(r":[\w-]+:")
_DATE = re.compile(r"(\d{1,2})/(\d{1,2})/(\d{4})")
_LIMIT = 10


def _title(text: str):
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return _ICON.sub("", s[2:]).strip()
    return None


def _date(text: str):
    for line in text.splitlines():
        if "**Date:**" in line:
            found = _DATE.findall(line)
            if found:
                d, m, y = found[-1]  # ranges like 21-23/06/2026 -> end date
                try:
                    return date(int(y), int(m), int(d))
                except ValueError:
                    return None
    return None


def _nav_paths(nav) -> set:
    """All .md doc paths referenced anywhere in the nav tree (published pages)."""
    paths = set()

    def walk(items):
        for item in items or []:
            if isinstance(item, str):
                paths.add(item)
            elif isinstance(item, dict):
                for val in item.values():
                    walk(val if isinstance(val, list) else [val])
            elif isinstance(item, list):
                walk(item)

    walk(nav)
    return paths


def _where(text: str):
    for line in text.splitlines():
        for label in ("**Path:**", "**Bucket:**"):
            if label in line:
                parts = [p.strip() for p in line.split(label, 1)[1].split(">")]
                parts = [p for p in parts if p]
                if not parts:
                    return ""
                # "Off the Beat" is a catch-all bucket; the platform sits one deeper.
                if parts[0] == "Off the Beat" and len(parts) > 1:
                    return parts[1]
                return parts[0]
    return ""


def on_post_build(config):
    docs = Path(config["docs_dir"])
    site_url = str(config.get("site_url", "")).rstrip("/")
    published = _nav_paths(config.get("nav") or [])
    items = []
    for p in (docs / "learning").rglob("*.md"):
        if p.name in ("index.md", "write-up-template.md"):
            continue
        if p.relative_to(docs).as_posix() not in published:
            continue  # skip backlog drafts not wired into the nav
        text = p.read_text(encoding="utf-8")
        if "**Date:**" not in text:
            continue
        d, title = _date(text), _title(text)
        if not d or not title:
            continue
        rel = p.relative_to(docs).with_suffix("").as_posix()
        items.append({
            "title": title,
            "url": f"{site_url}/{rel}/",
            "date": d.isoformat(),
            "where": _where(text),
        })
    items.sort(key=lambda x: x["date"], reverse=True)
    payload = {"generated": date.today().isoformat(), "items": items[:_LIMIT]}
    out = Path(config["site_dir"]) / "latest.json"
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")

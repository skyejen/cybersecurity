"""Build-time hook: fills placeholders on the Learning landing page.

  {{ count_cs101 }} / {{ count_jrpt }} / {{ count_side }}  -> write-up counts
  {{ cat_tryhackme }} / {{ cat_off_the_beat }}             -> nav category names
    (section headers auto-follow any nav rename — one source of truth)

NOTE: hook changes need a `mkdocs serve` RESTART to take effect (they don't hot-reload).
Everything works on a fresh build, including CI deploys.
"""
from pathlib import Path


def _count(docs: Path, rel: str) -> int:
    root = docs / rel
    if not root.exists():
        return 0
    return sum(1 for p in root.rglob("*.md")
               if p.name not in ("index.md", "write-up-template.md"))


def _learning_category_titles(config) -> dict:
    def find_learning(items):
        for item in items or []:
            if isinstance(item, dict):
                for key, val in item.items():
                    if key == "Learning" and isinstance(val, list):
                        return val
                    if isinstance(val, list):
                        found = find_learning(val)
                        if found:
                            return found
        return None

    def first_doc(val):
        if isinstance(val, str):
            return val
        if isinstance(val, dict):
            for v in val.values():
                p = first_doc(v)
                if p:
                    return p
        if isinstance(val, list):
            for v in val:
                p = first_doc(v)
                if p:
                    return p
        return None

    titles = {}
    for item in find_learning(config.get("nav") or []) or []:
        if isinstance(item, dict):
            for title, val in item.items():
                path = first_doc(val)
                if path and path.startswith("learning/"):
                    titles[path.split("/")[1]] = title
    return titles


def on_page_markdown(markdown, page, config, files):
    if page.file.src_uri != "learning/index.md":
        return markdown
    docs = Path(config["docs_dir"])
    cats = _learning_category_titles(config)
    return (markdown
            .replace("{{ cat_tryhackme }}", cats.get("tryhackme", "TryHackMe"))
            .replace("{{ cat_off_the_beat }}", cats.get("off-the-beat", "Off the Beat"))
            .replace("{{ count_cs101 }}", str(_count(docs, "learning/tryhackme/cyber-security-101/write-ups")))
            .replace("{{ count_jrpt }}", str(_count(docs, "learning/tryhackme/penetration-tester")))
            .replace("{{ count_side }}", str(_count(docs, "learning/tryhackme/side-quests"))))

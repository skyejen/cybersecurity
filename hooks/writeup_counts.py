"""Build-time hook: replaces count placeholders on the homepage.

Usage in markdown: {{ count_cs101 }}, {{ count_jrpt }}, {{ count_side }}
Counts update automatically on every build (including GitHub Actions deploys).
"""
from pathlib import Path


def _count(docs: Path, rel: str) -> int:
    root = docs / rel
    if not root.exists():
        return 0
    # count write-ups only — skip section landing pages and the nav template
    return sum(
        1 for p in root.rglob("*.md")
        if p.name not in ("index.md", "write-up-template.md")
    )


def on_page_markdown(markdown, page, config, files):
    # The learning home now lives at learning/index.md (was index.md before the
    # portfolio/learning split).
    if page.file.src_uri != "learning/index.md":
        return markdown
    docs = Path(config["docs_dir"])
    return (
        markdown
        .replace("{{ count_cs101 }}", str(_count(docs, "learning/tryhackme/cyber-security-101/write-ups")))
        .replace("{{ count_jrpt }}", str(_count(docs, "learning/tryhackme/penetration-tester")))
        .replace("{{ count_side }}", str(_count(docs, "learning/tryhackme/side-quests")))
    )

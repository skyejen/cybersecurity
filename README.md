# skyejen / cybersecurity

Cybersecurity portfolio and learning write-ups, part of **[skyejen.github.io](https://skyejen.github.io)**. Home labs, detection engineering, TryHackMe path notes, standalone challenges and other side-quests.

Live at **https://skyejen.github.io/cybersecurity**

## Local development

This site shares a design system with my other repos via the `sj-theme` git submodule.

```bash
git clone https://github.com/skyejen/cybersecurity.git
cd cybersecurity
git submodule update --init            # pull in sj-theme
pip install "mkdocs-material>=9.7,<10" "pymdown-extensions>=10,<11"
mkdocs serve                           # http://127.0.0.1:8001
```

## Structure

- `docs/portfolio/` — home labs & projects
- `docs/learning/` — TryHackMe paths, notes, and walkthroughs
- `docs/sj-theme/` — shared theme (git submodule)
- `overrides/` — theme customisations

Deploys automatically to GitHub Pages on push to `main` (see `.github/workflows/deploy.yml`).

# Agent instructions

How AI agents (Claude, Codex, etc.) should work in this repo. **Read this before editing.**
The sibling repos `skyejen.github.io` and `100-days-of-python` share this theme, so the same
rules apply there.

## Golden rules

1. **Reuse before building.** Grep for the existing pattern first (`sj-card`, a template, an
   existing landing) and match it. Don't invent new components or styles.
2. **Scope custom tweaks, never touch globals.** If one place needs a unique look, add a
   modifier class or id and style that (e.g. `.sj-cards--compact`, `.sj-home`,
   `.sj-home .sj-brand::after`). Editing `.sj-card` / `.md-header` / etc. directly breaks every
   other instance across the site.
3. **Build before you're done:** `mkdocs build --strict` must pass with no warnings.
4. **Jen commits.** Don't run git commits or pushes. Leave staging and commit messages to Jen.
5. **Keep this doc current.** If you introduce a new element, pattern, or system (a new
   component, a structural change, a new convention like the nbsp/`sj-cards--compact` rules),
   document it here in the same pass — and flag whether it should be ported to the sibling
   repos. This file is only useful if it stays true.

## Writing in Jen's voice (drafts she will "jenify")

When drafting prose in Jen's voice (write-ups, page copy), write a plain first draft she edits.

- **No em dashes. Ever.** Use commas, brackets, or full stops.
- **No AI-speak / LLM tics.** Avoid: "Honestly?", "at the intersection of", "spearheaded", the
  "it's not X, it's Y" / "it's THIS, not THAT" antithesis, "delve", "leverage", "seamless",
  "testament to", "it's worth noting", "in today's world", rhetorical "But here's the thing",
  and the tidy rule-of-three cadence. Write like a person, not a landing page.
- **No bold or italics.** Leave `**bold**` and `_italics_` out. Jen adds emphasis herself.
- **Match her tone first.** Before drafting, read 2-3 of her recent write-ups (newest under
  `docs/learning/tryhackme/`, plus the informal Wazuh one under `docs/learning/off-the-beat/`)
  to catch her wording, rhythm and humour.
- **Draft, don't finalise.** Assume she rewrites every line. Keep it plain and short.

## Page skeleton (every content page)

    # :material-ICON: Page Title

    One or two intro sentences.

    ---

    ## :material-ICON: Section

    ...content...

- H1 always opens with a `:material-…:` icon.
- Always put a **`---`** after the intro, before the first section. (Jen shouldn't have to add
  it every time.)
- Copy from the templates: `templates/write-up-template.md` (room / lab write-ups) and
  `templates/landing-page-template.md` (index / landing pages).

## Tiles

Use the `sj-cards` grid + `sj-card` tiles, never a bespoke card.

    <div class="sj-cards" markdown>

    <a class="sj-card" href="URL/" markdown="span">
    <span class="sj-card-icon">:material-ICON:</span>
    <span class="sj-card-title">Title</span>
    <span class="sj-card-desc" title="Full text, shown on hover.">Short desc (2 lines max).</span>
    <span class="sj-card-meta">meta <span class="sj-dot">·</span> chip</span>
    </a>

    </div>

- Tile `href` is the **final directory URL** (`.../slug/`, trailing slash). Raw HTML isn't
  rewritten by mkdocs, so don't use the `.md` path.
- **Compact / index tiles** (icon + title only, e.g. learning-path landings): add the
  `sj-cards--compact` modifier to the grid. Narrower, same height. Feature tiles with
  descriptions stay plain `sj-cards`.
- `sj-card-desc` and `sj-card-meta` are optional. Omit them for title-only tiles.

## Typography

- **Non-breaking hyphen** `&#8209;` for compounds that must not split: multi&#8209;OS,
  MITRE&#8209;mapped, write&#8209;ups.
- **Non-breaking space** `&nbsp;` to bind a short connector word to the next so it can't wrap
  alone: `The&nbsp;Basics`, `Getting&nbsp;Started`. Only small words (the, a, of, to, and…),
  never glue long words together (it overflows the narrow tiles).

## Write-up pages

Full cheat-sheet: `templates/write-up-template.md`. Key points:
- Title `# :material-pound: Room Name`, then a `<div class="sj-meta" markdown>` block
  (Path / Date / Difficulty), then `---`.
- `!!! quicklinks "Quick Links"` admonition with the real room URL and the room name as the
  label. Reuse existing room URLs, don't invent them.
- Section H2s use a material icon + `{ data-toc-label="..." }`. Section icons: covers =
  `:material-clipboard-text-outline:`, did/learned = `:material-laptop:`, struggle =
  `:material-magnify:`, takeaways = `:material-lightbulb-on-outline:`, bonus =
  `:material-star-outline:`.
- Blue lead-in `_text_{ .sj-lead }`; strikethrough `~~text~~` (needs `pymdownx.tilde`);
  collapsibles `??? note "Title"` (not `<details>`). Don't touch `<br>` tags, Jen manages those.

## Landings & home pages

- Top-level "doors" pages that should have **no left nav** (the hub, the Portfolio/Learning
  homes) use `template: home.html` in front matter. It renders the contact-card sidebar with no
  nav tree and no TOC. Normal section landings are plain pages and keep the left nav.
- A nav section with an `index.md` as its **first child** renders as a grey clickable landing
  (Material `navigation.indexes`); a pure grouping with no index stays a white label.
- The Learning landing's section headers are pulled from the nav by `hooks/writeup_counts.py`
  (placeholders like `{{ cat_tryhackme }}`, plus the `{{ count_* }}` write-up counts). **Hook
  changes need a `mkdocs serve` restart**, they don't hot-reload, so the page shows raw
  placeholders until you restart.

## Editing safety (this drive silently truncates long lines)

- The in-app editor truncates long single lines when saving to this drive. It has eaten bytes
  from `mkdocs.yml`, the hook, tile `<span>`s, and closing `</div>`s. **Edit long lines in
  VS Code** (native, safe) or write them via the shell. Don't trust the in-app editor for a
  long line.
- **Always end files with a trailing newline.** A no-newline final line is the one most likely
  to get chopped.
- One editor per file at a time. Concurrent saves have collided and corrupted content.

## Local dev & deploy

    pip install "mkdocs-material>=9.7,<10" "pymdown-extensions>=10,<11" "mkdocs-redirects>=1.2,<2"
    mkdocs serve            # live-reload dev server (dev_addr in mkdocs.yml: 127.0.0.1:8001)

- `extra.css` / `extra.js` changes hot-reload (hard-refresh, Ctrl/Cmd+Shift+R, if a JS change
  seems cached). `mkdocs.yml`, hooks, templates and new pages need a **serve restart**.
- Deploy is automatic: `.github/workflows/deploy.yml` runs `mkdocs gh-deploy --force` on every
  push to `main`. Just push. The workflow pins mkdocs-material 9.x, pymdown-extensions 10.x and
  mkdocs-redirects, so keep those in sync locally.

## Jen's working preferences

- **Tone with Jen:** warm, friendly, a bit playful. Concise and direct, cut filler.
- **Fix typos proactively** (standing permission), unless you're unsure of the intended word,
  then ask.
- **Verify before claiming done.** When you can't see the rendered result, say so and ask her
  to check. Don't claim a visual fix works if you haven't verified it. She values the honesty.
- **Root cause over guess-and-check.** She wants to know *why* something broke, not just that
  it's fixed. One change at a time, explained.
- She pastes screenshots (often with DevTools). Use them.
- When you stop to ask (question tool), wait for her reply, don't just go ahead with changes 
  without giving her a chance to reply.

## Theme internals

The theme is `docs/stylesheets/extra.css` (~1300+ lines, authoritative) and
`docs/javascripts/extra.js`. It took many rounds of pixel-tuning, so be surgical.

**Palette (CSS vars in `:root`):**

    --sj-bg #080b13   --sj-bg-deep #04060a   --sj-surface #141b2b   --sj-border #232d40
    --sj-blue #1e88ff --sj-gold #f2c14e      --sj-text #b9c3d2       --sj-text-dim #78839a
    --sj-heading #dee5f0

Fonts: **Inter** (text), **JetBrains Mono** (code), **Space Grotesk** (accents/titles).
Headings h3/h4 `#d8bd7e`, h5 `#cbb277` (pale gold); tooltip text `#e6cf94`.

**Header:** one uniform full-width bottom line (`.md-header::before`) plus a faint faded
brand separator (`.sj-brand::after`), identical on home and docs. The landing (`.sj-home`)
only additionally hides the big nav-column divider (`.md-sidebar--primary::after`), since it
has no nav tree.

**Custom JS systems (`extra.js`):** themed tooltips (native `title` → `data-sj-tip`, styled via
`::after/::before`; variants `sj-tip--up`, `sj-tip--left`); night-mode toggle (warm sepia
`feColorMatrix` filter, saved to `localStorage`); a contained scroller (on desktop the page
scrolls inside `.md-container`, not `window`, so scroll-spy + back-to-top account for that);
gold active-nav bar + nav memory; sidebar feather via `mask-image`; phantom-line trim for code;
a cursor-following card tooltip (`.sj-cursor-tip`, driven by `data-sj-cardtip`) that shows a
clipped tile's full text on hover.

**Hard-won gotchas (don't re-learn these):**
- The code copy button is `<button class="md-code__button" data-md-type="copy">` (not
  `.md-clipboard`), and its icon is drawn with its own `::after` + `mask-image`. You **cannot**
  put `data-sj-tip` on it (the tooltip's `::after` would erase the icon). Wrap it in
  `<span class="sj-tip-wrap">` instead; the JS dedupe flag is `data-sj-wrapped`, not
  `data-sj-tip`, for the same reason.
- `opacity < 1` on hover creates a stacking context that trapped header tooltips behind the
  header line. Material's `.md-source:hover{opacity:.7}` and `.md-header__button:hover{opacity:.7}`
  are overridden to `opacity:1`.
- `content.tooltips` is intentionally NOT enabled, so plain `title` attrs are converted in JS
  (otherwise the ugly native tooltip shows). The search input's `required` attr is stripped in
  JS to kill the browser "please fill in this fi

<!--
  Landing / index page template — copy the bits you need. See AGENTS.md for the full rules.
  - Add the `template: home.html` front matter ONLY for top-level "doors" pages that should
    have NO left nav (the hub, the Portfolio/Learning homes). Omit it for normal section
    landings (they keep the left nav).
  - Compact / title-only grids (e.g. a learning path's index): add `sj-cards--compact`.
-->
---
template: home.html
---

# :material-shield-lock-outline: Page Title

One or two intro sentences saying what this space is.

---

## :material-folder-outline: Section Name

<div class="sj-cards" markdown>

<a class="sj-card" href="target-slug/" markdown="span">
<span class="sj-card-icon">:material-file-document-outline:</span>
<span class="sj-card-title">Tile Title</span>
<span class="sj-card-desc" title="Full description, shown on hover.">Short two-line description.</span>
<span class="sj-card-meta">status <span class="sj-dot">·</span> tag</span>
</a>

</div>

<!-- Title-only / index variant (no descriptions) — add sj-cards--compact:

## :material-folder-outline: A Path

<div class="sj-cards sj-cards--compact" markdown>

<a class="sj-card" href="some-writeup/" markdown="span">
<span class="sj-card-icon">:material-file-document-outline:</span>
<span class="sj-card-title">Write-up Title</span>
</a>

</div>
-->

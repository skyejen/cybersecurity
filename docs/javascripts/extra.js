/* skyejen theme helpers */
document.addEventListener("DOMContentLoaded", function () {

  /* On desktop the page scrolls inside .md-container (below the header) */
  var scroller = window.matchMedia("(min-width: 76.25em)").matches
    ? document.querySelector(".md-container")
    : null;
  var scrollTarget = scroller || window;
  var getScrollTop = function () {
    return scroller ? scroller.scrollTop : window.scrollY;
  };

  /* Rename "Table of contents" (mobile fallback; desktop handled by CSS) */
  document.querySelectorAll(".md-nav--secondary > .md-nav__title").forEach(function (el) {
    el.childNodes.forEach(function (n) {
      if (n.nodeType === 3 && n.textContent.trim()) n.textContent = "On this page";
    });
  });

  /* Brand card in its own slot below the nav scroll area (desktop only) */
  /* Ctrl+K / Cmd+K focuses search, with a hint in the search bar */
  var searchForm = document.querySelector(".md-search__form");
  var searchInput = document.querySelector(".md-search__input");
  if (searchForm && searchInput) {
    var kbd = document.createElement("span");
    kbd.className = "sj-kbd";
    kbd.textContent = (navigator.platform || "").indexOf("Mac") !== -1 ? "⌘ K" : "Ctrl K";
    searchForm.appendChild(kbd);
    document.addEventListener("keydown", function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        searchInput.focus();
      }
    });
  }

  /* Move a "quicklinks" admonition into the right sidebar (desktop only) */
  /* Floating back-to-top button */
  var top = document.createElement("button");
  top.className = "sj-top";
  top.title = "Back to top";
  top.setAttribute("aria-label", "Back to top");
  top.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"></path></svg>';
  top.addEventListener("click", function () {
    scrollTarget.scrollTo({ top: 0, behavior: "smooth" });
  });
  document.body.appendChild(top);
  var onScroll = function () {
    top.classList.toggle("sj-top--visible", getScrollTop() > 400);
  };
  scrollTarget.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Custom ToC scroll-spy: activates sections at 35% viewport height */
  var tocLinks = Array.prototype.slice.call(
    document.querySelectorAll(".md-sidebar--secondary .md-nav__link")
  );
  if (tocLinks.length) {
    var pairs = tocLinks
      .map(function (l) {
        var href = l.getAttribute("href") || "";
        var target = document.getElementById(decodeURIComponent(href.slice(1)));
        return target ? { link: l, target: target } : null;
      })
      .filter(Boolean);
    var spy = function () {
      var threshold = window.innerHeight * 0.25;
      var current = null;
      pairs.forEach(function (p) {
        if (p.target.getBoundingClientRect().top <= threshold) current = p;
      });
      if (!current) current = pairs[0]; /* first section active at page top */
      /* at the very bottom, the last section wins */
      var atBottom = scroller
        ? scroller.scrollTop + scroller.clientHeight >= scroller.scrollHeight - 4
        : window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4;
      if (atBottom) current = pairs[pairs.length - 1];
      pairs.forEach(function (p) {
        p.link.classList.toggle("md-nav__link--active", p === current);
      });
    };
    scrollTarget.addEventListener("scroll", spy, { passive: true });
    spy();
  }

  /* Gold bar for the active nav row (drawn outside the nested-nav clip).
     Skip it for section-index pages — those get plain gold text, no bar. */
  var actRow = document.querySelector(".md-sidebar--primary a.md-nav__link--active");
  if (actRow && actRow.closest(".md-nav__container")) actRow = null;
  var barSidebar = document.querySelector(".md-sidebar--primary");
  var barWrap = document.querySelector(".md-sidebar--primary .md-sidebar__scrollwrap");
  if (actRow && barSidebar && barWrap && window.matchMedia("(min-width: 76.25em)").matches) {
    var bar = document.createElement("div");
    bar.className = "sj-nav-bar";
    barSidebar.appendChild(bar);
    var placeBar = function () {
      var r = actRow.getBoundingClientRect();
      var s = barSidebar.getBoundingClientRect();
      var w = barWrap.getBoundingClientRect();
      bar.style.top = (r.top - s.top) + "px";
      bar.style.height = r.height + "px";
      /* bridge the highlight from the gold bar to the row */
      bar.style.width = Math.max(2, r.left - bar.getBoundingClientRect().left + 1) + "px";
      bar.style.opacity = (r.bottom < w.top + 8 || r.top > w.bottom - 8) ? "0" : "1";
    };
    placeBar();
    /* Only the nav's own internal scroll moves the row relative to the sidebar.
       The main page scroll does NOT (sidebar is sticky) — listening to it
       caused the bar to chase transient sticky positions and snap back. */
    barWrap.addEventListener("scroll", placeBar, { passive: true });
    window.addEventListener("resize", placeBar);
    document.querySelectorAll(".md-sidebar--primary input.md-nav__toggle").forEach(function (t) {
      t.addEventListener("change", function () { setTimeout(placeBar, 300); });
    });
  }

  /* Night mode toggle */
  var nightBtn = document.querySelector(".sj-night-toggle");
  if (nightBtn) {
    nightBtn.addEventListener("click", function () {
      var on = document.documentElement.classList.toggle("sj-night");
      localStorage.setItem("sj-night", on ? "1" : "0");
    });
  }

  var ql = document.querySelector(".md-content .admonition.quicklinks");
  var side = document.querySelector(".md-sidebar--secondary .md-sidebar__scrollwrap");
  if (ql && side && window.matchMedia("(min-width: 76.25em)").matches) {
    var wrap = document.createElement("div");
    wrap.className = "md-typeset sj-ql-wrap";
    wrap.appendChild(ql);
    side.appendChild(wrap);
  }
});

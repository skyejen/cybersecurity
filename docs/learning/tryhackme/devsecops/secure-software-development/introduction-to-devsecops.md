# :material-infinity: Introduction to DevSecOps

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** DevSecOps > Secure Software Development > Introduction to DevSecOps

:material-calendar-month-outline: **Date:** 29/07/2026

:material-signal-cellular-1: **Difficulty:** Medium (THM) / Easy (me)

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: Introduction to DevSecOps](https://tryhackme.com/room/introductiontodevsecops)

## :material-clipboard-text-outline: What this room covers { data-toc-label="What this room covers" }

The first room of TryHackMe's new DevSecOps path. It explains how Waterfall became Agile, then DevOps, and how shifting security left morphed into DevSecOps.

## :material-laptop: What I did / learned { data-toc-label="What I did / learned" }

Most of the Waterfall/Agile/DevOps history was familiar territory (I worked in QA/ops for a decade, but specifically for DevOps, I had been mentored into a lot of this by a wonderful DevOps Engineer at work).

DevSecOps is "shift left" applied specifically to security instead of showing up at the end to reject a release. It's built into every stage of the pipeline loop (plan, code, build, test, release, deploy, operate, monitor).

The room mentioned three things that get in the way of doing this well:

- Security Silos - security treated as one team's job instead of everyone's (shared responsibility!)
- Lack of Visibility & Prioritisation - no shared view of what's actually risky right now
- Stringent Processes - security gates need to be flexible in some cases (e.g. prototyping or experimental stages) so people don't work around them

THM suggested three things to fix those:

- Autonomy - automate the boring checks so teams can self-serve
- Visibility - make a service's security state visible instead of buried somewhere
- Empathy - a platform team's "risk" isn't a core service team's "risk", and the process has to flex for both, not just the loudest one (this is probably a life lesson too :D...)

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- DevSecOps isn't a tool, it's shift-left applied to security - earlier and cheaper beats being an add-on at the end.
- Security Silos, Lack of Visibility, and Stringent Processes are how "shifting left" quietly fails in practice.
- Autonomy needs visibility to actually work, and visibility needs empathy for it to all work together.

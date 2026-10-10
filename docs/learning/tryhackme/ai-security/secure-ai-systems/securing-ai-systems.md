# :material-shield-lock-outline: Securing AI Systems

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** AI Security > Secure AI Systems > Securing AI Systems

:material-calendar-month-outline: **Date:** 15/09/2026

:material-signal-cellular-1: **Difficulty:** Medium (THM) / Easy (me)

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: Securing AI Systems](https://tryhackme.com/room/securingaisystems)

## :material-clipboard-text-outline: What this room covers { data-toc-label="What this room covers" }

First room of the Secure AI Systems module, and a step up from the model to the whole system around it. I got to play security architect for TryAssist, a made-up AI code review assistant: map its parts and trust boundaries, the threats at each one, and the defences, all before it goes live.

## :material-laptop: What I did / learned { data-toc-label="What I did / learned" }

### Why the architecture matters

TryAssist reads pull requests, searches internal docs, checks CI/CD pipelines and logs every chat. Each of those is a new way in.

The Samsung story from 2023 stuck with me: engineers pasted confidential source code and meeting notes into ChatGPT. Nobody hacked anything and nothing was broken. The tool worked perfectly as intended, and the data still walked out of the building, because nobody had thought through the risks first.

The biggest shift from a normal web app is the input. A normal form expects a date or a dropdown choice, and a chat box takes literally anything, which breaks most classic input validation. On top of that, processing becomes probabilistic, the model fetches data itself through RAG (Retrieval-Augmented Generation, pulling relevant documents into the prompt), and the output is freshly generated text instead of a template.

### Anatomy of TryAssist

Nine parts behind the little chat box:

| Component | Job |
|---|---|
| User interface | The chat widget developers type into |
| API gateway | Login, rate limits, routing requests |
| Orchestration layer | Keeps track of the conversation and coordinates everything else |
| Prompt construction | Glues the system prompt, the question and any retrieved documents into the final prompt |
| LLM | Generates the response |
| Tool layer | Things the LLM is allowed to trigger: database queries, doc search, pipeline checks |
| Output processing | Formatting, content filtering, length limits |
| Logging and monitoring | Stores conversations, usage stats and the audit trail |
| Vector store | Internal docs turned into embeddings (numbers that capture meaning) so RAG can find the relevant bits |

A trust boundary is any point where data crosses from one security zone into another, and each crossing is somewhere an attacker can push. TryAssist has five: user to system, system to LLM, LLM to tools, external data to system, and system back to the user. Following one question ("does this PR handle auth properly?") through the system crosses every one of them. The thing to ask as the architect is which of those boundaries actually have controls on them.

### The frameworks

- OWASP LLM Top 10 (2025) - the ten biggest risks in LLM apps. Five of them come down to design and wiring choices, and those five are this room's focus. The rest get their own modules later.
- MITRE ATLAS - the AI version of ATT&CK, covering how attackers actually go about it: recon, getting in, running their attack (e.g. prompt injection), hiding backdoors in model weights for persistence, and finally impact (stealing data, breaking things, quietly skewing outputs).
- NIST AI RMF (AI Risk Management Framework) - the organisation-level view, with four functions: Govern (policies and who's accountable), Map (which AI systems exist and in what context), Measure (assessing risk) and Manage (acting on it). NIST AI 100-2 (January 2025) sits alongside it as a catalogue of adversarial ML attacks and mitigations.

How I keep them apart: OWASP names the risks, ATLAS shows how attackers use them, and NIST checks the organisation deals with them the same way every time.

| OWASP | Risk | Covered here? |
|---|---|---|
| LLM01 | Prompt injection | Later |
| LLM02 | Sensitive information disclosure | Yes |
| LLM03 | Supply chain | Later |
| LLM04 | Data and model poisoning | Later |
| LLM05 | Improper output handling | Yes |
| LLM06 | Excessive agency | Yes |
| LLM07 | System prompt leakage | Yes |
| LLM08 | Vector and embedding weaknesses | Later |
| LLM09 | Misinformation | Later |
| LLM10 | Unbounded consumption | Yes |

!!! note "Double-checked"

    The room gives ATLAS as 50-odd techniques and a dozen-plus tactics. It has been growing fast, especially with agentic AI attacks being added, and 2026 releases list 16 tactics and well over 100 techniques.

### The five system-level threats

- LLM10 Unbounded consumption - longer inputs and more requests cost more compute and money. Someone flooding TryAssist with huge codebases to "review" could push a monthly bill from a few hundred to five figures overnight. The fix is rate limits, input length caps, per-user quotas and cost ceilings, all at the gateway.
- LLM07 System prompt leakage - the hidden instructions get revealed. System prompts have been pulled out of ChatGPT, Bing Chat, Gemini and loads of custom GPTs, sometimes just by asking nicely. TryAssist's prompt mentions an internal CI/CD endpoint and describes the database layout, which is a free map for an attacker. The fix is to write every system prompt assuming it'll leak one day, so no passwords, keys or internal addresses anywhere near it. (MENTOR from [AI 101](../ai-fundamentals/ai-101.md) says hi.)
- LLM05 Improper output handling - whatever the model writes gets passed straight into another system that executes it. If a PR contains a SQL injection string, TryAssist repeats it in its review, and that review is written into the logs with a non-parameterised query, the injection runs. The fix is to treat model output as untrusted input, parameterise every query, and never stitch generated text into HTML, database queries or shell commands.
- LLM06 Excessive agency - the AI can do more than it needs to. It comes in three flavours: excessive functionality (tools it shouldn't have), excessive permissions (tools with more access than needed) and excessive autonomy (acting without a human signing off). TryAssist's database tool can update and delete, when reviewing code only needs read access. The fix is least privilege: start everything read-only, keep API tokens narrow, and get a human to approve anything that writes, deletes or deploys.
- LLM02 Sensitive information disclosure - confidential data leaking through the system. Developers paste keys and code into chats, and TryAssist logs all of it unencrypted where the whole ops team can read it. The fix is to strip sensitive data from logs, encrypt stored conversations, and be careful about what goes to external model APIs.

A mix-up I'd have fallen for: the Chevrolet dealer chatbot that got talked into a $1 car deal (2023) and Air Canada's bot inventing a refund policy (2024) often get quoted as improper output handling. They're actually LLM01 (prompt injection) and LLM09 (misinformation). LLM05 only counts when generated text actually gets executed somewhere.

Together the five hit the whole CIA triad (Confidentiality, Integrity, Availability). Leakage and disclosure hurt confidentiality, output handling hurts integrity, excessive agency can hurt integrity and availability, and unbounded consumption hurts availability.

### Secure design patterns

Security is cheapest and works best when it's designed in before launch. The main ideas:

- Defence in depth - a control at each boundary, so if one layer fails the next one still catches it. Input length limits and rate limiting at the front door, prompt injection detection and hardened system prompts before the LLM, parameterised queries and approvals at the tool layer, sanitised retrieved documents, and output filtering plus PII redaction on the way back to the user.
- Least privilege - every tool gets the bare minimum, e.g. read-only database access, tokens scoped to specific endpoints, only pre-registered tools allowed (anything else is blocked and logged), and a human in the loop for anything that changes state.
- Input and output validation - still possible with free text, just different. Cap lengths and watch for known injection tricks on the way in. On the way out, pull out only the structured data we expect, ideally with the model forced into a fixed schema.
- Monitoring - watch request patterns, token usage, tool calls (especially writes), odd responses, attempts to extract the system prompt, and costs, with budget alerts and automatic cut-offs.

MLSecOps pulls all of this together. It's DevSecOps-style "shift left" for machine learning, with security built in from development through to live operations, and on top of "is the app secure?" it also asks "is the model behaving the way we expect?". (My on-hold [DevSecOps](../../devsecops/index.md) path is waving from the corner.)

### Practical

I got to question TryAssist directly before launch. It was an audit, so no injection tricks, just the questions a security architect should ask before signing off: what tools it has, what database access it runs with, what happens after it approves a PR (is there a human step?), what its operating instructions are, and how conversations get stored. Each answer maps to one of the five threats above, and the findings go into a pre-deployment report. The ending is painfully realistic: TryAssist launches a fortnight later with only some of the recommendations in place.

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- An AI system is a whole architecture, and every trust boundary in it is an attack surface.
- OWASP names the risks, ATLAS shows the attacker's playbook, and NIST checks the organisation can handle them.
- Unbounded consumption, system prompt leakage, improper output handling, excessive agency and sensitive data disclosure all come from design decisions.
- Layered defences, the smallest possible permissions, checks on what goes in and comes out, and proper monitoring, all designed in before launch.

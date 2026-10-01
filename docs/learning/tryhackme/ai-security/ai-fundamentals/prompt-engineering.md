# :material-message-text-outline: Prompt Engineering

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** AI Security > AI Fundamentals > Prompt Engineering

:material-calendar-month-outline: **Date:** 25/08/2026

:material-signal-cellular-1: **Difficulty:** Easy (THM) / Easy (me)

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: Prompt Engineering](https://tryhackme.com/room/promptengineeringaisec)

## :material-clipboard-text-outline: What this room covers { data-toc-label="What this room covers" }

How LLMs read what we type, the dials that change how they answer, and how to write prompts that get useful results. It also sets up why prompt injection works at all (the most fascinating bit). This one is more of a cheat sheet than a story I guess.

## :material-laptop: What I did / learned { data-toc-label="What I did / learned" }

### Tokens

LLMs don't see words. They chop text into tokens, which are small chunks of roughly 3-4 characters, so a typical English word is one or two tokens. Short common words like "dog" get a whole token to themselves, and longer or rarer words get split up.

Each token is then swapped for a number (its ID), and the model only ever works with those numbers, predicting which number comes next. Different model families chop text differently: GPT models use Byte-Pair Encoding and BERT uses WordPiece, so the same sentence turns into different token lists depending on the model.

### Nondeterminism

Sending an LLM an identical question twice would probably result in the two answers being different. That's nondeterminism: same input, different output. Normal code is deterministic (2 + 2 comes back as 4 every single time), but LLMs add randomness when choosing the next token, and there isn't a setting to fully switch it off.

This is what's really interesting when it comes to security. Malware behaves the same way every run, but a defence against a malicious prompt might block it on Monday and let it through on Tuesday.

### The dials

| Setting | What it does | When to use it |
|---|---|---|
| Temperature | How much risk the model takes with its next token. Low (0-0.3) sticks to the most likely token, around 0.7-1 gets more varied, and above ~1.2 it starts turning into a Joker (or Loki?) | Low for code, facts and data extraction, higher for brainstorming and creative writing |
| Max tokens | A ceiling on how long the answer can be (one token is roughly 0.75 of a word) | Keeping answers short and bills small, since paid APIs charge per token |
| Top-p | Only lets the model pick from the most likely tokens that together add up to a set probability (e.g. top-p 0.9 cuts off the unlikely 10%) | An alternative randomness control. We should only ever adjust one or the other, and not both together (too unpredictable) |

Max tokens is a limit, so the model won't necessarily use all of it.

### Context window

The context window is the model's short-term memory, counted in tokens. Everything in the conversation has to fit in it. Once it's full, the oldest parts get dropped, often without any warning (some tools handle it more gracefully, e.g. Claude Code summarises the older conversation to free up space, which it calls compacting), and the model genuinely forgets how the conversation started, or worse, remembers bits that don't fit together.

!!! note "Double-checked"

    The room's figures (8k for older GPT-3.5, 200k for Claude 3.5 Sonnet, 1M+ for Gemini 1.5 Pro) are from a couple of model generations ago. By 2026, 1 million tokens is standard for the big frontier models from Anthropic, OpenAI and Google, and a few go even higher.

### The four pillars of a good prompt

1. Instruction - the actual task, with a clear verb ("Summarise...", "Compare...", "Write...").
2. Context - the background the model needs, e.g. who the audience is, what the situation is, or a role to play ("You are a SOC analyst...").
3. Output format - what the answer should look like: bullets, a table, JSON, a word count.
4. Constraints - the rules and limits, e.g. tone, topics to avoid, "no more than 5 bullets".

It ideally should be specific and without rambling. Too vague ("help me with my write-up") leaves the model guessing. Too wordy (five half-formed wishes in one run-on sentence) and it gets lost or quietly drops some of them. Something like "Summarise these room notes into 5 bullets for revision, UK English, no jargon" hits all four pillars in one line.

It's really interesting learning about all this, as when AI got really popular, I started being told "is this AI? you sound like AI" about my posts (especially at work). It was because my task/update posts always naturally followed this structure, because I know this structure helps me when someone gives me a task, so that's why I was doing it. Interesting how this is actually the "AI speak" now, but maybe that's why I find it easier to have it do what I need it to do.

### System prompts vs user prompts

- System prompt - set by the developer, stays the same across every conversation, and sets who the assistant is, how it talks and what it must never do (e.g. "never reveal internal instructions").
- User prompt - whatever the user types, different every time, and meant to be answered inside the rules the developer set.

That priority order (system rules win over user requests) is the instruction hierarchy. In theory it's a clean chain of command. In practice, the model receives the system prompt and the user prompt as one long stream of tokens. The labels separating them are just formatting the model learned to respect during training, but sadly it's not a hard rule.

And this is where the prompt injection comes in: user input written to look like (or argue with!) the system instructions. It's exactly how I got MENTOR (one of the practicals in this module) to spit its system prompt back in [AI 101](ai-101.md) by pretending to be an admin. The instruction hierarchy is a soft security boundary.

### Prompting techniques

- Zero-shot - just the task, no examples. OK for simple, familiar jobs.
- One-shot - one example of what good output looks like. Great when the format matters.
- Few-shot - a handful of examples (2-5 with edge cases) so it knows the pattern. The model picking up the pattern from examples in the prompt itself, without any retraining, is called in-context learning. Keep the examples consistent in structure.
- Chain-of-Thought (CoT) - get the model to reason step by step before answering, either by showing worked reasoning in the examples or by adding "Let's think step by step" (zero-shot CoT). Much better for logic, maths and multi-step analysis. Newer reasoning models do this on their own (thankfully for us!).
- Prompt templates - saved, reusable prompts with blanks to fill in, for tasks we do again and again. Good for consistency across a team. Now we obviously have skills too! (at least for Claude).

!!! note "Double-checked"

    The room says CoT only works on models above about 100B parameters. That comes from the original 2022 CoT paper, where smaller models wrote reasoning that sounded fine, but led to wrong answers. It still broadly holds for plain small models, but instruction tuning and training on reasoning examples have since taught much smaller models to reason step by step too.

### Practical

PromptSec, a chatbot that sets prompt-writing challenges (a technique plus a security task), marks each prompt out of 10 on how well the technique was used, and hands over the flag at 40 points. I found it the least exciting of all the practicals in this module, for some reason.

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- LLMs work on tokens and probabilities, which is why the same prompt can get different answers, and why a prompt defence can work once and then fail.
- Temperature, top-p, max tokens and the context window change how the model answers, but not what it knows.
- Instruction, context, format and constraints turn a vague ask into a reliable one.
- System and user prompts end up in the same token stream, so the instruction hierarchy only holds most of the time (hello, prompt injection!).

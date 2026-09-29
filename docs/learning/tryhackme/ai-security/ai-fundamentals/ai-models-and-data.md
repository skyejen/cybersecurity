# :material-database-outline: AI Models & Data

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** AI Security > AI Fundamentals > AI Models & Data

:material-calendar-month-outline: **Date:** 18/08/2026

:material-signal-cellular-1: **Difficulty:** Medium (THM) / Easy (me)

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: AI Models & Data](https://tryhackme.com/room/aimodelsdata)

## :material-clipboard-text-outline: What this room covers { data-toc-label="What this room covers" }

The security problems with AI start long before a model is ever deployed. This room covers where training data comes from (and why nobody really knows), what gets baked into a model along the way, what we inherit when we fine-tune someone else's model, and why a trained model is a black box.

## :material-laptop: What I did / learned { data-toc-label="What I did / learned" }

### Where training data comes from

LLMs eat so much text that nobody curates it by hand. Where it's scooped up from:

| Source | Example | Trust level |
|---|---|---|
| Web scraping | Bots hoovering up public websites | Low - nobody checks it, and pages change after they're grabbed |
| Licensed data | Deals with platforms like Reddit | Medium - the people who wrote the posts never signed up for AI training |
| Synthetic data | AI-written text used to train other AI | Depends, and there's more of it every year |
| Internal data | A company's own docs and support chats, for fine-tuning | Higher - the company controls it, but if it leaks or breaks privacy rules, that's on them |

Common Crawl is the giant here: a free, public dump of web crawls that pretty much every big model family has eaten. We only know the exact recipe for a handful of models, GPT-3 being one, and about 60% of its training mix was a cleaned-up Common Crawl. "Cleaned-up" by whom, and how well, is the security question.

### Provenance

Data provenance means knowing a piece of data's backstory: its origin, when it was grabbed, and whether anyone's tampered with it since.

Mostly, nobody can say. Training sets are usually mashups of other training sets, and the origin info falls off along the way. The Data Provenance Initiative audited over 1,800 datasets: the licence was missing for most of them on the big hosting sites, and loads of the ones that did have a licence had the wrong one.

Software security learned this lesson the hard way with SolarWinds (a compromised software update that reached thousands of organisations). The fix there was SBOMs (Software Bill of Materials, an ingredients list for software). AI's version is the ML-BOM: which datasets, which licences, what personal data, what got filtered out. Not many organisations have adopted it yet.

### PII and secrets baked in

Scrape the web at scale and we scrape everything that was public at the time: personal details, medical forum posts, and secrets. Once it's in the weights, there's no real way to get it out. It also clashes with GDPR's data minimisation (only collect what's needed), which is the opposite of "the more data, the better the model".

There's a real example of this. Truffle Security scanned one Common Crawl archive (December 2024, 400TB, 2.67 billion pages) and found about 12,000 live, working API keys and passwords. Models can sometimes be tricked into repeating their training data, so those keys could come back out in a chat. Nobody even had to hack anything, and there's no fix to ship once the model's live.

### Building the model

- Epoch - one full pass of training through the whole dataset. Smaller models usually train over many epochs, but big LLMs often see their data once or not even fully. GPT-3 only got through about 44% of its Common Crawl data during training, so a big chunk of it was never seen at all.
- Overfitting (hello from [AI 101](ai-101.md)!) - keep training past the sweet spot and it starts memorising the examples instead of learning the pattern. That's a security problem too, because memorised data is data that can leak.
- Validation set - a chunk of data held back from training and used to test the model as it goes. If training accuracy keeps going up while validation accuracy stalls or drops, that's overfitting happening in real time. It's the quality gate: skip it and we're left guessing how the model really behaves.
- Pruning - removing parameters that barely matter, to shrink the model.
- Quantisation - storing the weights with less precision (e.g. 8 bits per number instead of 32) so the model is smaller and cheaper to run. The downside is that it can quietly weaken safety behaviour, and backdoor defences tested on the full-size model might miss things in the compressed one. Often done later by a different team, and rarely documented.
- Federated learning - instead of pooling everyone's data in one place, each participant (e.g. a hospital) trains locally and only sends weight updates back. Great for privacy, but any participant can send poisoned updates, and they're hard to spot when everything gets merged. Privacy win, integrity headache.

### Fine-tuning means inheriting baggage

Training from scratch costs millions, so most organisations build on a model somebody else already trained:

- Pre-trained model - already trained on a huge general dataset (e.g. Meta's LLaMA, OpenAI's GPT models).
- Fine-tuning - training it a bit more on a smaller, specific dataset (medical notes, case law...).

Fine-tuning changes the tone, the task and the domain knowledge. It doesn't change the billions of base weights shaped by data we never saw. We inherit all of it:

- Safety alignment erodes. Researchers broke a model's safety training by fine-tuning it on just 10 crafted examples, for under $0.20. Even innocent fine-tuning chipped away at it. Slow erosion.
- Specialised models are easier to attack. Cisco found fine-tuned models fall for prompt injection more easily than the models they started from. Tune a model on finance and an attacker who dresses their prompt up as a finance question gets further.
- Versions matter and nobody tracks them. If the base checkpoint turns out to have a backdoor, every model built on top of it has one too.

Deploying a fine-tuned model means deploying the whole base model underneath it too, flaws included.

### Why we can't just look inside

We can read source code, and even disassemble a binary. Model weights are billions of numbers with no record of why they are the way they are. So trusting a model means trusting the process that made it. Benchmarks and red teaming help, but they only sample behaviour on the inputs we thought of. They can't audit it.

Model cards are meant to fill that gap (a Google research idea from 2019): a document shipped with a model that should cover training data, intended use (and misuse), evaluation results, known limitations, bias assessment and licence. Basically the model's recipe.

In reality they're often vague, incomplete or missing. A thin or missing model card is a red flag: either nobody tested it properly, or they did and didn't want to say.

!!! note "Double-checked"

    The room says nobody has to publish model documentation in most cases. Model cards themselves still are, but the EU AI Act has moved things on for general-purpose AI models: since 2 August 2025, providers placing them on the EU market must keep technical documentation and publish a summary of their training data (using an official EU template), with fines enforceable from August 2026.

### Practical

A model audit on a fake Hugging Face-style repository (a popular site where anyone can upload and share AI models, which is exactly why it's a supply chain risk). The job was to dig through the model card, metadata, files and training info and call out everything dodgy, then get told how bad each find was. The result is basically a checklist for any third-party model: where did it come from, what's it built on, what's missing from the card, and would I let it near production?

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- AI has a supply chain too, it starts with the data, and most organisations can't see any of it.
- Whatever goes into training (PII, live credentials, poisoned data) stays in the weights. There's no patching it out after deployment.
- Fine-tuning inherits everything from the base model, including its problems, and it wears down safety along the way.
- A missing or thin model card is a warning sign. Crossing our fingers and trusting the vendor isn't a security control.

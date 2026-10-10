# :material-magnify-scan: AI Forensics

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** AI Security > AI Fundamentals > AI Forensics

:material-calendar-month-outline: **Date:** 03/09/2026

:material-signal-cellular-1: **Difficulty:** Medium (THM) / Easy (me)

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: AI Forensics](https://tryhackme.com/room/aiforensics)

## :material-clipboard-text-outline: What this room covers { data-toc-label="What this room covers" }

AI in DFIR (Digital Forensics and Incident Response): where it helps, where it falls short, and the legal and ethical mess when AI output ends up as evidence. Plus a hands-on investigation where ML scripts point the way and human judgement does the rest. The courtroom bits were my favourite part.

## :material-laptop: What I did / learned { data-toc-label="What I did / learned" }

### Why DFIR wants AI

Forensics is a lot of data, a tiny number of things that matter, and a clock ticking. AI helps with:

- Processing - transformer models get through huge piles of text in parallel and classify or summarise it way faster than a person.
- Anomaly detection - ML learns what normal looks like for a user, system or network and flags what doesn't fit. Good attackers try to blend in, so this shrinks the haystack.
- Scale - cloud, hybrid and remote setups produce more logs than ever, and AI keeps up without the team needing to grow at the same rate.

Tools already doing this:

| DFIR task | How AI helps | Examples |
|---|---|---|
| Anomaly detection / UEBA (User and Entity Behaviour Analytics) | Learns a baseline of normal behaviour without rules, flags deviations | Splunk UEBA, Elastic ML, Exabeam |
| Phishing and messages | Language models like BERT sort emails as phishing or safe from tone, structure and links | Microsoft Defender for Office 365 |
| Malware classification | Models trained on huge malware collections judge new files from metadata, code and sandbox behaviour | Microsoft Defender, Cylance, VirusTotal |
| Alert triage | Ranks alerts using past incidents and analyst feedback, so the priority ones surface first | Cortex XSOAR/XSIAM, CrowdStrike Charlotte AI |
| Timelines | Clusters and links log events across sources to rebuild what happened in order | Timesketch, Velociraptor |

### Where AI falls short

Forensics needs consistent, repeatable results. AI is probabilistic, so the same evidence could give two slightly different timelines, and a small tweak to a prompt can change the answer a lot. Not great when the output might end up in court.

Measuring a model also takes more than one number. A made-up example to keep it straight in my head: 1,000 emails, 10 of them phishing.

- Accuracy - how often it's right overall. A model that calls every email safe scores 99% and catches nothing, so on lopsided data like this accuracy on its own is useless.
- Precision - of the emails it flagged, how many were really phishing. High precision means fewer false positives to chase.
- Recall - of the 10 real phishing emails, how many it caught. Catching 9 means 90% recall. Flagging everything gets 100% recall and a very annoyed analyst.

Only all three together give a fair picture. Garbage in, garbage out also applies more than ever: a model trained on bad data states wrong conclusions with total confidence. When someone's liberty is on the line, AI can point the way, but a human has to check it.

### Where it's already used

- Images and video - CNNs (convolutional neural networks, which learn visual patterns using small filters that slide across an image) get paired with ELA (Error Level Analysis, which highlights parts of an image with different compression levels, a sign of editing) to spot tampering. A 2024 study reported 94% accuracy. CNNs also show up in deepfake detectors.
- GANs (Generative Adversarial Networks) - two networks trained against each other, one making fakes and one catching them. They're behind better deepfakes and better deepfake detectors at the same time. An arms race with AI on both sides.
- Messages - NLP (natural language processing) models flag phishing and scan chat logs for threats, plus sentiment analysis (working out whether a message sounds angry, scared, upbeat and so on).
- Timelines and behaviour - merging logs, file timestamps and network records into one timeline, and spotting impossible logins (one user in two places at once).
- Malware - classifying files as malicious or safe (Microsoft and Intel's STAMINA research turned files into images so a neural network could judge them), and dynamic analysis, which watches what a program actually does when it runs. One research idea even turns a program's sequence of API calls into an image and classifies that.

### The legal and ethical side

The bit I found most interesting, probably because of my aspiring-police-officer brain.

- Explainability - a lot of models can't explain why they flagged something. In one civil case, an LLM marked emails as suspicious, the other side asked why, nobody could answer, and the evidence got thrown out. In the US, expert and scientific evidence has to pass the Daubert standard (a test of whether the method is reliable and can be scrutinised), and "the model said so" doesn't pass.
- Bias - models learn from historical data, prejudices included. Facial recognition used by police misidentifies Black people and other minorities at much higher rates, and it has led to wrongful arrests in the US. If the defence can show a technique is biased, a judge can exclude it, and investigators have an ethical duty to check for bias in the first place.
- Chain of custody - courts need every step of evidence handling to be traceable. In one case an LLM summarised a suspect's phone data, the intermediate AI outputs weren't logged, and the defence challenged the findings on procedural grounds. Every AI step needs documenting, and on-premises or tightly controlled tools help.
- Privacy - sending evidence to a public cloud AI can expose it to third parties and break laws like GDPR or court orders. Offline tools or federated learning (training locally without moving the data, see [AI Models & Data](ai-models-and-data.md)) help keep it lawful. Evidence gathered unlawfully can end up inadmissible.

!!! note "Double-checked"

    The room mentions at least seven known US wrongful arrests caused by faulty facial recognition. The number has grown since: the ACLU's April 2026 update counts at least 14 publicly known cases.

### Practical

"The Digital Trail", a noir-style investigation for a firmware company called RobbCo. The founder gets woken up about a suspicious late-night login and wants to know whether their crown jewels (proprietary firmware, bootloader and OS source code) were taken.

It starts inside an isolated Python virtual environment, a clean workspace so the tools don't contaminate the evidence. Then two scikit-learn scripts (scikit-learn is an open-source Python ML library) do the first sweep. One was trained on labelled logs and picks out suspicious entries in the auth log. The other scores files in high-value folders on things like name, path, size, entropy (how random the contents look, since encrypted or packed data scores high), permissions and creation time.

After that it's human work, following each flagged artefact to rebuild the attack:

1. Initial access - a phishing email with a fake invoice spreadsheet. Its macro harvested shell history, SSH keys, active sessions and account info, dumped it all in `/tmp` and tried to send it out.
2. Tooling - a hidden dropper that pulled down a second-stage script, and a reverse shell (the victim's machine connecting back to the attacker and handing over a command line) running as the first compromised user.
3. Privilege escalation - no fancy exploit at all. The attacker abused legitimate sudo rights to plant their own SSH key in the founder's account.
4. Persistence - a second reverse shell disguised as a system monitoring tool, with a fake log file created just to make it look legitimate. Sneaky.
5. The theft - the source code compressed, encoded and stashed in shared memory, ready to leave.

My favourite moment: the file script also flagged RobbCo's genuine source code as suspicious. Those files were the stolen goods themselves, nothing malicious about them. A nice reminder that whatever the AI flags is only a lead until a human checks it.

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- AI is brilliant at shrinking the haystack in DFIR: anomaly detection, triage, timelines, phishing and malware.
- Accuracy on its own lies. Precision and recall together tell the real story.
- In court, explainability, bias, chain of custody and privacy decide whether AI-assisted evidence survives at all.
- AI points, humans confirm. The RobbCo lab's false positive proved it.

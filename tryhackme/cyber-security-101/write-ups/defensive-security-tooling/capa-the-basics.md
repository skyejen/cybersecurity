# #️⃣ CAPA: The Basics

**Path:** Cyber Security 101 > Defensive Security Tooling > CAPA: The Basics  
**Date:** 10-12/06/2026  
**Difficulty:** Easy

## 📋 What this room covers

This room focused on a tool called CAPA (Common Analysis Platform for Artifacts). This tool is used to identify capabilities present in an executable file during dynamic and static analysis. The room covered the static analysis specifically.

## 💻 What I did

CAPA can be used to perform an analysis to identify whether a suspicious file is capable of doing something malicious, such as network communications, file manipulation, process injection and other.

In the first task we've gone through helpful commands, learned how to run the tool and initiate a scan in PowerShell. Since the scan takes a long time we were also given an output file to analyse separately which was very thoughtful of the THM team.

After we've done the basics, we covered four sections on analysing the scan results:
- General information, MITRE and MAEC
- Malware behaviour catalogue
- Namespaces
- Capabilities

### General information, MITRE and MAEC

This section dived into the following:
- cryptographic algorithms, type of analysis, OS, etc
- ATT&CK Tactic and ATT&CK Technique information
- MAEC (Malware Attribute Enumeration and Characterization) - specialised language for encoding and communicating malware concerns and details.


### Malware behaviour catalogue

MBC is a catalogue of malware objectives and behaviours and is designed to support malware analysis (labelling, similarity analysis, and standardised reporting). It can also link to ATT&CK methods (naming may be different) and log all behaviours and code features identified during malware analysis.

This section also dived deep into objectives, micro-objectives, MBC behaviours, micro-behaviours and methods.

Objective is an objective of the given malware, some of the covered ones were anti-behavioural analysis (where malware attempts to avoid detection), anti-static analysis (where malware attempts to add complexity to static analysis making it more challenging for the analysists), collection (where malware attempts to identify and gather information on the target machine or network) and many other.

Micro-objectives are associated with micro-behaviours which may be flagged by CAPA, but may not necessarily be malicious grouped by process, memory, communication and data, with the following examples: creating processes, allocating memory, communicating over network, decoding/encoding data and other.

MBC behaviours and micro-behaviours are associated with objectives and micro-objectives correspondingly. Such behaviours are an explanation to an objective and how it can be achieved. For example:
- Micro-objective: PROCESS
- Micro-behaviour: Create Process
- Identifier: C0017
- Explanation: Malware creates a process via WMI or shellcode. It can also create a suspended process.

Methods are tied to behaviours. For example, "ncode data" behaviour can have "Base64" method.

At the end of the theory for this section THM brought it all together. I want to include it for my own reference at a later stage. I'm doing this because reading through all explanations separately was a little challenging, but now having worked through the theory I can understand and explain the table below. Very cool transformation (and a little confidence boost!). So, the table:

| MBC Objective | MBC Behavior |
|---------------|--------------|
| DATA | Encode Data::Base64 [C0026.001] |

Explanation of the result:

| Label | Value | Explanation |
|-------|-------|-------------|
| MBC Objective | DATA | Exhibiting behaviours such as, but not limited to, checking strings, compressing, decoding, and encoding data. |
| MBC Behavior | Encode Data | Malware has the capability to encode data using Base64 and XOR. |
| Method | Base64 | Malware may encode data using Base64. |
| Identifier | C0026.001 | Identifier relays information about a behaviour. This also serves as a tag. |

This means that the given file can use the base64 encoding scheme.


### Namespaces

Namespaces are workspaces that group items by the same purpose. There are Top-Level Namespaces (TLN) and smaller namespaces within each TLN. For example, "anti-analysis" is a TLN which contains a set of rules designed to detect behaviour displayed by malware to avoid analysis (such as obfuscation, packing, and anti-debugging). This TLN can have further namespaces: anti-vm (with vm-detection of different capabilities) and obfuscation, which subsequently can also be broken down into smaller namespaces.

| TLN | Namespace | Rule YAML Files | Explanation |
|-----|-----------|-----------------|-------------|
| Anti-Analysis | anti-vm/vm-detection | reference-anti-vm-strings-targeting-virtualbox.yml, reference-anti-vm-strings-targeting-virtualpc.yml | Contains rules targeting VM environments, identifying strings or patterns used by malware to detect VMs (e.g. VMware-specific registry keys, presence of VMware tools). |
| Anti-Analysis | obfuscation | obfuscated-with-dotfuscator.yml, obfuscated-with-smartassembly.yml | Malware often uses obfuscation to hide its true purpose — string encryption, code obfuscation, packing, and anti-debugging tricks. |

The sweetest thing - the TLN called "nursery" for rules which are still work-in-progress <3

### Capabilities

Pretty much covered above in Namespaces, I guess worth mentioning that capabilities hold the same name as they corresponding .yml files (e.g. "delete file" -> "delete-file.yml")

#### Practical

The practical was a quick overview of CAPA Web Explorer which included uploading a -vv version of CAPA output and going through rules for each triggered namespace. 

## 🔍 What tripped me up

- THM's VM performance was genuinely painful on this one, slow enough to affect the flow of learning.
- The MBC terminology was a lot to take in all at once (objectives, micro-objectives, behaviours, micro-behaviours, methods). It only clicked once THM brought it all together in a summary table at the end (which was a validating experience at the end!).

## 💡 Key takeaways

- CAPA tells you what a file is capable of doing without ever executing it. Static analysis gives you the picture without the risk.
- MBC gives analysts a standardised vocabulary for describing malware behaviour. Instead of everyone describing the same thing differently, there's a shared language. Important for reporting, collaboration and court (and my sanity).
- The hierarchy (objective > behaviour > method > identifier) is how CAPA communicates both the "what" and the "how" of malicious capability.
- Namespaces group detection rules by purpose - the TLN already tells you the category of threat before you've read a single rule.
- The "nursery" namespace for work-in-progress rules is the most endearing thing I've encountered in cybersecurity tooling so far.
- CAPA Web Explorer makes the -vv output actually human-readable. Always use it for reviewing results properly :muscle:



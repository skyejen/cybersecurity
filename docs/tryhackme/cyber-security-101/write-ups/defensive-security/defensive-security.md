# :material-shield-outline: Defensive Security

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** Cyber Security 101 > Defensive Security

:material-calendar-month-outline: **Date:** 03/06/2026

:material-signal-cellular-1: **Difficulty:** Easy

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: Intro to Defensive Security](https://tryhackme.com/room/defensivesecurityintro)
    - [:simple-tryhackme: SOC Fundamentals](https://tryhackme.com/room/socfundamentals)
    - [:simple-tryhackme: Digital Forensics Fundamentals](https://tryhackme.com/room/digitalforensicsfundamentals)
    - [:simple-tryhackme: Incident Response Fundamentals](https://tryhackme.com/room/incidentresponsefundamentals)
    - [:simple-tryhackme: Logs Fundamentals](https://tryhackme.com/room/logsfundamentals)

## :material-clipboard-text-outline: What this module covers { data-toc-label="What this module covers" }

Five rooms covering the defensive side of cybersecurity: Defensive Security Intro, SOC Fundamentals, Digital Forensics Fundamentals, Incident Response Fundamentals, and Logs Fundamentals. Mostly theoretical, but with a small hands-on practical task at the end of each room.

## 🧠 What I learned

Most of this module was theory, which was fascinating to read about. Now some terms and job roles have a clearer meaning in my head when I bump into them online.

**SOC**

A SOC (Security Operations Centre) includes analysts of 3 levels. Level 1 is the first line of defence or triage, they monitor the systems and investigate alerts that come up during their shifts. If they evaluate that an alert needs deeper investigation, they will pass it onto Level 2 analysts. Level 3 in turn, are for escalation for complex investigations. There are other roles within the SOC team: Security Engineers build and maintain tools, Detection Engineers (if there are dedicated ones within a given team) write the detection rules, and, of course, a SOC Manager who runs the team. Reading about this hierarchy definitely improved my understanding of how a SOC team operates.

**Playbooks vs runbooks**

At first it wasn't 100% clear to me, so I had to read up on the distinction. Playbooks are high level generic plan of action, it's a step-by-step guide for each type of incident. While runbooks are the detailed and specific how-tos that provide guidance within the specific environment using the specific tools. The means that a playbook would tell you to isolate the infected machine, while a runbook would guide you which commands to run. Both exist for different stakeholders serving different purposes.

**Digital forensics and write blockers**

The thing that triggered my fascination while learning about digital forensics was write blockers - physical hardware devices that sit between a suspect's drive and the forensic workstation. They block any write commands while letting the workstation read from it. Without one, the moment the OS touches the drive may already be modifying timestamps, metadata, potentially creating files. That evidence is now compromised and potentially inadmissible in court. Such a simple yet elegant physical solution to what could otherwise be a massive problem.

**Logs**

As I'm a big fan of labels, it was absolutely fascinating reading about log types. They each capture a different layer of activity - System logs for OS-level events, Security logs for authentication and access, Application logs for software behaviour, Audit logs for policy and compliance, Network logs for traffic, Access logs for resource requests. The interesting thing is that these overlap deliberately - multiple log types can capture the same event from completely different angles. This overlap builds a fuller picture and is useful in court (and for spotting discrepancies between sources, of course!). Having been working in a very chaotic start-up for the last 2 years I really appreciated such diligence and accuracy.

Some little awesome things I learned from the log-specific practice task:
- Event ID 4624 is a successful logon event - and it fires *constantly* in the background from services and scheduled tasks, not just when a human logs in.
- I somehow still didn't fully understand how piping works in `grep`, now I do! (the file has to go with the first command, not appended to the end of a pipe chain).

## :material-laptop: Practical Tasks { data-toc-label="Practical Tasks" }

Most of the practical tasks were simple concept demonstrations (apart from the last one for logs), but nevertheless it definitely was very exciting. I think it gave me a taste of what I could be doing for a living.

- Defensive Security Intro: acting as a SOC Level 1 analyst and investigating a suspicious alert using a SIEM tool about an unauthorised connection attempt.
- SOC Fundamentals: Similar to the above, but the alert is about a port scanning activity with an additional context provided that needed to be verified.
- Digital Forensics Fundamentals: Investigating a fictional kidnapping using metadata of PDF and jpg files, establishing the file owner as well as the location of where the image was taken.
- Incident Response Fundamentals: Investigating and responding to a phishing email attack in a corporate setting.
- Logs Fundamentals: This room had two practical tasks, both focused on log analysis and finding out required information. The first one was devoted to Windows Event logs while the second one was for a Linux web server.

## :material-magnify: What was new or surprising { data-toc-label="What was new or surprising" }

I expected Event ID 4624 to appear roughly once per user session. So... it does not. Services and scheduled tasks generate logon events constantly, so a real log is full of them (thank god for filtering!).

I also didn't expect SYSTEM to appear as a Security ID rather than a username. Once I understood why (SYSTEM is a built-in account that sits at a lower level than regular user accounts), it made sense - but it's not intuitive at first glance (for me).

The IP address field on a local SYSTEM logon is empty. That field is where remote access shows up. So an empty IP on a 4624 tells you it was local. A populated one should immediately raise questions... Scenarios like this get me proper excited haha

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- Defensive security is a fascinating complex discipline with multiple dimensions. I can't wait to start my SOC Level 1 learning path once I finish this Cybersecurity 101 path.
- Log overlap allows capturing the same event from different angles which is exactly how we can build an airtight evidential picture.
- Write blockers exist because the OS cannot be trusted not to touch the evidence the moment it mounts a drive.
- Playbook = strategy. Runbook = execution. They serve different purposes for different people and complement each other.
- Knowing how to efficiently filter logs is apparently a super power :)
- Digital Forensics and Incident Response makes my heart beat faster :eyes:

# :material-pound: IDS Fundamentals

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** Cyber Security 101 > Security Solutions > IDS Fundamentals

:material-calendar-month-outline: **Date:** 08/06/2026

:material-signal-cellular-1: **Difficulty:** Easy

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: IDS Fundamentals](https://tryhackme.com/room/idsfundamentals)

## :material-clipboard-text-outline: What this room covers { data-toc-label="What this room covers" }

This room was devoted to IDS (Intrusion Detection Systems), its types, purpose and usage. After the general theory, we dived into Snort and also had two practical exercises.

## :material-laptop: What I did / learned { data-toc-label="What I did / learned" }

### General Theory

There was a lot of new and exciting information in this room. I learned that if a firewall is a security guard in a shopping mall, IDS is surveillance cameras.

IDS (Intrusion Detection System) is a security solution that monitors network from within (in case anything gets past the firewall). It can only alert, can't act upon those alerts.

That IDS can be categorised depending on certain factors such as its deployment and detection modes.

When it comes to deployment modes we can group IDS into HIDS (Host Intrusion Detection System) group and NIDS (Network Intrusion Detection System):
- HIDS get installed on each individual host and can be hard to manage in a big organisation and can also be resource-demanding. But it provides detailed visibility over that specific host's activity.
- NIDS monitors the whole network regardless of specific hosts and provides a centralised location to view all detections inside the whole network.

In regard to Detection Modes, we covered these:
- Signature-Based IDS: when a new attack is encountered, this gets logged into IDS database and in future, this IDS would be able to flag this attack based on this attack pattern (called a "signature"). This type of IDS is unable to detect zero-day attacks (something totally new).
- Anomaly-Based IDS: this type of IDS learns the baseline and then flags everything that seems off. The downside is that it may generate a lot of false positive since some legitimate programs can behave similarly to the malicious ones. The amount of false positives can be reduced by manually defining the normal behaviour in the IDS.
- Hybrid IDS: this type of IDS combines methods from signature-based and anomaly-based IDS and uses their methods in the most appropriate situations. As such, for something that's already in IDS database, signature-based IDS methods would be used, while for something new, anomaly-based IDS methods will be utilised.

Typically, signature-based IDS are used for a smaller threat surface, while anomaly-based and hybrid IDS can help with zero-day attacks (which are getting more frequent these days).

### Snort

Snort is apparently one of the most widely used open-source IDS solutions. It was developed in 1998 and uses signature-based and anomaly-based detections to identify and flag threats. Snort comes with pre-built rules, which can already catch some known attacks, the user is able to disable them if they don't fit their organisation's context. Snort allows the creation of custom rules.

Snort has three modes:
- Packet sniffer mode: this mode reads and displays network packets, but doesn't perform any analysis on them. It also allows to display the network traffic on the console or save it in a file. It can be useful, for example, when the team notices network performance issues and they need an insight into the traffic flow.
- Packet logging mode: Snort performs detection on the network traffic in real-time, but sometimes this network traffic needs to be logged for further analysis (for forensic teams, for example). This is where this packet logging mode comes in.
- Network Intrusion Detection System mode: this is the main functionality of Snort - detecting and flagging potential attacks (based on rule files) in real-time.

There was a hands-on practical task in the second section of Snort materials which gave me access to a VM with Snort installed. We went through the components of a rule (action, protocol, source IP/port, destination IP/port, rule metadata), created and tested a "ping detected" alert rule. We also learned how to check historical data (a .pcap file with old network traffic).

### Practical

Don't start me on this task. Honestly. When the brief starts with "you are a third-part forensic investigator" I can't contain myself... Right, I should really keep these write-ups a bit more formal and serious. Where was I?

I needed to run a command to dig into old logs (.pcap file), conduct a log analysis and answer questions.

## :material-magnify: Power through struggle { data-toc-label="Power through struggle" }

- Again, my own brain tripped me up a little bit when I was reading about signature-based IDS, my first question to Claude was - is it like modus operandi? Give me an example :D
- I got so excited running Snort that I tried to ping in the same terminal without switching first. When there was no output I assumed something was wrong, I checked the instructions where they mentioned that my loopback interface may be called somewhere else. I didn't know how to check it (or couldn't remember at the top of my head), so I googled and found the relevant command. I used `ifconfig -a` to verify my loopback interface was correctly named (it was), then I stopped to think and realised I just needed to swap terminals, same as when setting up a port listener (deh).

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- IDS is a crucial security solution that serves as the second line of defence for anything that sneaks past the firewall.
- IDS can be of different types and serve different purposes, signature-based flags known threats and builds a database when encountering something new, anomaly-based knows the baseline and flags anything abnormal, while hybrid uses both. 
- IDS comes with pre-defined rules and also an ability to create custom rules.
- I had a "mind = blown" moment when I saw the extension for snort configuration file... Lua? I only bumped into Lua when I started working in my current company (where we are building a modding platform based on Unreal Engine (C++ & Blueprints) with modding support in Lua). I knew C++ was used outside of games, of course, but I didn't realise Lua was too. Wow.


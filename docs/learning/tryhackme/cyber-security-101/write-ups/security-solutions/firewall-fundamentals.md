# :material-pound: Firewall Fundamentals

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** Cyber Security 101 > Security Solutions > Firewall Fundamentals

:material-calendar-month-outline: **Date:** 07/06/2026

:material-signal-cellular-1: **Difficulty:** Easy

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: Firewall Fundamentals](https://tryhackme.com/room/firewallfundamentals)

## :material-clipboard-text-outline: What this room covers { data-toc-label="What this room covers" }

This room covers the fundamentals of Firewalls, the common types, the components and the concept of directionality, a good chunk of theory on Linux and a practice task on Windows.

## :material-laptop: What I did / learned { data-toc-label="What I did / learned" }

It was absolutely fascinating to learn about firewalls. I know I say this in all my write-ups, but honestly this is just so awesome. I remember being confused about different built-in security tools many moons ago and the more I learn on THM, the clearer it gets. Everything fits in so nicely together and just makes sense. OK, enough with the puppy excitement, so what is it that I learned?

### The Magic of firewall

Firewall is a security solution designed to inspect a network's or a digital device's incoming and outgoing traffic. The way this is achieved is via built-in and custom rules (at a minimum). There are many types of firewalls, which operate on different levels of the OSI model. In that room we covered the four most common ones:

- Stateless (layers 3 & 4): doesn't memorise how decisions were made for previous packages, i.e., if it denied a packet from a source, and then a new packet from the same source is received, this type of firewall will have to rely on the rules to "rethink" and act afresh, without taking into account that this has already been done for a previous packet.
- Stateful (layers 3 & 4): this type of firewall "learns" from the pattern, if they allowed a packet in from a single source, they will allow further packets (within the same connection which will eventually expire for security reasons).
- Proxy (layer 7): hello parental controls (and many other wonderful things)! This type of firewall looks into packets and checks what's inside, this is the feature that allows content filtering.
- Next-Generation (layers 3-7): it is in its name, an absolute beast of a firewall that offers deep packet inspection, intrusion prevention, heuristic analysis, SSL/TLS decryption capabilities and many other wonderful things. Scary! (not... if you are on the side of the good guys)

I also learned about the concept of the traffic directionality. That there are three directionalities, inbound (incoming traffic only), outbound (outgoing) and forward (a forwarder).

### Curiosity leads the way

The coolest thing about this room was that I actually had to create firewall rules and a port forwarder before. At work I needed to set up a locally spun dedicated server for our game which would be accessible to my colleagues outside of my home network. To do that I needed to set up rules to allow inbound TCP connection on a certain port in my PC's firewall and then add a port forwarder in my internet provider's dashboard. I managed to do it back then and it wasn't as challenging as if I had done it before I started learning on THM, but studying the theory behind everything in this specific room actually gave me a fuller understanding of the whys.

Something else that I didn't know was how network profiles kick in. Turned out the firewall (at least on Windows) determines the user's current network based on Network Location Awareness (NLA) and then applies the corresponding profile (private or guest/public a.k.a untrusted network). Pretty exciting if you ask me.

### Linux

Finally some more Linux stuff, this was very interesting as I know very little about Linux still. This section covered Netfilter, ufw, iptables, nftables and firewalld, as well as gave examples of commands on how to check status of the firewall, enable/disable it, set up allow/deny default policies and rules, list all rules and delete rules. The commands are so nice I feel like I'd prefer configuring a Linux firewall to using GUI on Windows hehe.

### Practical task

Windows Defender Firewall: I was given access to a Windows VM with predefined Firewall rules. The task was to navigate Windows Defender Firewall and answer questions about these rules. 

## :material-magnify: Power through struggle { data-toc-label="Power through struggle" }

- My own relentless curiosity tripped me up, mostly for time. Learning about stateful, proxy and NG firewalls specifically brought multiple questions across different scenarios (made up by my brain), I needed to know the answers or I just wouldn't sleep. Anything from "what if an employee initiates a connection to a host with stateful firewall, then gets up and another malicious person uses their PC" and "would proxy/NG firewall decrypt and check all data of low ranking police officers but not someone like high ups in GCQH for a risk of more sensitive and classified data being intercepted".
- The "Rules in Firewalls" section talked about different types of actions with the last one being "forward". I was wondering why I had to set up my game server's forwarder in my internet provider's dashboard instead of using my firewall's rule of this action type. After a little "why" session with Claude I realised that THM was giving an example of, let's say, a commercial office setup, while my home obviously has a consumer router which gets encountered first. So if I had set up the forwarder in my firewall software on my game PC, it would have never reached my PC as my router wouldn't have let it in. Typing this now makes me feel a little silly, but nevertheless it's a good light bulb moment (and maybe a cringe moment a year down the line haha).

Shout out to my mentor Claude for answering numerous questions and "whatif" scenarios, I love gaining understanding so having someone to ask a million times without being afraid to annoy them is truly a gift of the modern time.

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- A firewall is only as good as its rules - and rules only work if you understand the traffic direction, the network context, and what the firewall can and can't see.
- Stateless firewalls are fast but frogetful (🐸). Stateful firewalls learn. Proxy and next-gen firewalls look inside the packet.
- Network profiles aren't manual - Windows determines your network type automatically via NLA and applies the right rules without asking the user.
- The forward action in a firewall only makes sense when the firewall is the edge device. In a home setup, the router gets encountered first - which is why port forwarding lives in the router dashboard, not the PC firewall (for my game server setup).
- Linux firewall configuration via command line is genuinely more transparent than Windows GUI (for me?) - you can see exactly what's happening and why.
- Knowing the why behind something you've already done is learning on a whole new level. Highly recommend :)
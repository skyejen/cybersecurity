# 🍳 CyberChef: The Basics

**Path:** Cyber Security 101 > Defensive Security Tooling > CyberChef: The Basics  
**Date:** 10/06/2026  
**Difficulty:** Easy

## 📋 What this room covers

This room introduced CyberChef - a web-based data transformation tool built and open-sourced by GCHQ. It covers encoding, decoding, encryption, decryption, data format conversion, and how to chain operations together using "recipes".

## 💻 What I did

CyberChef is described as a Swiss Army knife for cybersecurity professionals - a browser-based tool that lets you transform data in hundreds of ways without writing any code. You drag and drop "ingredients" (operations) into a "recipe", feed it input, and get output. The operations cover everything from Base64 encoding to AES decryption to extracting IPs from text.

The room walked through the interface (input, output, recipe panel, operations library) and demonstrated common use cases such as decoding obfuscated strings, extracting data from files, and chaining multiple transformations together in a single recipe. To be honest this tool is so well designed that I felt the walk through was very much redundant. But maybe it's my QA brain! (I tinker with things proactively).

The fact that GCHQ built this and just put it on GitHub for the entire world to use is still something I think about. British signals intelligence, just casually releasing one of the most useful tools in the security community for free.

## 🔍 What tripped me up

How should I say this... My own excitement. I actually had to go for a 5k run just to get it out of my system. The room itself was straightforward - some sections explained things that were obvious from looking at the interface - but the tool itself is genuinely brilliant and I kept stopping to try things that weren't part of the tasks.

## 💡 Key takeaways

- CyberChef is a very user-friendly and empowering tool. Paste in a suspicious encoded string, pick the right operation, and suddenly you can read it!
- Recipes are the real power - chaining multiple transformations means you can handle complex obfuscation in one go rather than doing each step manually (I still want to go back to it to play with it a bit more).
- The "magic" operation that tries to auto-detect encoding is a great starting point when you don't know what you're looking at.
- GCHQ open-sourced this. Just... just stop and think about it for a moment. I can't compute.

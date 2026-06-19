# #️⃣ Hashing Basics

**Path:** Cyber Security 101 > Cryptography > Hashing Basics  
**Date:** 04/04/2026  
**Difficulty:** Easy

## 📋 What this room covers

The fundamentals of hashing - what hash functions are, how they're used in
password verification and file integrity, and how to crack them using hashcat
and rockyou.txt (mostly...).

## 💻 What I did

Tasks 1-3 were straightforward - hashcat, rockyou.txt, correct hash mode, done.

Task 4 kept returning "exhausted" every single time. I went through the
auto-detected candidates methodically - 900, 0, 70, 2600, 3500, 4400, and more.
Exhausted. Exhausted. Exhausted. I was convinced that this way TryHackMe's way to bring the learners back on Earth, as in, perhaps it was a lesson on persistence and patience. That it's not all "Mr Robot". But after trying numerous hashes, I started suspecting I was doing something wrong.

Then I reread the task instructions~~, crossed out 10 years of experience in QA from my CV~~ and noticed something I'd missed: *"for the first three questions, using hashcat along with rockyou.txt is enough."*

The first three. Not four...

Task 4 needed rules - adding `best64.rule` to the command cracked it
immediately. The password was a variation, not a word that exists
verbatim in rockyou.txt.

## 🔍 What tripped me up

Missing one sentence in the instructions cost me a lot of time. The room
explicitly signalled that task 4 was different - I just didn't clock it on the
first read. I guess I was just too excited to do the practical (can you blame me?).

The other thing that tripped me up conceptually: I'd been treating the wordlist
as a fixed list of candidates. Either the password is in there or it isn't.
Rules completely reframe that. They transform each word in the list into dozens
of variations - capitalisation changes, number substitutions, suffixes,
prefixes. The wordlist becomes significantly larger without you adding
a single new word to it.

I felt it was very elegant when I saw it working its magic in practice.

## 💡 Key takeaways

- Contain your excitement while reading the instructions.
- Rules are not optional extra credit - they're what bridges the gap between
  "exhausted" and cracked.
- A wordlist without rules is leaving most of the attack surface untouched.
- Same input always produces the same hash - this is why password reuse is
  genuinely dangerous, not just theoretically dangerous.
- "Exhausted" doesn't mean uncrackable. It means your current approach ran out
  of candidates. Change the approach.

## 🗺️ Concepts worth exploring further

After cracking task 4, I had questions. I always have questions. Rather than
move on immediately, I decided to spend some time on a few things that had come
up during the room and task investigation and felt worth understanding properly.

**Why not just use online lookup databases?**
They work, and they're fast - but they log every hash you submit. If that hash
belongs to a sensitive breach or an active investigation, you've announced
yourself. This is OPSEC (Operational Security) in practice - being deliberate
about what you expose to systems you don't control. In CTFs it's fine. In real
work, cracking offline is not just faster, it's safer. This is so sexy.

**Mask attacks**
Where rules transform wordlist entries, mask attacks let you define the
structure of a password directly - "8 characters, starts uppercase, ends with
two digits". Humans create predictable passwords (Name + year, Word + 123,
Capitalised word + !) and mask attacks are built for exactly that.

**Hash vs HMAC vs encryption**
Three different tools that get conflated constantly. Hashing is one-way - you
verify integrity, you can't reverse it. Encryption is two-way - confidentiality,
requires a key to decrypt. HMAC adds a secret key to the hashing process,
giving you both integrity and authentication. Different problems, different
tools.
# #️⃣ OWASP Top 10 (2025): Insecure Data Handling

**Path:** Cyber Security 101 > OWASP Top 10 (2025) > Insecure Data Handling  
**Date:** 19/06/2026  
**Difficulty:** Easy

## 📋 What this room covers

This is the third of three rooms in the OWASP Top 10 (2025) module. It covers three OWASP categories relating to how applications handle data and dependencies at runtime:

- **A04: Cryptographic Failures** (revisited -> weak cipher angle)
- **A05: Injection**
- **A08: Software or Data Integrity Failures**

## 💻 What I did

### A04: Cryptographic Failures (weak ciphers)

A04 appeared in the previous room too (see [owasp-top-2025-application-design-flaws.md](owasp-top-2025-application-design-flaws.md) for the full breakdown). This time the focus was specifically on homegrown/weak cipher algorithms rather than hardcoded keys.

The practical was a "note sharing" service using a weak XOR cipher with a 4-character key. XOR is reversible, so if you know (or can guess) the key, you can decrypt anything. The key was only 4 characters and the first 3 were given as a hint ("KEY_"). I tried KEY1 first and it worked. All three encrypted notes decrypted instantly, one of them containing the flag.

The lesson is the same as last time, but from a different angle: weak or homegrown algorithms are a gift to attackers. XOR with a short key has a repeating pattern that makes it vulnerable to frequency analysis too, not just brute force.

### A05: Injection

Injection occurs when an application takes user input and passes it directly into something that can execute it - a database, shell, templating engine, or API - instead of treating it as untrusted data. Classic examples include SQL injection, command injection, and Server-Side Template Injection (SSTI). AI prompt injection also now makes the list. It's been on OWASP for years and appears twice in the 2025 list, which tells us everything about how persistent this class of vulnerability is.

Prevention: treat all user input as untrusted. Use prepared statements and parameterised queries for SQL, safe APIs for OS commands (nothing that passes input to a shell directly), and validate/sanitise/escape everything before it touches the application logic.

#### Practical

This practical was specifically SSTI using a Jinja2 template (Python/Flask). The app was using `render_template_string` to directly render raw user input - meaning anything you typed into the payload field got evaluated as a Jinja2 expression on the server. This was quite exciting as last year (or a year before now?) I built a web app (Detective Buggy game!) using Python, Flask and Jinja with SQL. So seeing this practical was quite insightful.

I figured out the first two steps myself:
1. Confirmed code execution with `{{ 7 * 7 }}` - rendered as 49, proving expressions are evaluated
2. Enumerated the context with `{{ config.items() }}` - dumped a big list of Flask config including DEBUG mode, session settings, cookie config, etc.

I tried figuring it out myself, but then realised perhaps more advanced Python knowledge is required which I don't have at the moment. So for step 3 I had a sneaky look at the solution: to read `flag.txt`, you chain through Flask's request object to reach Python's builtins and call `open()`:

```
{{ request.application.__globals__.__builtins__.open('flag.txt').read() }}
```

The chain works because `request.application` exposes Flask internals, `__globals__` gets the module's global namespace, `__builtins__` gets Python's built-in functions, and from there you can call `open()` like normal Python. I wouldn't have arrived at that specific chain without a nudge - it's deep Flask/Python internals knowledge rather than pure SSTI concept knowledge. The concept I fully understand though: user input should never be evaluated as code. The specific exploit chain is something to revisit properly in the dedicated injection module (or when I progress further in my Python studies, which are currently ongoing and going well! :)).

### A08: Software or Data Integrity Failures

Software or Data Integrity Failures occur when an application trusts code, updates, or data without verifying their authenticity or origin. This essentially means loading scripts from untrusted sources, accepting software updates without checksums, or deserializing data without checking whether it's been tampered with. Trust boundaries need to extend into build and deployment pipelines too - CI/CD is an attack surface (my beloved CI/CD!).

The practical demonstrated this via Python's `pickle` module. Serialization is turning a Python object into bytes for storage or transfer. Deserialization is the reverse (I had to read up on that). Pickle's vulnerability is `__reduce__`: a method that tells pickle "when you reconstruct me, call this function with these args". If an attacker crafts an object whose `__reduce__` returns `(eval, ("open('flag.txt').read()",))`, the server executes that code the moment it deserializes the payload.

The exploit flow:
1. Write a Python script that creates a malicious class with `__reduce__` returning the command you want to run
2. Serialize it with `pickle.dumps()` and base64-encode the output
3. Submit that base64 string to the form - the server deserializes it and executes your code

I didn't manage to get my script working (Python gaps, more on that below...), so I used the solution.

## 🔍 What tripped me up

- The A08 practical hit a Python wall I wasn't expecting. I found a script online and adapted it, but couldn't get it working easily - missing imports, wrong structure, and I wasn't fully clear on how `__reduce__` actually hooks into pickle's execution flow. I understand the concept, but my Python skills are lagging behind a bit. Not a big deal as I'm actually doing a very hands-on Python course right now (by Angela Yu) and loving every lesson. I attempted it years ago and it was scary and confusing, now it all makes sense. I guess I gained technical knowledge from CS50x, my work and also confidence that I can dive int and learn too. I didn't have that before.

## 💡 Key takeaways

- Never deserialize untrusted data. Pickle especially - `__reduce__` turns deserialization into arbitrary code execution, and there is no safe way to unpickle (what a cool name!) data you didn't create yourself. Use JSON or YAML with safe_load instead.
- Software integrity failures are broader than just deserialization: unverified updates, unsigned packages, untrusted scripts loaded from CDNs, and compromised CI/CD pipelines are all the same class of problem - us trusting something we shouldn't have.
- SSTI: if user input touches a template engine, we've handed the attacker a code execution interface. `render_template_string(user_input)` is about as dangerous as `eval(user_input)` :skull:.
- XOR with a short key isn't encryption, it's a puzzle with 10 possible answers. The key lesson across all three rooms - "we made our own crypto" is almost always a red flag.
- Python knowledge gaps will show up in cybersecurity faster than I expected. Not a huge blocker as right now I think concepts matter more, plus I'm already working on Python so we are good! :fingerscrossed:

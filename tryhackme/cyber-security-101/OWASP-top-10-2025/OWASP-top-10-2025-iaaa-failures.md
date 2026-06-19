# #️⃣ OWASP Top 10 (2025): IAAA Failures

**Path:** Cyber Security 101 > OWASP Top 10 (2025) > IAAA Failures  
**Date:** 18/06/2026  
**Difficulty:** Easy

## 📋 What this room covers

This is the first of three rooms in the OWASP Top 10 (2025) module. It covers IAAA (Identity, Authentication, Authorisation, and Accountability) - the four pillars of access security - and three OWASP Top 10 (2025) categories where IAAA fails in practice: Broken Access Control (A01), Authentication Failures (A07), and Logging & Alerting Failures (A09).

## 💻 What I did

IAAA stands for Identity, Authentication, Authorisation and Accountability. IAAA is a security principle used to protect systems and data - it ensures only authorised users can access a system and that their actions can be tracked.

The four components must be achieved in order, meaning if the previous component was not completed, we cannot proceed to the next one:
- Identity - a unique account representing a person or a service
- Authentication - proving the identity (passwords, OTP, passkeys)
- Authorisation - permissions for what that identity is allowed to do
- Accountability - recording and alerting who did what, when, and from where

### A01: Broken Access Control

Broken Access Control refers to when the server doesn't properly enforce who can access what on every request. A classic example is IDOR (Insecure Direct Object Reference) - by changing the value of the `id` in the URL, a user can see (horizontal privilege escalation) or edit (vertical privilege escalation) data belonging to someone else.

### A07: Authentication Failures

Authentication Failures refers to an application not being able to reliably establish or bind a user's identity. Most common causes include username enumeration, weak or guessable passwords (with no lockout or rate limits), logic flaws in the login/registration flow, and insecure session or cookie handling.

### A09: Logging & Alerting Failures

Logging & Alerting Failures refers to an application not recording or alerting on security-relevant events, meaning defenders can't detect or investigate attacks. This is tied to the Accountability component of IAAA. Failures can look like missing authentication events, vague error logs, no alerting on brute-force or privilege changes, short retention, or logs stored where attackers can tamper with them.

### Practicals

Each section had a small practical task to illustrate its concept visually. They were very simple, but a lot of fun still!

## 🔍 What tripped me up

Nothing significant in this room - the concepts clicked and the practicals were straightforward. The real head-scratching happened in the rooms that followed...

## 💡 Key takeaways

- IAAA is sequential and the order is not arbitrary. You can't authorise someone you haven't authenticated, and you can't authenticate someone who hasn't identified themselves.
- Broken Access Control (A01) is ranked #1 in OWASP consistently because it's everywhere - any time a server assumes "if you can see the page, you must be allowed to" rather than checking permissions on every single request.
- IDOR is deceptively simple: just change a number in a URL. The fix is equally simple too: verify the requesting user owns that resource. It is indeed simple, yet it keeps appearing in real systems.
- Authentication failures aren't always about weak passwords. No rate limiting, no lockout, and poor session handling can be just as exploitable even with a strong password.
- Without logging, defenders are blind. An attacker who acts in an unlogged system effectively doesn't exist (in the context of an investigation).
- Accountability without the other three is meaningless - if identity and authentication aren't solid, your logs are faithfully recording the wrong person.

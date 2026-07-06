# :material-pound: OWASP Top 10 (2025): Application Design Flaws

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** Cyber Security 101 > OWASP Top 10 (2025) > Application Design Flaws

:material-calendar-month-outline: **Date:** 18-19/06/2026

:material-signal-cellular-1: **Difficulty:** Easy

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: TryHackMe Room](https://tryhackme.com/room/owasptopten2025one)

## :material-clipboard-text-outline: What this room covers { data-toc-label="What this room covers" }

This is the second of three rooms in the OWASP Top 10 (2025) module. It covers four OWASP categories relating to failures in application architecture and design - where the vulnerability isn't always a bug in the code itself, but a flaw in how the system was conceived, configured, or built:

- **AS02: Security Misconfigurations**
- **AS03: Software Supply Chain Failures**
- **AS04: Cryptographic Failures**
- **AS06: Insecure Design**

It was an absolutely fascinating room and I really enjoyed it, I loved how the conclusion tied it all up nicely at the end. You cannot add security at the end and expect it to work. Strong systems start with clear security requirements, realistic threat assumptions, controlled configurations, verified dependencies, and strong cryptographic choices. Treat everything with suspicion (#trustno1)

## :material-laptop: What I did { data-toc-label="What I did" }

### AS02: Security Misconfigurations

Security misconfigurations are not code bugs - they are mistakes in how an environment, software, or network was set up, which open doors for attackers. Even a small misconfiguration can expose sensitive data, enable privilege escalation, or give attackers a foothold into the system.

> The common patterns and prevention methods below are kept very close to source material. This is intentionaly and I found them super useful and wanted to keep them for myself for reference as almost like checklists.

**Common patterns:**
- Default or weak credentials left in place
- Unnecessary services or endpoints exposed
- Misconfigured cloud storage or permissions
- Unrestricted API access or missing authentication/authorisation
- Verbose error messages exposing system details
- Outdated software, frameworks, or containers with known vulnerabilities
- Exposed AI/ML endpoints without proper access controls

**Prevention methods:**
- Harden default configurations
- Remove unused features or services
- Enforce strong authentication and least privilege across all systems
- Limit network exposure and segment sensitive resources
- Keep everything up-to-date
- Hide sensitive information from error messages
- Audit cloud and permission configurations
- Secure AI endpoints and automation services with proper access controls and monitoring
- Integrate configuration reviews and automated security checks into the deployment pipeline

#### Practical

The practical task included a web page for a User Management API which I needed to investigate for security misconfigurations. It turned out the user ID field wasn't limited to numeric values - it also accepted "admin" (and with no authentication required). Changing the ID to "admin" returned debug info including the flag.

### AS03: Software Supply Chain Failures

Software supply chain failures occur when an application relies on components, libraries, services, or models that are compromised, outdated, or improperly verified. This allows attackers to exploit these weak links to inject malicious code, bypass security, or steal sensitive data - meaning one compromised dependency can compromise an entire system. In the modern world of third-party packages, APIs, and AI models, this is especially important. Supply chain attacks can be automated, which makes them hard to detect and very dangerous.

Nowadays this can be observed with AI - using unverified third-party models or fine-tuned datasets can include hidden behaviours, backdoors, or biased outputs that compromise systems or leak data.

> Common patterns and prevention methods kept as a reference checklist (see note in AS02 above).

**Common patterns:**
- Using unverified or unmaintained libraries and dependencies
- Automatically installing updates without verification
- Over-reliance on third-party AI models without monitoring or auditing
- Insecure build pipelines or CI/CD processes that allow tampering
- Poor licence or provenance tracking for components
- Lack of monitoring for vulnerabilities in dependencies after deployment

**Prevention methods:**
- Verify all third-party components, libraries, and AI models before use
- Monitor and patch dependencies regularly
- Sign, verify, and audit software updates and packages
- Lock down CI/CD pipelines and build processes to prevent tampering
- Track provenance and licensing for all dependencies
- Implement runtime monitoring for unusual behaviour from dependencies or AI components
- Integrate supply chain threat modelling into the SDLC, including testing, deployment, and update workflows

#### Practical

For this practical I was given Python code of an app, and access to this app being hosted on the web. The brief was that the app had outdated code and imported an old component. I reviewed the code and noticed that when a POST request is made with `debug` value in the `data` field:

```bash
curl -i -X POST -H 'Content-Type: application/json' -d '{"data": "debug"}' http://10.129.166.201:5003/api/process
```

... it returns hardcoded sensitive information such as an admin token, internal secret, and the flag!

### AS04: Cryptographic Failures

Cryptographic failures occur when encryption is not used, or used incorrectly - weak algorithms, hard-coded keys, poor key handling, or unencrypted sensitive data. This can lead to violation of privacy and confidentiality, exposure of sensitive data, and breaches.

These vulnerabilities can be exploited through man-in-the-middle attacks, brute-force attacks on weak keys, or by finding secrets that were not stored and handled securely.

> Common patterns and prevention methods kept as a reference checklist (see note in AS02 above).

**Common patterns:**
- Using deprecated or weak algorithms
- Hard-coded secrets in code or configuration (like in the practical below!)
- Poor key rotation or management practices
- Lack of encryption for sensitive data at rest or in transit
- Self-signed or invalid TLS certificates
- Using AI/ML systems without proper secret handling for model parameters or sensitive inputs

**Prevention methods:**
- Use strong and modern algorithms, enforce TLS 1.3 with valid certificates
- Use secure key management services
- Rotate secrets and keys regularly at defined crypto periods
- Document and enforce policies and SOPs for key lifecycle management
- Maintain a complete inventory of certificates, keys, and their owners
- Ensure AI models and automation agents never expose unencrypted secrets or sensitive data

#### Practical

This practical was fascinating. They gave a web page mentioning a PDF document that was encrypted (alongside its encryption code), but that the decryption functionality was unavailable. The brief hinted there was a vulnerability to exploit to decrypt the file and get the flag.

I used Firefox DevTools to dig around and found a `decrypt.js` script in a hidden location. I curled it:

```bash
curl -i http://10.129.166.201:5004/static/js/decrypt.js
```

The secret key was hardcoded in the configuration field. I also spotted they used AES in ECB mode - AES is deprecated in this context, and ECB mode is an insecure practice on top of that. With the encrypted document and the hardcoded secret key, I googled a decryption script, recreated it on the VM, and ran it. Getting the flag was very satisfying!

### AS06: Insecure Design

Insecure design occurs when flawed logic or architecture is built into the system from the start. This happens due to skipped threat modelling, no design requirements or reviews, or accidental errors. This risk has increased with the introduction of AI, where developers often assume that models are safe, correct, or predictable and that their generated code is flaw-free, but in reality it often leads to poor architectural patterns.

Insecure design cannot be patched, it's built into the workflow, logic, and trust boundaries. It therefore requires rethinking and redesigning how systems work and interact with each other (and with AI).

> Common patterns and prevention methods kept as a reference checklist (see note in AS02 above).

**Common insecure designs in 2025:**
- Weak business logic controls, like recovery or approval flows
- Flawed assumptions about user or model behaviour
- AI components with unchecked authority or access
- Missing guardrails for LLMs and automation agents
- Test or debug bypasses left in production
- No consistent abuse-case review or AI threat modelling
- With AI specifically, prompt injection can be extremely dangerous - user input mixed with system prompts allows attackers to hijack context or extract hidden data. Blind trust in AI output, especially for poisoned models pulled from unverified sources or fine-tuned on unsafe data, can embed hidden behaviours or backdoors that compromise the system from within

**Prevention methods:**
- Treat every model as untrusted until proven otherwise
- Validate and filter all model inputs and outputs to ensure accuracy and integrity
- Separate system prompts from user content
- Keep sensitive data out of prompts unless absolutely needed and protect it with strict controls
- Require human review for high-risk AI actions
- Log model provenance, monitor behaviour, and apply differential privacy for sensitive data
- Include AI-specific threat modelling for prompt attacks, inference risks, agent misuse, and supply chain compromise throughout the design process
- Build threat modelling into every stage of development, not just at the start
- Define clear security requirements for each feature before implementation
- Apply the principle of least privilege across users, APIs, and services
- Ensure proper authentication, authorisation, and session management across the system
- Keep dependencies, third-party components, and supply chain sources verified and up to date
- Continuously monitor and test the system for logic flaws, abuse paths, and emergent risks as new features or AI components are added

#### Practical

The practical included a web page for a mobile-only messaging app instructing users to download a mobile app. The task brief hinted that the "mobile-only" assumption wasn't very secure. I tried lots of different things including following most common `/api` paths, inspecting the web page source code, sending GET and POST requests with adjusted `User-Agent` headers to simulate mobile access, even mobile device mode in DevTools. Nothing worked. Only to discover that I got discouraged with common paths too quickly - while `/api` and `/users` both returned 404... `/api/users` worked :skull:. No authentication required, full user list exposed. After that, `/api/messages/admin` handed me the flag.

## :material-magnify: What tripped me up { data-toc-label="What tripped me up" }

- In the AS02 practical (User Management API), the landing page had `GET /api/user/123` hardcoded and I could access it without any authentication. But I was struggling to get the flag - the only hint was "It appears that the developers left too many traces in their User Management APIs". I looked through request/responses, tried accessing other users, tried the terminal. Then I realised I had blindly trusted the landing page saying "ID accepts numeric values"." Changing it to "admin" gave me debug info including the flag. Not sure how I missed it - my shift was starting in 15 minutes, brain already half in work mode. Live and learn... (...to take a pause).
- Remember I just said I need to learn to take a pause? Well I didn't. I got so excited in the AS03 practical that I missed a huge "DOWNLOAD FILES" button and was looking for the script everywhere else. Got there eventually :D
- In the AS04 practical I initially thought I'd need to run the JS script to decrypt the document. After looking through the code multiple times I realised the script wasn't there to be executed, it was planted so I'd find the hardcoded secret key. Once it clicked, the rest was a breeze!
- The AS06 practical (insecure design) gave me a lot to scratch my head about, as described in the practical section above. Lesson: don't assume that if a parent root returns 404, child endpoints within that root won't work... especially when the whole point is design flaws.

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- Security misconfigurations aren't "bugs" - they're more of setup mistakes. But they're just as dangerous (or more?). Default credentials and exposed endpoints are gifts to attackers.
- "ID accepts numeric values" is not a security control. Trusting the frontend to enforce input constraints is insecure design in itself (I'm honestly still surprised at myself). Always validate server-side. Always.
- Supply chain attacks target your dependencies, not your code. One compromised or outdated package can compromise everything downstream, including via AI models fine-tuned on unsafe data.
- Hard-coded secrets are a gift to anyone who bothers to check. Found in JS files, config files, debug endpoints - anywhere they shouldn't be. Always use a secrets manager.
- AES-ECB being deprecated matters - it's not just the algorithm name you need to check, it's the mode. ECB is deterministic and pattern-preserving, which makes it weak.
- Insecure design cannot be patched. You can't bolt security onto a fundamentally flawed architecture, it has to be rethought from the ground up. Is it bad that the concept of redesigning a working application with security in mind makes me very excited?
- `/api` returning 404 doesn't mean child endpoints are also 404. Gotta enumerate properly before giving up on a path.
- The mobile app frontend is decoration if the API behind it has no authentication. The "security" was an assumption, which is a classic insecure design.

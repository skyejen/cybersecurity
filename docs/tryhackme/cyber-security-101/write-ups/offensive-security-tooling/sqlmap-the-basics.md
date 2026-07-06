# :material-pound: SQLMap: The Basics 

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** Cyber Security 101 > Offensive Security Tooling > SQLMap: The Basics

:material-calendar-month-outline: **Date:** 21/05/2026

:material-signal-cellular-1: **Difficulty:** Easy

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: SQLMap: The Basics](https://tryhackme.com/room/sqlmapthebasics)

## :material-clipboard-text-outline: What this room covers { data-toc-label="What this room covers" }

This room covered SQL injection vulnerabilities, how they can be exploited and introduced me to SQLMap, an automation tool for detecting and exploiting SQL injection vulnerabilities.

## :material-laptop: What I did / learned { data-toc-label="What I did / learned" }

I learned the following:
- websites with databases can be vulnerable to SQL injections
- this occurs when there is no user input validation and sanitisation or when there is only validation on client side (easy to work around it), an example of this can be injecting "' OR 1=1;-- -" in a database query
- SQL injections can be done via GET and POST requests (although POST method was out of scope for this room, sadly!)
- this can be attempted manually, but it can also be automated by a tool called SQLMap (which also conveniently has a --wizard flag for some help with the setup)
- there are lots of flags to help with enumeration and exploitation, the main ones as --dbs (to get databases' names), --tables (to get all tables' names), --dump to get info from tables themselves and so on
- SQLMap also allows you to import files (for POST request exploitation)
- solved a practice task!

## :material-magnify: Power through struggle { data-toc-label="Power through struggle" }

I'm at my cybersecurity journey where everything is very exciting and I'm now gaining a little bit of confidence to try and solve things by myself instead of relying on instructions to guide me. I attempted to solve this practice task myself and the fact that I needed a GET URL for SQLMap to work and I only had the login form available made me scratch my head a little.

I did end up figuring it out: The login form itself sent a POST request, but the actual vulnerable endpoint was a GET URL with parameters that weren't visible in the browser address bar. I used Firefox devtools Network tab to intercept the request and extract the full URL including parameters.

I then ran several commands, first enumerating the website and obtaining the number of databases it's linked to, then obtaining names of a specific database and finally, checking the output of one of the tables to find a password to the test user account.

After I completed this task I went back to read the full instructions and saw they confirmed this was the way to go. That was quite encouraging!

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- I have tested API endpoints for validation in a work setting before, but it was my first experience to being on the offensive side. It was really great seeing the implications and damage that SQL injection can do from this angle
- SQLMap seems to be a fantastic tool with beginner friendly wizard setup and automation support for time-consuming tasks
- Not to get discouraged when I have a POST form and I need a GET URL^^
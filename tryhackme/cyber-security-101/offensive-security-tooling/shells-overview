# #️⃣ Shells Overview

**Path:** Cyber Security 101 > Offensive Security Tooling > Shells Overview
**Date:** 26/05/2026
**Difficulty:** Easy

## 📋 What this room covers

This room covered different kinds of shells such as reverse, bind and web shells, and how they can be used to exploit vulnerable websites.

## 💻 What I did

The practice task consisted of two subtasks, one was for either reverse or bind shell. The other was for a web shell.

The first task presented a web page of a server which had a command injection vulnerability, which I needed to exploit to get access to a shell. I chose a reverse shell as I find this concept fascinating and wanted to practise a bit more. I set up a listener on my AttackBox and then using the input box on the vulnerable website, I executed the command for the web server to connect to my AttackBox where my listener was set up. This worked because the vulnerable web page wasn't sanitising the input, so I could run my command.

In the second task I was presented with a web page where I could upload a file. This web server was vulnerable to malicious files being uploaded. I created a new file, added a PHP shell script and uploaded it to the server. I executed my commands using the URLs (GET + keyword format).

I then used the URL to execute commands on the web server to find my flag.

## 🔍 What tripped me up

### Task 1
- A rookie mistake incoming!.. So... the website was hosted on 8081 so I somehow assumed I needed to listen on that same port. The logic made sense intuitively (?) but obviously the reverse shell needs its own separate listener port that has nothing to do with the web app port. The web app port (8081) was where the vulnerable site lived. And my listener port (4444 in the end) was where the target machine phoned home to. Two completely different things, yet my overexcited mind mashed them into one. Won't happen again though!
- When the web server connected to my machine, I noticed the tty error which I had to research first. It turned out that the shell wasn't fully interactive but it still worked for what I needed it for (getting my flag!).

### Task 2
- When I tried executing my commands using the URLs (GET + keyword format) at first it didn't work. I then realised that my file was missing .php extension so it would have never been picked up as a executable script by the vulnerable web server (rookie mistake!) so once I fixed that, it all worked like magic.
- Another thing to mention is that I didn't realise the web shell doesn't maintain state between requests, so I couldn't get any result when I was using cat command on my flag after cd-ing into the required directory. Once I figured that out I used the full path and it all worked.

## 💡 Key takeaways

- Vulnerable websites can be exploited in numerous ways using shell, including a command injection as well as an unrestricted file upload
- Be mindful of extensions and file naming conventions when dealing with shell and scripts in general
- Web shell doesn't maintain state between requests
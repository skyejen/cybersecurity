# :material-pound: Ninja Skills

<div class="sj-meta" markdown>

:material-shield-star-outline: **Path:** Ninja Skills

:material-calendar-month-outline: **Date:** 04-05/07/2026

:material-signal-cellular-1: **Difficulty:** Easy (THM) / Easy (me)

</div>

---

!!! quicklinks "Quick Links"

    - [:simple-tryhackme: TryHackMe Room](https://tryhackme.com/room/ninjaskills)

## :material-clipboard-text-outline: What this room covers { data-toc-label="What this room covers" }

This room gave file names for 12 files and asked me to find answers to 6 questions (group owner, IP address inside files, hash, word count, owner ID and permissions)

## :material-laptop: What I did / learned { data-toc-label="What I did / learned" }

This room, I think, was meant to be done manually. But I've been doing some script-adjacent work (AI-assisted) at work and the second I saw the task, I thought - this would be a great opportunity to learn about `bash` scripting. I have an amazing colleague who agreed to mentor me for DevOps tasks, and he really wants me to learn, rather than to "help" fully relying on AI (he has a good heart!), so I thought this could be a part of my "homework" too

I started with manually researching all commands to be able to answer all questions and then I reached to Claude for scripting support

---

### Version 1

??? note "Script"

    ```bash
    #!/bin/bash

    for file in 8V2L bny0 c4ZX D8B3 FHl1 oiMO PFbD rmfX SRSq uqyw v2Vb X1Uy; do
        file_location=$(find / -iname "$file" 2>/dev/null)
        echo "=== $file ==="
        ls -la "$file_location"
        sha1sum "$file_location"
        wc -l "$file_location"
        grep -oP '([0-9]{1,3}\.){3}[0-9]{1,3}' "$file_location"
        echo
    done > file_check.txt
    ```

??? note "Output"

    ```console
    [new-user@ip-10-129-128-198 ~]$ cat file_check.txt
    === 8V2L ===
    -rwxrwxr-x 1 new-user new-user 13545 Oct 23  2019 /etc/8V2L
    0323e62f06b29ddbbe18f30a89cc123ae479a346  /etc/8V2L
    209 /etc/8V2L

    === bny0 ===

    === c4ZX ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /mnt/c4ZX
    9d54da7584015647ba052173b84d45e8007eba94  /mnt/c4ZX
    209 /mnt/c4ZX

    === D8B3 ===
    -rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /mnt/D8B3
    2c8de970ff0701c8fd6c55db8a5315e5615a9575  /mnt/D8B3
    209 /mnt/D8B3

    === FHl1 ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/FHl1
    d5a35473a856ea30bfec5bf67b8b6e1fe96475b3  /var/FHl1
    209 /var/FHl1

    === oiMO ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/oiMO
    5b34294b3caa59c1006854fa0901352bf6476a8c  /opt/oiMO
    209 /opt/oiMO
    1.1.1.1

    === PFbD ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/PFbD
    256933c34f1b42522298282ce5df3642be9a2dc9  /opt/PFbD
    209 /opt/PFbD

    === rmfX ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /media/rmfX
    4ef4c2df08bc60139c29e222f537b6bea7e4d6fa  /media/rmfX
    209 /media/rmfX

    === SRSq ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /etc/ssh/SRSq
    acbbbce6c56feb7e351f866b806427403b7b103d  /etc/ssh/SRSq
    209 /etc/ssh/SRSq

    === uqyw ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/log/uqyw
    57226b5f4f1d5ca128f606581d7ca9bd6c45ca13  /var/log/uqyw
    209 /var/log/uqyw

    === v2Vb ===
    -rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /home/v2Vb
    7324353e3cd047b8150e0c95edf12e28be7c55d3  /home/v2Vb
    209 /home/v2Vb

    === X1Uy ===
    -rw-rw-r-- 1 newer-user new-user 13545 Oct 23  2019 /X1Uy
    59840c46fb64a4faeabb37da0744a46967d87e57  /X1Uy
    209 /X1Uy
    ```

??? note "Observations"

    - This script doesn't show user IDs so I can't answer one of the questions
    - I'm missing information for one file
    - There is a lot of redundancy there
    - Formatting could be improved

---

### Version 2

??? note "Script"

    ```bash
    #!/bin/bash

    for file in 8V2L bny0 c4ZX D8B3 FHl1 oiMO PFbD rmfX SRSq uqyw v2Vb X1Uy; do
        file_location=$(find / -iname "$file" 2>/dev/null)
        echo "=== $file ==="
        ls -la "$file_location"
        owner=$(ls -la "$file_location" | awk '{print $3}')
        id -u "$owner"
        sha1sum "$file_location"
        wc -l "$file_location"
        grep -oP '([0-9]{1,3}\.){3}[0-9]{1,3}' "$file_location"
        echo
    done > file_check.txt
    ```

??? note "Output"

    ```text
    === 8V2L ===
    -rwxrwxr-x 1 new-user new-user 13545 Oct 23  2019 /etc/8V2L
    501
    0323e62f06b29ddbbe18f30a89cc123ae479a346  /etc/8V2L
    209 /etc/8V2L

    === bny0 ===

    === c4ZX ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /mnt/c4ZX
    501
    9d54da7584015647ba052173b84d45e8007eba94  /mnt/c4ZX
    209 /mnt/c4ZX

    === D8B3 ===
    -rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /mnt/D8B3
    501
    2c8de970ff0701c8fd6c55db8a5315e5615a9575  /mnt/D8B3
    209 /mnt/D8B3

    === FHl1 ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/FHl1
    501
    d5a35473a856ea30bfec5bf67b8b6e1fe96475b3  /var/FHl1
    209 /var/FHl1

    === oiMO ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/oiMO
    501
    5b34294b3caa59c1006854fa0901352bf6476a8c  /opt/oiMO
    209 /opt/oiMO
    1.1.1.1

    === PFbD ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/PFbD
    501
    256933c34f1b42522298282ce5df3642be9a2dc9  /opt/PFbD
    209 /opt/PFbD

    === rmfX ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /media/rmfX
    501
    4ef4c2df08bc60139c29e222f537b6bea7e4d6fa  /media/rmfX
    209 /media/rmfX

    === SRSq ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /etc/ssh/SRSq
    501
    acbbbce6c56feb7e351f866b806427403b7b103d  /etc/ssh/SRSq
    209 /etc/ssh/SRSq

    === uqyw ===
    -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/log/uqyw
    501
    57226b5f4f1d5ca128f606581d7ca9bd6c45ca13  /var/log/uqyw
    209 /var/log/uqyw

    === v2Vb ===
    -rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /home/v2Vb
    501
    7324353e3cd047b8150e0c95edf12e28be7c55d3  /home/v2Vb
    209 /home/v2Vb

    === X1Uy ===
    -rw-rw-r-- 1 newer-user new-user 13545 Oct 23  2019 /X1Uy
    502
    59840c46fb64a4faeabb37da0744a46967d87e57  /X1Uy
    209 /X1Uy
    ```

??? note "Observations"

    - Doing it step-by-step, so got my user IDs for one of the questions
    - Spoke to Claude to scout info on optimisation and he said that the file path mentioned 3 times is not really a redundancy, as in, that's how commands work. We could strip it, but it's just cosmetic. Since I'm going to try and make it formatted better I'm going to disregard this one for now
    - He did point out that we are running `ls -la` twice and suggested an optimisation for that, that made total sense and was very cool

---

### Version 3

??? note "Script"

    ```bash
    #!/bin/bash

    for file in 8V2L bny0 c4ZX D8B3 FHl1 oiMO PFbD rmfX SRSq uqyw v2Vb X1Uy; do
        file_location=$(find / -iname "$file" 2>/dev/null)
        echo "=== $file ==="
        ls_output=$(ls -la "$file_location")
        echo "$ls_output"
        owner=$(echo "$ls_output" | awk '{print $3}')
        id -u "$owner"
        sha1sum "$file_location"
        wc -l "$file_location"
        grep -oP '([0-9]{1,3}\.){3}[0-9]{1,3}' "$file_location"
        echo
    done > file_check.txt
    ```

??? note "Observations"

    - Output is the same, but we are not running the same command for the same files twice, so happy times
    - Next stop - formatting!

---

### Version 4

??? note "Script"

    ```bash
    #!/bin/bash

    for file in 8V2L bny0 c4ZX D8B3 FHl1 oiMO PFbD rmfX SRSq uqyw v2Vb X1Uy; do
        file_location=$(find / -iname "$file" 2>/dev/null)
        echo "=== $file ==="
        ls_output=$(ls -la "$file_location")
        echo "file info: $ls_output"
        owner=$(echo "$ls_output" | awk '{print $3}')
        echo "owner ID: $(id -u "$owner")"
        echo "sha1 hash: $(sha1sum "$file_location")"
        echo "word count: $(wc -l "$file_location")"
        echo "IP: $(grep -oP '([0-9]{1,3}\.){3}[0-9]{1,3}' "$file_location")"
        echo
    done > file_check.txt
    ```

??? note "Output"

    ```text
    === 8V2L ===
    file info: -rwxrwxr-x 1 new-user new-user 13545 Oct 23  2019 /etc/8V2L
    owner ID: 501
    sha1 hash: 0323e62f06b29ddbbe18f30a89cc123ae479a346  /etc/8V2L
    word count: 209 /etc/8V2L
    IP:

    === bny0 ===
    file info:
    owner ID:
    sha1 hash:
    word count:
    IP:

    === c4ZX ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /mnt/c4ZX
    owner ID: 501
    sha1 hash: 9d54da7584015647ba052173b84d45e8007eba94  /mnt/c4ZX
    word count: 209 /mnt/c4ZX
    IP:

    === D8B3 ===
    file info: -rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /mnt/D8B3
    owner ID: 501
    sha1 hash: 2c8de970ff0701c8fd6c55db8a5315e5615a9575  /mnt/D8B3
    word count: 209 /mnt/D8B3
    IP:

    === FHl1 ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/FHl1
    owner ID: 501
    sha1 hash: d5a35473a856ea30bfec5bf67b8b6e1fe96475b3  /var/FHl1
    word count: 209 /var/FHl1
    IP:

    === oiMO ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/oiMO
    owner ID: 501
    sha1 hash: 5b34294b3caa59c1006854fa0901352bf6476a8c  /opt/oiMO
    word count: 209 /opt/oiMO
    IP: 1.1.1.1

    === PFbD ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/PFbD
    owner ID: 501
    sha1 hash: 256933c34f1b42522298282ce5df3642be9a2dc9  /opt/PFbD
    word count: 209 /opt/PFbD
    IP:

    === rmfX ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /media/rmfX
    owner ID: 501
    sha1 hash: 4ef4c2df08bc60139c29e222f537b6bea7e4d6fa  /media/rmfX
    word count: 209 /media/rmfX
    IP:

    === SRSq ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /etc/ssh/SRSq
    owner ID: 501
    sha1 hash: acbbbce6c56feb7e351f866b806427403b7b103d  /etc/ssh/SRSq
    word count: 209 /etc/ssh/SRSq
    IP:

    === uqyw ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/log/uqyw
    owner ID: 501
    sha1 hash: 57226b5f4f1d5ca128f606581d7ca9bd6c45ca13  /var/log/uqyw
    word count: 209 /var/log/uqyw
    IP:

    === v2Vb ===
    file info: -rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /home/v2Vb
    owner ID: 501
    sha1 hash: 7324353e3cd047b8150e0c95edf12e28be7c55d3  /home/v2Vb
    word count: 209 /home/v2Vb
    IP:

    === X1Uy ===
    file info: -rw-rw-r-- 1 newer-user new-user 13545 Oct 23  2019 /X1Uy
    owner ID: 502
    sha1 hash: 59840c46fb64a4faeabb37da0744a46967d87e57  /X1Uy
    word count: 209 /X1Uy
    IP:
    ```

??? note "Observations"

    - Claude and I explored two ways to format this, add labels or a table. Labels seemed easier for a quick dopamine boost (and a tidy up session) - `echo "label: $(command)"`. This was pretty cool and looks great. I wanted to try a table too, but now thinking that I'd rather polish this output as I prefer it (?)
    - I'd like to chop the last two instances of the `path` (coming from the hash and word count commands) and put "N/A" for IP entry that don't have any value there
    - I also want to rename file_check to file-check, I don't know why I put an underscore there and it annoys me now

---

### Version 5

??? note "Script"

    ```bash
    #!/bin/bash

    for file in 8V2L bny0 c4ZX D8B3 FHl1 oiMO PFbD rmfX SRSq uqyw v2Vb X1Uy; do

        # Find all files and save their location in a variable file_location
        file_location=$(find / -iname "$file" 2>/dev/null)

        # Add a separator with the file name when printing each file block
        echo "=== $file ==="

        # Save output of ls command into the ls_output variable so we could use it in two places
        ls_output=$(ls -la "$file_location")

        # Print out the ls_output (we need to explicitly echo it as we saved it in a variable above)
        echo "file info: $ls_output"

        # Using the ls_output variable we just created, save the third value from its output into owner variable
        owner=$(echo "$ls_output" | awk '{print $3}')

        # Print out owner ID with a label
        echo "owner ID: $(id -u "$owner")"

        # Print out hash with a label and remove the file path to avoid unnecessary clutter in the terminal/file
        echo "sha1 hash: $(sha1sum "$file_location" | awk '{print $1}')"

        # Do the same for word count
        echo "word count: $(wc -l "$file_location" | awk '{print $1}')"

        # Look for an IP in a file, if found, print it out, if not, print "N/A"
        ip=$(grep -oP '([0-9]{1,3}\.){3}[0-9]{1,3}' "$file_location")
        echo "IP: ${ip:-N/A}"
        echo
    done > file-check.txt
    ```

??? note "Output"

    ```text
    === 8V2L ===
    file info: -rwxrwxr-x 1 new-user new-user 13545 Oct 23  2019 /etc/8V2L
    owner ID: 501
    sha1 hash: 0323e62f06b29ddbbe18f30a89cc123ae479a346
    word count: 209
    IP: N/A

    === bny0 ===
    file info:
    owner ID:
    sha1 hash:
    word count:
    IP: N/A

    === c4ZX ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /mnt/c4ZX
    owner ID: 501
    sha1 hash: 9d54da7584015647ba052173b84d45e8007eba94
    word count: 209
    IP: N/A

    === D8B3 ===
    file info: -rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /mnt/D8B3
    owner ID: 501
    sha1 hash: 2c8de970ff0701c8fd6c55db8a5315e5615a9575
    word count: 209
    IP: N/A

    === FHl1 ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/FHl1
    owner ID: 501
    sha1 hash: d5a35473a856ea30bfec5bf67b8b6e1fe96475b3
    word count: 209
    IP: N/A

    === oiMO ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/oiMO
    owner ID: 501
    sha1 hash: 5b34294b3caa59c1006854fa0901352bf6476a8c
    word count: 209
    IP: 1.1.1.1

    === PFbD ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/PFbD
    owner ID: 501
    sha1 hash: 256933c34f1b42522298282ce5df3642be9a2dc9
    word count: 209
    IP: N/A

    === rmfX ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /media/rmfX
    owner ID: 501
    sha1 hash: 4ef4c2df08bc60139c29e222f537b6bea7e4d6fa
    word count: 209
    IP: N/A

    === SRSq ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /etc/ssh/SRSq
    owner ID: 501
    sha1 hash: acbbbce6c56feb7e351f866b806427403b7b103d
    word count: 209
    IP: N/A

    === uqyw ===
    file info: -rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/log/uqyw
    owner ID: 501
    sha1 hash: 57226b5f4f1d5ca128f606581d7ca9bd6c45ca13
    word count: 209
    IP: N/A

    === v2Vb ===
    file info: -rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /home/v2Vb
    owner ID: 501
    sha1 hash: 7324353e3cd047b8150e0c95edf12e28be7c55d3
    word count: 209
    IP: N/A

    === X1Uy ===
    file info: -rw-rw-r-- 1 newer-user new-user 13545 Oct 23  2019 /X1Uy
    owner ID: 502
    sha1 hash: 59840c46fb64a4faeabb37da0744a46967d87e57
    word count: 209
    IP: N/A
    ```

??? note "Observations"

    - This looks so much nicer! I can see how I could pass this "report" to someone else (rather than just a plain output)
    - I know it's probably going overboard, but I'd like to split "file info" into "permissions" and "path" (I'm somehow treating this now as a "polish the report for a stakeholder" task now haha)
    - I'd also like to put "Not found" for the file we are missing

---

### Version 6

??? note "Script"

    ```bash
    #!/bin/bash

    {

        echo
        echo "==================== OUTPUT: $0 ===================="
        echo

        for file in 8V2L bny0 c4ZX D8B3 FHl1 oiMO PFbD rmfX SRSq uqyw v2Vb X1Uy; do

            # Find all files and save their location in a variable file_location
            file_location=$(find / -iname "$file" 2>/dev/null)

            # Add a separator with the file name when printing each file block
            echo "=== $file ==="

            # If file is not found, print "file not found" instead
            if [ -z "$file_location" ]; then
                echo "- file not found"
                echo
                continue
            fi

            # Save output of ls command into the ls_output variable so we could use it in multiple places
            ls_output=$(ls -la "$file_location")

            # Save permissions from ls_output in a new variable "permissions"
            permissions=$(echo "$ls_output" | awk '{print $1}')

            # Print out permissions
            echo "- permissions: $permissions"

            # Save file path from ls_output in a new variable "file_path"
            file_path=$(echo "$ls_output" | awk '{print $9}')

            # Print out file path
            echo "- file path: $file_path"

            # Using the ls_output variable we just created, save the third value from its output into owner variable
            owner=$(echo "$ls_output" | awk '{print $3}')

            # Print out owner ID with a label
            echo "- owner ID: $(id -u "$owner")"

            # Print out hash with a label and remove the file path to avoid unnecessary clutter in the terminal/file
            echo "- sha1 hash: $(sha1sum "$file_location" | awk '{print $1}')"

            # Do the same for word count
            echo "- word count: $(wc -l "$file_location" | awk '{print $1}')"

            # Look for an IP in a file, if found, print it out, if not, print "N/A"
            ip=$(grep -oP '([0-9]{1,3}\.){3}[0-9]{1,3}' "$file_location")
            echo "- IP: ${ip:-N/A}"
            echo

        done
    } > file-check.txt
    ```

??? note "Output"

    ```console
    [new-user@ip-10-128-164-120 ~]$ cat file-check.txt

    ==================== OUTPUT: script.sh ====================

    === 8V2L ===
    - permissions: -rwxrwxr-x
    - file path: /etc/8V2L
    - owner ID: 501
    - sha1 hash: 0323e62f06b29ddbbe18f30a89cc123ae479a346
    - word count: 209
    - IP: N/A

    === bny0 ===
    - file not found

    === c4ZX ===
    - permissions: -rw-rw-r--
    - file path: /mnt/c4ZX
    - owner ID: 501
    - sha1 hash: 9d54da7584015647ba052173b84d45e8007eba94
    - word count: 209
    - IP: N/A

    === D8B3 ===
    - permissions: -rw-rw-r--
    - file path: /mnt/D8B3
    - owner ID: 501
    - sha1 hash: 2c8de970ff0701c8fd6c55db8a5315e5615a9575
    - word count: 209
    - IP: N/A

    === FHl1 ===
    - permissions: -rw-rw-r--
    - file path: /var/FHl1
    - owner ID: 501
    - sha1 hash: d5a35473a856ea30bfec5bf67b8b6e1fe96475b3
    - word count: 209
    - IP: N/A

    === oiMO ===
    - permissions: -rw-rw-r--
    - file path: /opt/oiMO
    - owner ID: 501
    - sha1 hash: 5b34294b3caa59c1006854fa0901352bf6476a8c
    - word count: 209
    - IP: 1.1.1.1

    === PFbD ===
    - permissions: -rw-rw-r--
    - file path: /opt/PFbD
    - owner ID: 501
    - sha1 hash: 256933c34f1b42522298282ce5df3642be9a2dc9
    - word count: 209
    - IP: N/A

    === rmfX ===
    - permissions: -rw-rw-r--
    - file path: /media/rmfX
    - owner ID: 501
    - sha1 hash: 4ef4c2df08bc60139c29e222f537b6bea7e4d6fa
    - word count: 209
    - IP: N/A

    === SRSq ===
    - permissions: -rw-rw-r--
    - file path: /etc/ssh/SRSq
    - owner ID: 501
    - sha1 hash: acbbbce6c56feb7e351f866b806427403b7b103d
    - word count: 209
    - IP: N/A

    === uqyw ===
    - permissions: -rw-rw-r--
    - file path: /var/log/uqyw
    - owner ID: 501
    - sha1 hash: 57226b5f4f1d5ca128f606581d7ca9bd6c45ca13
    - word count: 209
    - IP: N/A

    === v2Vb ===
    - permissions: -rw-rw-r--
    - file path: /home/v2Vb
    - owner ID: 501
    - sha1 hash: 7324353e3cd047b8150e0c95edf12e28be7c55d3
    - word count: 209
    - IP: N/A

    === X1Uy ===
    - permissions: -rw-rw-r--
    - file path: /X1Uy
    - owner ID: 502
    - sha1 hash: 59840c46fb64a4faeabb37da0744a46967d87e57
    - word count: 209
    - IP: N/A
    ```

??? note "Observations"

    - I think we are done. What a difference between V1 and V6!

## :material-magnify: Power through struggle { data-toc-label="Power through struggle" }

### Bash Syntax and Its Possibilities
- The main "struggle" was syntax and knowing bash's possibilities. I've never really used bash before and I don't have much scripting experience at all. I started this room yesterday as I was a bit down that my THM score was still at 34 (for ages), and this room was recommended. I knew I needed to get more comfortable with terminal work and I was waiting for Claude Opus to work on my other stuff so in between waiting for him to respond I was doing this room
- I couldn't finish it last night as I ran out of time and my wonderful boyfriend already prepared dinner. So before bed time and this morning I spent some time on my phone doing a "Bash Scripting" room on THM, it was super basic but I think it helped a little bit
- I was relieved to know logic wasn't the hardest part, it's more like "how do I actually do it in bash", but that was also interesting to learn

### Jen vs Claude
- Had a few fights with Claude. Some were him pushing back to me asking him to help with scripting, I found it frustrating at first as he is supposed to "let me struggle" (and poke with direction if super stuck) only with cybersecurity and Python studies (we have a pact - no AI, I have to do everything myself), but I haven't done bash scripting before and I was basically starting from 0. I only really wanted to see the possibilities, but Claude was pushing back and making me do most of the work myself. TBH when I saw the outcome I was grateful. I won't be able to write it from scratch myself again, but maybe with Google!
- I noticed some errors that were printing to the terminal when I was running `bash` command on my script, those were related to the file we couldn't find (bny0). When we added `{}` (or so I thought), those were gone. I kept asking Claude why it happened and he kept almost gaslighting me (lol) that these errors never happened. That was such a crazy experience as he was basically telling me "no you are wrong", I eventually reran the old version of the script and showed him, and that's when we had a chat and he talked me through it. Mental!

## :material-lightbulb-on-outline: Key takeaways { data-toc-label="Key takeaways" }

- Probably best not to jump straight into scripting (before getting comfortable with commands themselves), especially for rooms that are supposed to be for manual training. Saying that, I think I'm a bit more comfortable with commands and using terminal now too
- If you are running a command, it would naturally print the result. If you are saving the output of that command into a variable, you need to explicitly run `echo`. Sounds mega silly, it's so obvious and I wouldn't have thought twice if I was doing something else with Python etc, but for some reason here it tripped me, so adding it here (for the world to see lol)
- It's super easy to tidy up the output, for labels, you can do this: `echo "label: $(command)"` or `echo "label: $variable"`
- Similarly, you can clean up output of a command (if you don't want the whole thing), by using `awk` in this way, for example: `permissions=$(echo "$ls_output" | awk '{print $1}')` (and then you'd need to `echo` it, of course)
- Be careful not to run the same operations more than once, run it once and save the output into a variable (and then butcher it as you see fit)
- Syntax is still going to be a bit of a struggle until I get used to it
- I enjoyed this more than I thought I would!

## :material-star-outline: Bonus! { data-toc-label="Bonus!" }

??? note "Claude's Wisdom"

    **stdout vs stderr**

    Every command in Linux has two output streams: **stdout** (standard output) and **stderr** (standard error). stdout is where normal output goes — the result of a command working as expected. stderr is where error messages go — things like "file not found" or "permission denied."

    By default, both streams print to the terminal, which is why they look the same when you're watching output scroll past. But they are separate, and you can redirect them independently.

    `>` only captures stdout. So when you did `done > file-check.txt`, all the normal output went into the file, but the errors from missing files (`ls: cannot access`, `sha1sum: no such file`) went to stderr and straight to your terminal, bypassing the redirect entirely.

    `2>/dev/null` redirects stderr (stream 2) to `/dev/null`, which is a black hole — it discards everything sent to it. That's why `find / -iname "$file" 2>/dev/null` silently swallows "permission denied" errors from directories you can't access.

    If you wanted to capture both stdout and stderr into a file, you'd use `2>&1`:

    ```bash
    done > file-check.txt 2>&1
    ```

    This means "redirect stderr (2) to wherever stdout (&1) is going."

    **The if check**

    ```bash
    if [ -z "$file_location" ]; then
        echo "- file not found"
        echo
        continue
    fi
    ```

    `[ -z "$file_location" ]` checks whether the variable is empty (zero length). If `find` comes back with nothing — because the file doesn't exist or can't be found — `$file_location` is an empty string. The `-z` flag returns true when that's the case.

    `continue` skips the rest of the current loop iteration and jumps straight to the next file. Without it, all the commands below (`ls -la`, `sha1sum`, etc.) would run with an empty path and produce the "no such file" errors you were seeing before. The `if` check catches the problem early and exits cleanly instead.

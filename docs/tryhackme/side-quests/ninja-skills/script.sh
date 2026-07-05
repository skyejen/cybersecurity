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
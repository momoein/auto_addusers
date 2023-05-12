#!/bin/bash

# Check if the script is being run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" >&2
   exit 1
fi

# Read the usernames and passwords from a text file
while read -r line; do
   username=$(echo "$line" | cut -d':' -f1)
   password=$(echo "$line" | cut -d':' -f2)
   
   # Check if the user exists
   if id "$username" >/dev/null 2>&1; then
      # Change the user's password
      echo "username:newpassword" | chpasswd
      echo "Password for user $username changed"
   else
      echo "User $username does not exist, skipping..."
   fi
done < passwords.txt

echo "Done."


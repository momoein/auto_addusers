#!/bin/bash

# Check if the script is being run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" >&2
   exit 1
fi

# Read the usernames from a text file
usernames=$(cat users.txt)

# Loop through the usernames and create user accounts
for username in $usernames; do
   # Check if the user already exists
   if id "$username" >/dev/null 2>&1; then
      echo "User $username already exists, skipping..."
   else
      # Create the user account
      useradd -m "$username"
      echo "User $username created"
   fi
done

echo "Done."


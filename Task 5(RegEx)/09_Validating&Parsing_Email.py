# Task_05 Q_09:
# A valid email address meets the following criteria:
# It's composed of a username, domain name, and extension assembled in this format: username@domain.extension
# The username starts with an English alphabetical character, and any subsequent characters consist of one or more of the following: alphanumeric characters, -,., and _.
# The domain and extension contain only English alphabetical characters.
# The extension is 1, 2, or 3 characters in length.

# Given n pairs of names and email addresses as input, print each name and email address pair having a valid email address on a new line.

# Input Format
# The first line contains a single integer,n, denoting the number of email address.
# Each line i of the n subsequent lines contains a name and an email address as two space-separated values following this format:

import re
import email.utils
n = int(input("Enter the number of email addresses: "))

for i in range(n):
    name, email = input().split()
    patt="<[a-z][a-zA-Z0-9\-\.\_]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>"
    if bool(re.match(patt, email)):
        print(name,email)
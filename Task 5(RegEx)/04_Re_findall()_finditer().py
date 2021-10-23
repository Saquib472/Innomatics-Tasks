# Task_05 Q_04:
# You are given a string s. It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of s that contains 2 or more vowels.
# Also, these substrings must lie in between 2 consonants and should contain vowels only.

# Note :
# Vowels are defined as: AEIOU and aeiou.
# Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

import re
patt = re.compile(r"(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])", re.IGNORECASE)
matches = patt.findall(input())
if matches:
    print("\n".join(matches))
else:
    print(-1)

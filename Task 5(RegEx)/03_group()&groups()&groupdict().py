# Task_05 Q_03:
# You are given a string s.
# Your task is to find the first occurrence of an alphanumeric character in s (read from left to right) that has consecutive repetitions.

import re
patt = re.compile(r'([a-zA-Z0-9])\1+')
matches = patt.search(input())
if matches:
    print(matches.group(1))
else:
    print(-1)
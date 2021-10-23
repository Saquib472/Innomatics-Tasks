# Task_05 Q_05:
# You are given a string s.
# Your task is to find the indices of the start and end of string k in s.

import re
s = input()
k = input()
patt = re.compile(r'(?=('+k+'))')
matches = patt.finditer(s)
findm = False
for match in matches:
    findm = True
    print((match.start(1), match.end(1) - 1))
if findm==False:
    print((-1,-1))
#Task_05 Q_06:
# You are given a text of  lines. The text contains && and || symbols.
# Your task is to modify those symbols to the following: && → and , || → or

import re
def replace(match):
    if match.group(1) =="&&":
        return 'and'
    else:
        return 'or'
n = int(input())
for i in range(n):
    print(re.sub(r"(?<= )(\|\||&&)(?= )", replace,input()))
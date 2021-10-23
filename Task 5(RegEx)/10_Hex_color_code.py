# Task_05 Q_10:
# CSS colors are defined using a hexadecimal (HEX) notation for the combination of Red, Green, and Blue color values (RGB).
# Specifications of HEX Color Code:
# It must start with a '#' symbol.
# It can have 3 or digits 6.
# Each digit is in the range of 0 to F. ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, A, B, C, D, E and F).
# A - F letters can be lower case. (a, b, c, d, e and f are also valid digits).
# You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

import re
n = int(input())
inside = False
for i in range(n):
    st = input()    
    if '{' in st:
        inside = True
    elif '}' in st:
        inside = False
    elif inside:        
        for color in re.findall('#[0-9a-fA-F]{3,6}', st):
            print(color)
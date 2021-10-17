# Task_3 Q_2:
# You are given the lengths AB and BC.
# Your task is to find THE ANGLE OF MBC in degrees.

# Input Format
# The first line contains the length of side AB.
# The second line contains the length of side BC.

import math
a = int(input())
b = int(input())
M = math.sqrt(a**2+b**2)
theta = math.acos(b/M )
print(str(round(math.degrees(theta)))+ '\N{DEGREE SIGN}')

# Task_3 Q_3:
# Read in two integers, a and b, and print three lines.
# The first line is the integer division a//b.
# The second line is the result of the modulo operator: a%b.
# The third line prints the divmod of a and b.

from __future__ import division
a = int(input())
b = int(input())

print (a // b)
print (a % b)
print (divmod(a,b))
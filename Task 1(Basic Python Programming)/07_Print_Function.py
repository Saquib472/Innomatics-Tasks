# Task1 Q7:
# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following: 123...n
# Note that "..." represents the consecutive values in between.

n = int(input("Enter an integer:"))
strr = ''
for i in range(1,n+1):
    strr = strr+str(i)
print(strr)
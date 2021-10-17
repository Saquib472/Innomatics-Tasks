# Task_3 Q_7:
# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size N is:
# 1
# 121
# 12321
# 1234321
# 123454321

for i in range(1,int(input())+1):
    print((10**i//9)**2 )
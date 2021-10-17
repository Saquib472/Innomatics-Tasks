# Task_4 Q_9:
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:
# Mat size must be X. ( is an odd natural number, and  is  times .)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------

N, M = map(int, input().split())
d = ".|."
for i in range(N//2):
    print((d*i).rjust(M//2-1,'-') + d + (d*i).ljust(M//2-1,'-'))
print("WELCOME".center(M,'-'))
for j in range(N//2+2,N+1):
    print((d*(N-j)).rjust(M//2-1,'-') + d + (d*(N-j)).ljust(M//2-1,'-'))
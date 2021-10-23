# Task_06 Q_12:
# You are given a 2-D array of size NXM.
# Your task is to find:
# The mean along axis 1
# The var along axis 0
# The std along axis 

# Input Format :
# The first line contains the space separated values of N and M.
# The next N lines contains M space separated integers.

import numpy
N,M = map(int,input().split())
A = numpy.array([input().split() for i in range(N)], int)
print(A.mean(axis=1))
print(A.var(axis=0))
print(A.std(axis=None))
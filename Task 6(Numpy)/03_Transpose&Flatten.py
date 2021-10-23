# Task_06 Q_03:
# You are given a NXM integer array matrix with space separated elements (N = rows and M = columns).
# Your task is to print the transpose and flatten results.

# Input Format
# The first line contains the space separated values of N and M.
# The next N lines contains the space separated elements of M columns.

import numpy
n,m=map(int,input().split())

M=[list(map(int,input().split())) for i in range(n)]
my_array=numpy.array(M)

print(numpy.transpose(my_array))
print(my_array.flatten())
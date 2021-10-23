# Task_06 Q_04:
# You are given two integer arrays of size NxP and MxP (N & M are rows, and P is the column). Your task is to concatenate the arrays along axis 0.

# Input Format
# The first line contains space separated integers N, M and P.
# The next N lines contains the space separated elements of the P columns.
# After that, the next M lines contains the space separated elements of the P columns.

import numpy
p, n, m = map(int,input().split())
arr1 = numpy.array([input().split() for i in range(p)],int)
arr2 = numpy.array([input().split() for i in range(n)],int)
print(numpy.concatenate((arr1, arr2), axis = 0))

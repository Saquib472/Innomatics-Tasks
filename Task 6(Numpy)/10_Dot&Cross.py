# Task_06 Q_10:
# You are given two arrays A and B. Both have dimensions of NXN.
# Your task is to compute their matrix product.

# Input Format :
# The first line contains the integer N.
# The next N lines contains N space separated integers of array A.
# The following N lines contains N space separated integers of array B.

import numpy
n=int(input())
a = numpy.array([input().split() for i in range(n)],int)
b = numpy.array([input().split() for i in range(n)],int)
res = numpy.dot(a,b)
print (res)
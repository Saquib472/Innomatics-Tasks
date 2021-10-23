# Task_06 Q_13:
# You are given two arrays: A and B.
# Your task is to compute their inner and outer product.
# Input Format :
# The first line contains the space separated elements of array A.
# The second line contains the space separated elements of array B. 

import numpy
A = numpy.array(input().split(), int)
B = numpy.array(input().split(), int)
print(numpy.inner(A, B))
print(numpy.outer(A, B))

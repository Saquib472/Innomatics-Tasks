# Task_06 Q_15:
# You are given a square matrix A with dimensions NXN. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

# Input Format :
# The first line contains the integer N.
# The next N lines contains the N space separated elements of array A.

import numpy
N=int(input())
A=numpy.array([input().split() for i in range(N)],float)
numpy.set_printoptions(legacy='1.13')
print(numpy.linalg.det(A))
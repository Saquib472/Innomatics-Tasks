# Task_06 Q_08:
# You are given a 1-D array, A. Your task is to print the floor, celi and rint of all the elements of A.

import numpy

numpy.set_printoptions(sign=' ')

A = numpy.array(input().split(),float)
print(numpy.floor(A))
print(numpy.ceil(A))
print(numpy.rint(A))
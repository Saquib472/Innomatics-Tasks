# Task_06 Q_11:
# You are given a 2-D array with dimensions NXM.
# Your task is to perform the min function over axis 1 and then find the max of that.
# Input Format :
# The first line of input contains the space separated values of N and M.
# The next N lines contains M space separated integers. 

import numpy
N, M = map(int, input().split())
st = numpy.array([input().split() for _ in range(N)],int)
output = numpy.min(st, axis=1)
final_output = numpy.max(output, axis=0)
print(final_output)
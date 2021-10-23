# Task_06 Q_02:
# You are given a space separated list of nine integers. Your task is to convert this list into a 3X3 NumPy array.

import numpy
arr = input().strip().split()
my_array = numpy.array(arr,int)
print(numpy.reshape(my_array,(3,3)))
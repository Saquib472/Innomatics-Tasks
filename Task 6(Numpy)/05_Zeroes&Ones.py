# Task_06 Q_05:
#You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

import numpy

shape = tuple(map(int, input().split()))
print(numpy.zeros(shape, int))
print(numpy.ones(shape, int))
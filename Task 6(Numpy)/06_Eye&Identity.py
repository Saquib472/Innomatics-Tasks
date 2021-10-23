# Task_06 Q_06:
# Your task is to print an array of size NxM with its main diagonal elements as 1's and 0's everywhere else.

import numpy
numpy.set_printoptions(sign=' ')
n,m = map(int, input().split())
print(numpy.eye(n,m))
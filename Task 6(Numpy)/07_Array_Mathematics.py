# Task_06 Q_07:
# You are given two integer arrays, A and B of dimensions NxM.
# Your task is to perform the following operations:
# Add (A + B)
# Subtract (A - B)
# Multiply (A * B)
# Integer Division (A / B)
# Mod (A % B)
# Power (A ** B)

import numpy

N, M = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for n in range(N)])
B = numpy.array([list(map(int, input().split())) for n in range(N)])

print(numpy.add(A, B))
print(numpy.subtract(A, B))
print(numpy.multiply(A, B))
print(A//B)
print(numpy.mod(A, B))
print(numpy.power(A, B))

# Task_4 Q_10:
# Given an integer, n, print the following values for each integer i from 1 to n:
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

# print_formatted has the following parameters:
# int number: the maximum value to print

# Prints
# The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.

def print_formatted(number):
    for i in range(1, number + 1):
        width = len(f"{number:b}")
        print(f"{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
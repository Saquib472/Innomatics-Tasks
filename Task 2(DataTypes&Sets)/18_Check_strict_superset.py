# Task_2 Q_18:
# You are given a set A and n other sets.
# Your job is to find whether set A is a strict superset of each of the N sets.
# Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
# A strict superset has at least one element that does not exist in its subset.

# Input Format
# The first line contains the space separated elements of set A.
# The second line contains integer n, the number of other sets.
# The next n lines contains the space separated elements of the other sets.

A = set(map(int, input().split()))
for _ in range(int(input())):
    X = set(map(int, input().split()))
    if A.issuperset(X) != True or len(A) == len(X): 
        print(False)
        break 
else: print(True)
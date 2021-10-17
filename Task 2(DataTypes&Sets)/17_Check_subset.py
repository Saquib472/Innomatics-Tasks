# Task_2 Q_17:
# You are given two sets, A and B.
# Your job is to find whether set A is a subset of set B.
# If set A is subset of set B, print True.
# If set A is not a subset of set B, print False.

# Input Format
# The first line will contain the number of test cases, T.
# The first line of each test case contains the number of elements in set A.
# The second line of each test case contains the space separated elements of set A.
# The third line of each test case contains the number of elements in set B.
# The fourth line of each test case contains the space separated elements of setB .

def checker():
    x = int(input())
    s1 = set(map(int, input().split()))
    y = int(input())
    s2 = set(map(int, input().split()))
    l = []
    for i in s1:
        if i in s2:
            l.append(i)
    l = set(l)
    if l == s1:
        print(True)
    else:
        print(False)

T = int(input())
for i in range(T):
    checker()
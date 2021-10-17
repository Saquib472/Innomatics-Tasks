# Task_2 Q_9:
# Given  sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
# Input Format
# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer,N .
# The fourth line contains N space-separated integers.

M = int(input())
m = set(map(int, input().split()))
N = int(input())
n = set(map(int, input().split()))
mdeff = m.difference(n)
ndeff = n.difference(m)
f_out = mdeff.union(ndeff)
for i in sorted(list(f_out)):
    print(i)
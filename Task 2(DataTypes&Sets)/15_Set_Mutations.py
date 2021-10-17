# TASK_2 Q_15:
# You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.
# Your task is to execute those operations and print the sum of elements from set A.

# Input Format
# The first line contains the number of elements in set A.
# The second line contains the space separated list of elements in set A.
# The third line contains integer N, the number of other sets.
# The next 2*N lines are divided into N parts containing two lines each.
# The first line of each part contains the space separated entries of the operation name and the length of the other set.
# The second line of each part contains space separated list of elements in the other set.

A = int(input())
Aset = set(map(int, input().split()))
N = int(input())
for i in range(N):
    ip = input().split()
    if ip[0] == 'intersection_update':
        Bset = set(map(int, input().split()))
        Aset.intersection_update(Bset)
    elif ip[0] == 'update':
        Bset = set(map(int, input().split()))
        Aset.update(Bset)
    elif ip[0] == 'symmetric_difference_update':
        Bset = set(map(int, input().split()))
        Aset.symmetric_difference_update(Bset)
    elif ip[0] == 'difference_update':
        Bset = set(map(int, input().split()))
        Aset.difference_update(Bset)
    else:
        print("Enter a valid operation")
print(sum(Aset))
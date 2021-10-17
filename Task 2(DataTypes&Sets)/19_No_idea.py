# Task_2 Q_19:
# There is an array of n integers. There are also 2 disjoint sets, A and B, each containing m integers. You like all the integers in set A and dislike all the integers in set B. Your initial happiness is 0. For each i integer in the array, if i in A, you add 1 to your happiness. If i in B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

n,m = list(map(int,input().split()))
happiness = 0
arr = list()
A,B = set(),set()

arr = list(map(int,input().strip().split()))
A = set(map(int,input().strip().split()))
B = set(map(int,input().strip().split()))

for i in arr:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)
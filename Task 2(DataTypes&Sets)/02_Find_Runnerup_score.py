# Task_2 Q_2:
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

n = int(input("Enter the number of integers: "))
arr = list(set(map(int, input("Enter the "+str(n)+" integers values following by spaces: ").split())))
arr.sort()
print(arr[-2])
# Task_2 Q_13:
# The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
# You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed only English newspaper.

# Input Format
# The first line contains an integer, n, the number of students who have subscribed to the English newspaper.
# The second line contains n space separated roll numbers of those students.
# The third line contains b , the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.

n = int(input("Enter the number of student who have subscribed for the English Newspaper: "))
nr = set(map(int, input("Enter the Roll numbers of those students(space-separeted): ").split()))
b = int(input("Enter the number of student who have subscribed for the French Newspaper: "))
br = set(map(int, input("Enter the roll numbers of those students(space-separeted): ").split()))
res = nr.difference(br)
count = 0
for i in range(len(res)):
    count+=1
print("The total number of students who have subscribed only English newspaper: ",count)
# Task_2 Q_10:
# Apply your knowledge of the .add() operation to help your friend Rupal.
# Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
# Find the total number of distinct country stamps.

N = int(input("enter the total number of country: "))
s = set()
count = 0
print("Enter the country names: ")
for i in range(N):
    s.add(input())
print(len(s))
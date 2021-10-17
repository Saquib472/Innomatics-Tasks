#Task_2 Q_10:
# You have a non-empty set s, and you have to execute n commands given in n lines.
# The commands will be pop, remove and discard.

# Input Format
# The first line contains integer n, the number of elements in the sets s.
# The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer N, the number of commands.
# The next N lines contains either pop, remove and/or discard commands followed by their associated value.

n = int(input())
s = set(map(int, input().split()))
for x in range(int(input())):
  op = input().split()
  if op[0] == "remove":
    s.remove(int(op[1]))
  elif op[0] == "discard":
    s.discard(int(op[1]))
  else:
    s.pop()
print(sum(s))   


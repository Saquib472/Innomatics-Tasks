# Task_2 Q_5:

# Consider a list (list = []). You can perform the following commands:
# insert i e: Insert integer e at position i.
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer e at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

N = int(input())
Output = []
for i in range(N):
    ip = input().split()
    if ip[0] == "print":
        print(Output)
    elif ip[0] == "insert":
        Output.insert(int(ip[1]), int(ip[2]))
    elif ip[0] == "remove":
        Output.remove(int(ip[1]))
    elif ip[0] == "pop":
        Output.pop()
    elif ip[0] == "append":
        Output.append(int(ip[1]))
    elif ip[0] == "sort":
        Output.sort()
    else:
        Output.reverse()

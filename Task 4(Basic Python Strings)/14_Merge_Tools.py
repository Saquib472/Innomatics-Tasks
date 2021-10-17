# Task_4 Q_14:
# Function Description
# Complete the merge_the_tools function in the editor below.

# merge_the_tools has the following parameters:
# string s: the string to analyze
# int k: the size of substrings to analyze

# Prints
# Print each subsequence on a new line. There will be n/k of them. No return value is expected.

# Input Format
# The first line contains a single string,s .
# The second line contains an integer, k, the length of each substring.

def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        line = string[i:i+k]
        seen = set()
        for i in line:
            if i not in seen:
                print(i,end="")
                seen.add(i)
        print()

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
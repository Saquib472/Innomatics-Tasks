# Task_4 Q_6:
# You are given a strings .
# Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Input Format
# A single line containing a string .

# Output Format
# In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if s has any alphabetical characters. Otherwise, print False.
# In the third line, print True if s has any digits. Otherwise, print False.
# In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if s has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = input("Enter the string: ")
    print(any(map(str.isalnum,s)))
    print(any(map(str.isalpha,s)))
    print(any(map(str.isdigit,s)))
    print(any(map(str.islower,s)))
    print(any(map(str.isupper,s)))
# Task_4 Q_4:
# Read a given string, change the character at a given index and then print the modified string.

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

if __name__ == '__main__':
    s = input("Enter the string: ")
    i, c = input("Enter the index and character: ").split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
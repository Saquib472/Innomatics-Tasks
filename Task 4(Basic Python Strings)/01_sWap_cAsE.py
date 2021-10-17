# Task_4 Q_1:
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    final_str = ''
    for ch in s:
        if ch.isupper() == True:
            final_str = final_str + ch.lower()
        elif ch.islower() == True:
            final_str = final_str + ch.upper()
        else:
            final_str = final_str + ch
    return final_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
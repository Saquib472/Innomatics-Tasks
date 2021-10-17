# Task_2 Q_7:
# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
def average(array):
    res = sum(set(array))/len(set(array))
    return res

if __name__ == '__main__':
    n = int(input("Enter the number of plants: "))
    arr = list(map(int, input("Enter the heigts of the plant(space-separeted): ").split()))
    result = average(arr)
    print(result)
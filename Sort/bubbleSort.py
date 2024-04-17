#Bubble Sort
# O(n^2) for the worst and average cases.

def bubbleSort(list):
    for i in range(0, len(list) - 1):
        for j in range(0, len(list) - 1):
            if (list[j] <= list [j+1]):
                continue
            else:
                list[j], list[j+1] = list[j+1], list[j]

    return list


list = [99, 34, 55, 7, 82, 21, 9, 10, 3, 46]
list = bubbleSort(list)
print(list)
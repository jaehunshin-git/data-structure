# Selection Sort
# O(n^2) for the average and worst cases.

def selectionSort(list):
    min = 0
    for i in range(0, len(list) - 1):
        minIndex = i
        for j in range(i+1, len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        list[i], list[minIndex] = list[minIndex], list[i]
    return list

list = [2, 34, 55, 7, 82, 21, 9, 10, 3, 46]
list = selectionSort(list)
print(list)


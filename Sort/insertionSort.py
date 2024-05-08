def insertionSort(data):
    if len(data) <= 1:
        return
    
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    return data



a = [5,4,23,5,7,23,23,7,8]
a = insertionSort(a)
print(a)
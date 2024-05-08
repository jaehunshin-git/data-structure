def quickSort(arr):
    if len(arr) <= 1:
        return arr
    temp1 = []
    temp2 = []
    for i in range(1, len(arr)):
        if arr[0] > arr[i]:
            temp1.append(arr[i])
        else:
            temp2.append(arr[i])
    return quickSort(temp1) + [arr[0]] + quickSort(temp2)

a = [99, 1]
a = quickSort(a)
print(a)
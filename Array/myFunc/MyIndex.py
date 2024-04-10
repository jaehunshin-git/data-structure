def myIndex(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i;
        else:
            continue
    return -1

arr = [1,2,3,4,5]
print(myIndex(arr, 6))

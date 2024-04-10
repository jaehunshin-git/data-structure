def myInsert(arr, index, x):
    temp = []
    for i in range(0,index-1):
        temp.append(arr[i])

    temp.append(x)

    for i in range(index-1, len(arr)):
        temp.append(arr[i])
    
    return temp

arr = [1,2,3,4,5]
arr = myInsert(arr, 2, 10)

for i in range(0, len(arr)):
    print(arr[i])



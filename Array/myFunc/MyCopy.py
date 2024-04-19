def myCopy(arr):
    temp = []
    for i in range(0, len(arr)):
        temp.append(arr[i])
    return temp

a = [1,2,3,4,5]
b = myCopy(a)
print(a)
print(b)

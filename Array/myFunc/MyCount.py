def myCount(arr, x):
    num = 0
    for i in arr:
        if i == x:
            num += 1
        else:
            continue
    return num

arr = [1,2,3,4,5,1,2,3,4,5,1,2,3,5]
print(myCount(arr,4))

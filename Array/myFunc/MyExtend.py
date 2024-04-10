def myExtend(arr1, arr2):
    for i in arr2:
        arr1.append(i)

a = [1,2,3,4,5]
b = [6,7,8,9]

myExtend(a,b)
print(a)
print(b)
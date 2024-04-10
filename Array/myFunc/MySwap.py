def mySwap(arr,x,y):
    arr[x], arr[y] = arr[y], arr[x]

arr = [1,2,3,4,5]
mySwap(arr, 2, 4)

print(arr)
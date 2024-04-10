def myClear(arr):
    arrLength = len(arr)
    for i in range(0, arrLength):
        arr.pop()
        
arr = [1,2,3,4,5,6]
myClear(arr)

print(arr)
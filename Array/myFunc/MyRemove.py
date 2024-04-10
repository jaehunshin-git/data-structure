def myRemove(arr, x):
   i = 0
   while i < len(arr):
    if arr[i] == x:
           del arr[i]
    else:
        i+=1

arr = [1,2,3,4,5]
myRemove(arr, 3)

for i in arr:
    print(i)


# 파이썬은 메서드의 인수를 줄 때 참조값 자체를 준다..

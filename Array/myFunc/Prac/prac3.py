a= [1, 9, 3, 1, 8, 17, 8, 3, 218]

def myIndex(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i;
        else:
            continue
    return -1

# delete repition without modifying the sequence
def noRep(arr):
    temp =[]
    for i in arr:
        if myIndex(temp, i) == -1 :
            temp.append(i)
        else:
            continue
    arr = temp
    return arr
a = noRep(a)
print(a)
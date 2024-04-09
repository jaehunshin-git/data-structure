a = [1,2,3,4,5]

def MyReverse(x):
    firstLen = len(x)
    temp = len(x) - 2
    
    for i in range(0, len(x) - 1):
        a.append(a[temp])
        temp -= 1
    for i in range(0, firstLen - 1):
        del(a[0])

print(a)
MyReverse(a)
print(a)
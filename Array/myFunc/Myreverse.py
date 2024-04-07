a = [1,2,3,4,5]
def Myreverse():
    firstLen = len(a)
    temp = len(a) - 2
    
    for i in range(0, len(a) - 1):
        a.append(a[temp])
        temp -= 1
    for i in range(0, firstLen - 1):
        del(a[0])

print(a)
Myreverse()
print(a)
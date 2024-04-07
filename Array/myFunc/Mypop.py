a = [1,2,3,4,5]

def Mypop ():
    endNum = a[-1]
    del(a[-1])
    return endNum

print(a)
print(Mypop())
print(a)
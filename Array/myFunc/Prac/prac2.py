a = [8,17,5,18, 5, 9, 1, 2, 5, 4]

def countEvenNum(arr):
    count = 0
    for i in arr:
        if i % 2 == 0:
            count += 1
        else:
            continue
    
    return count

print(countEvenNum(a))

def repetitionCheck(arr):
    rep = False
    
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if rep is True:
                return True
            elif i == j:
                continue
            elif arr[i] == arr[j]:
                rep = True
            else:
                continue
    return rep
b = [1,2,3,4,5,5]
print(repetitionCheck(b))


def gap(arr):
    max = arr[0]
    min = arr[0]
    for i in arr:
        if i > max:
            max = i
        if i < min:
            min = i
    result = max - min
    return result

print(gap(a))
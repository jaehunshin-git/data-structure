def binarySearch(data, target):
    if len(data) == 0:
        print("Invalid data is given.")
        return

    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2
        midValue = data[mid]

        if midValue == target:
            return True
        elif midValue < target:
            start = mid + 1
        else:
            end  = mid - 1
    return False


a= [1,2,3,4,5]
print(binarySearch(a, 3))
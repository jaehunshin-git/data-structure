def bin_search_recursive(data, target):
    data.sort()

    if len(data) == 0:
        print("There is no target in the list.")
        return None

    low = 0
    high = len(data) - 1

    if low > high:
        print("Target not found in the list.")
        return None

    mid = (low + high) // 2
    mid_value = data[mid]

    if mid_value == target:
        return mid_value
    elif mid_value < target:
        return bin_search_recursive(data[mid + 1:], target)
    else:
        return bin_search_recursive(data[:mid], target)

data = [1, 3, 5, 7, 9, 11, 13]
print(bin_search_recursive(data, 15))

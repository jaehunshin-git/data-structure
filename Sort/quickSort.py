def quick_sort(arr, low, high):
    if low < high:
        # 파티션 인덱스를 정의하고, 파티션을 수행
        pi = partitionMid(arr, low, high)

        # 파티션 기준 왼쪽 부분 배열 정렬
        quick_sort(arr, low, pi - 1)
        # 파티션 기준 오른쪽 부분 배열 정렬
        quick_sort(arr, pi + 1, high)

def partitionHigh(arr, low, high):
    # 피벗을 설정 (여기서는 가장 오른쪽 요소를 피벗으로 설정)
    pivot = arr[high]
    i = low - 1  # 작은 요소의 인덱스

    for j in range(low, high):
        # 현재 요소가 피벗보다 작거나 같은 경우
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 요소를 스왑

    # 피벗을 i + 1 위치로 이동하고, i + 1을 반환
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def partitionLow(arr, low, high):
    pivot = arr[low]
    i = low + 1  # i의 시작점을 low 바로 다음 요소로 설정

    for j in range(low + 1, high):
        # 현재 요소가 피벗보다 작거나 같은 경우
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # 피벗을 올바른 위치(i-1)로 이동
    arr[i-1], arr[low] = arr[low], arr[i-1]
    return i-1  # 피벗의 새 위치 반환

def partitionMid(arr, low, high):
    # 중간 인덱스를 피벗으로 설정
    mid = (low + high) // 2
    pivot = arr[mid]
    
    # 피벗을 high 위치로 이동시킴
    arr[mid], arr[high] = arr[high], arr[mid]
    
    i = low - 1
    for j in range(low, high):
        # 현재 요소가 피벗보다 작거나 같은 경우
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 요소를 스왑

    # 피벗을 i + 1 위치로 이동하고, i + 1을 반환
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# 배열과 시작 인덱스, 마지막 인덱스를 인자로 퀵 정렬 함수 호출
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n-1)
print("정렬된 배열:", arr)

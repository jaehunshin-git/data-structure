# 2차원 배열을 생성하는 함수
def clockwiseSnail2dArr(rows, cols):
    arr_2d = [[0] * cols for _ in range(rows)]  # 초기화된 배열 생성
    
    num = 0
    start_row = 0
    start_col = 0
    end_row = rows - 1
    end_col = cols - 1

    while start_row <= end_row and start_col <= end_col:
        # 왼쪽 위에서 오른쪽 위로
        for j in range(start_col, end_col + 1):
            arr_2d[start_row][j] = num
            num += 1
        start_row += 1
        
        # 오른쪽 위에서 오른쪽 아래로
        for i in range(start_row, end_row + 1):
            arr_2d[i][end_col] = num
            num += 1
        end_col -= 1
        
        # 오른쪽 아래에서 왼쪽 아래로
        for j in range(end_col, start_col - 1, -1):
            arr_2d[end_row][j] = num
            num += 1
        end_row -= 1
        
        # 왼쪽 아래에서 왼쪽 위로
        for i in range(end_row, start_row - 1, -1):
            arr_2d[i][start_col] = num
            num += 1
        start_col += 1

    return arr_2d

# 주어진 예시에 맞게 패턴을 따르는 2차원 배열 생성
rows = 5
cols = 5
arr_2d = clockwiseSnail2dArr(rows, cols)

# 생성된 배열 출력
for row in arr_2d:
    print(" ".join(str(num).rjust(3) for num in row))

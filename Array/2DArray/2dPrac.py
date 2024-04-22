import numpy as np

# tuple unpacking
# rows 는 튜플 (3,3) 에서 요소값 3을 할당받고, cols 는 튜플에서 두번째 요소값 3을 각각 할당받는다.
# 따라서 rows = (3,) 과 cols = (3,) 의 개념과는 완전히 다르다.
# 두번째 방법대로 rows 와 cols 를 초기화 해버리면 단일 요소를 가지는 튜플을 할당하는 것이다.
rows, cols = (3,3)

a = []
for i in range(0, rows):
    for j in range(0, cols):
        a.append(int(input()))

a = np.reshape(a, (rows, cols))

for i in range(0, rows):
    for j in range(0, cols):
        print(a[i][j], end= " ")
    print(" ")


import numpy as np

a = [0,1,2,3,4,5]
rows , cols = (3,2)

a = np.reshape(a, (rows, cols))

for i in range(0, rows):
    print(' ')
    for j in range(0, cols):
        print(a[i][j], end='')

        
import numpy as np
import random

a = []
rows, cols =(5,6)
for i in range(0, rows):
    for j in range(0, cols):
        a.append(random.randrange(0,10))

a = np.reshape(a, (rows, cols))

for i in range(0, rows):
    for j in range(0, cols):
        print(a[i][j], end=" ")
    print(" ")
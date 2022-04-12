
import numpy as np
import pandas as pd
def calc_spiral(matrix, direction, x, y):
    if 0 not in matrix:
        return matrix, direction, x, y
    else:
        if direction == 'r':
            y += 1
            matrix[x,y] = matrix[x,y-1] + 1
            if matrix[x+1,y] == 0:
                direction = 'd'
            matrix, direction, x, y = calc_spiral(matrix, direction, x, y)
        elif direction == 'l':
            y -= 1
            matrix[x,y] = matrix[x,y+1] + 1
            if matrix[x-1,y] == 0:
                direction = 'u'
            matrix, direction, x, y = calc_spiral(matrix, direction, x, y)
arr = int(input("please enter an integer: "))
mat = np.zeros((arr, arr))
dir = 'r'
x = arr//2
y = arr//2
calc_spiral(mat, dir,   x, y)

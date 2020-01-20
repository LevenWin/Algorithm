# -*- coding: UTF-8 -*-
import math
# 矩阵的最小路径和 

# 空间复杂度(m*n)
def minPathSum1(arr):
    if len(arr) == 0:
        return 0
    row = len(arr)
    col = len(arr[0])
    res = []
    for i in range(0, row):
        res.append([0 for j in range(col)])
        
    res[0][0] = arr[0][0]

    for i in range(1, row):
        res[i][0] = res[i-1][0] + arr[i][0]
    for i in range(1, col):
        res[0][i] = res[0][i-1] + arr[0][i]
    
    for i in range(1, row):
        for j in range(1, col):
            res[i][j] = min(res[i-1][j], res[i][j-1]) + arr[i][j]
    return res[row - 1][col - 1]

# 空间复杂度min(m, n)
def minPathSum2(arr):
    if len(arr) == 0:
        return 0
    more = max(len(arr), len(arr[0]))
    less = min(len(arr), len(arr[0]))
    more_row = True
    if more != len(arr):
        more_row = False
    res = [0 for i in range(less)]
    res[0] = arr[0][0]
    for i in range(1, less):
        if more_row:
            res[i] = res[i-1] + arr[0][i]
        else:
            res[i] = res[i-1] + arr[i][0]
    for i in range(1, more):
        for j in range(0, less):
            v = 0
            if more_row:
                v = arr[i][j]
            else:
                v = arr[j][i]
            if j == 0:
                res[j] = res[j] + v
            else:
                res[j] = min(res[j], res[j-1]) + v
            
    return res[less - 1]




    
if __name__ == "__main__":
    arr = [
        [1, 3, 5, 9, 2],
        [8, 1, 3, 4, 2],
        [5, 0, 6, 1, 0],
        [8, 8, 4, 0, 1],
    ]
    print(minPathSum1(arr))
    print(minPathSum2(arr))
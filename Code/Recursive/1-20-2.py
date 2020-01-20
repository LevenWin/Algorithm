# -*- coding: UTF-8 -*-
import math
# 路径是否可达 1 可走，0 不可走。是否能走到右下角
def isValidPath(arr):
    if len(arr) == 0:
        return False
    row = len(arr)
    col = len(arr[0])
    res = {"result": 0}
    goto(0, 0, row, col, arr, res)
    if res["result"] == 1:
        print("Just Do It")
    else:
        print("Oh NO!")

def goto(row_index, col_index, row, col, arr, result):
    if row_index == row or col_index == col:
        return 
    if row_index + 1 == row and col_index + 1 == col:
        result["result"] = 1
        return 
    v = arr[row_index][col_index]
    if v == 0:
        return
    goto(row_index + 1, col_index, row, col, arr, result)
    if result["result"] == 1:
        return 
    goto(row_index, col_index + 1, row, col, arr, result)
    if result["result"] == 1:
        return 
if __name__ == "__main__":
    arr = [
        [1, 1, 1, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 1, 1],
    ]
    isValidPath(arr)

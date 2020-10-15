# -*- coding: UTF-8 -*-
from stack import Stack

# 给定整形矩阵，求全是1的最大子矩阵
# 深刻理解单调栈的原理。左边是比自己小，且离自己最近的index，右边是比自己大，且离自己最近的index
def maxSubRec(rect):
    height = [0, 0, 0]
    maxSub = 0
    for i in range(0, len(rect)):
        for j in range(0, len(rect[0])):
            if rect[i][j] == 0:
                height[j] = 0
            else:
                height[j] = height[j] + 1
        temp = maxItemRect(height)
        if maxSub < temp:
            maxSub = temp
    return maxSub
def maxItemRect(heights):
    s = Stack([])
    maxValue = 0
    for i in range(0, len(heights)):
        while s.isEmpty() == False and heights[i] <= heights[s.peek()]:
            top = s.pop()
            left = -1 # 0 的前一个位置为 -1
            if s.isEmpty() == False:
                left = s.peek()
            temp = heights[top] * ((i - 1) - (left + 1) + 1)
            if maxValue < temp:
                maxValue = temp
        s.push(i)

    while s.isEmpty() == False:
        top = s.pop()
        left = -1
        if s.isEmpty() == False:
            left = s.peek()
        right = len(heights)
        temp = heights[top] * ((right - 1 ) - (left + 1) + 1)
        if maxValue < temp:
            maxValue = temp
    return maxValue
        



if __name__ == "__main__":
    # print(maxSubRec([[1,0,1], [1,1,1], [1,1,1]]))
    print(maxItemRect([2,3,2,3,2]))


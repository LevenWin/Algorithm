# -*- coding: UTF-8 -*-
from tree import Tree
import sys
import os
import math
# 根据有序数组重建平衡搜索二叉树,默认递增
def generateTree(arr):
    return headFromArr(arr, 0, len(arr) - 1)
    
def headFromArr(arr, begin, end):
    if begin > end:
        return None
    index = int(math.ceil((end+begin)/2))
    node = Tree(arr[index])
    node.left = headFromArr(arr, begin, index - 1)
    node.right = headFromArr(arr, index + 1, end)
    return node
def middleTraverse(node):
    if node == None:
        return
    middleTraverse(node.left)
    print(node.value)
    middleTraverse(node.right)

if __name__ == "__main__":
    node = generateTree([1,2,3,4,5,6,7])
    middleTraverse(node)



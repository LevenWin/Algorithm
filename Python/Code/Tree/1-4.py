# -*- coding: UTF-8 -*-
from tree import Tree
import sys
import os
# 根据后序数组重建搜索二叉树

def postTraval(node):
    if node == None:
        return
    postTraval(node.left)
    postTraval(node.right)
    print(node.value)

def isPostArr(arr):
    return isPost(arr, 0, len(arr) -1)
def isPost(arr, s, e):
    if s == e:
        return True
    small = -1
    big = e
    for i in range(s, e):
        if arr[e] >  arr[i]:
            small = i
        elif big == e:
            big = i
    if small == -1 or big == e:
        return isPost(arr, s, e - 1)
    if small != big - 1:
        return False
    return isPost(arr, s, small) and isPost(arr, big, e-1)
def postToBST(arr, s, e):
    if s > e:
        return None
    node = Tree(arr[e])
    small = -1
    large = e
    for i in range(s,e):
        if arr[e] >  arr[i]:
            small = i
        elif large == e:
            large = i
    node.left = postToBST(arr, s, small)
    node.right = postToBST(arr, large, e - 1)
    return node
if __name__ == "__main__":
    print(isPostArr([2,1,3,8,6,5,7]))

            


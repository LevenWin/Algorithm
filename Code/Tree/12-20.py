# -*- coding: UTF-8 -*-
import math
from tree import Tree




def tree_height(t, h):
    if t == None:
        return h
    return max(tree_height(t.left, h + 1), tree_height(t.right, h + 1))

# 每一层的边界节点
def printEdge1(t):
    h = tree_height(t, 0)
    levelList = []
    for i in range(0, h):
        levelList.append([None, None])
    # setEdge1(t, 0, levelList)
    leafNode(t, 1,3, h)
    print(levelList)
    pass


# 某一层节点
def leafNode(t, level, target_level, h):
    if t == None or target_level > h:
        return
    if level == target_level:
        print(t.value)
        return
    else:
        leafNode(t.left, level + 1,target_level, h)
        leafNode(t.right, level + 1,target_level, h)

# 求出边界节点
def setEdge1(t, h, levelList):
    if t == None:
        return
    if h == 0:
        levelList[h][0] = t.value
        levelList[h][1] = t.value
    else:
        if levelList[h][0] == None:
            levelList[h][0] = t.value
        levelList[h][1] = t.value
    setEdge1(t.left, h + 1, levelList)
    setEdge1(t.right, h + 1, levelList)
    







if __name__ == "__main__":
    tree = Tree(0).defatulTree()
    print(printEdge1(tree))
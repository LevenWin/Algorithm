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

# 每层的内边缘节点
def internalNode(t, level, levelNodes, is_left):
    if t == None:
        return
    if len(levelNodes) <= level:
            levelNodes.append([None, None])
    if level == 0:
        levelNodes[level][0] = t.value
        levelNodes[level][1] = t.value
    else:
        if is_left:
            levelNodes[level][0] = t.value
        else:
            if levelNodes[level][1] == None:
                levelNodes[level][1] = t.value
    if level == 0:
        internalNode(t.left, level + 1, levelNodes, True)
        internalNode(t.right, level + 1, levelNodes, False)
    else:
        internalNode(t.left, level + 1, levelNodes, is_left)
        internalNode(t.right, level + 1, levelNodes, is_left)
    
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

# 左右分支的左右极点
def mostNode(t, center_offset, is_left,result, level):
    if t == None:
        return
    
    if is_left:
        if result['left']['left']['offset'] <= center_offset:
            result['left']['left']['offset'] = center_offset
            result['left']['left']['value'] = t.value
        if result['left']['right']['offset'] >= center_offset:
            result['left']['right']['offset'] = center_offset
            result['left']['right']['value'] = t.value
    else:
        if result['right']['left']['offset'] <= center_offset:
            result['right']['left']['offset'] = center_offset
            result['right']['left']['value'] = t.value
        if result['right']['right']['offset'] >= center_offset:
            result['right']['right']['offset'] = center_offset
            result['right']['right']['value'] = t.value
    if level == 0:
        mostNode(t.left, center_offset + 1, True, result, level + 1)
        mostNode(t.right, center_offset - 1, False, result, level + 1)
    else:
        mostNode(t.left, center_offset + 1, is_left, result, level + 1)
        mostNode(t.right, center_offset - 1, is_left, result, level + 1)
        


if __name__ == "__main__":
    tree = Tree(0).defatulTree()
    internalNodes = {"left":{"left":{"value":0,"offset":0}, "right":{"value":0,"offset":0}},"right":{"left":{"value":0,"offset":0},"right":{"value":0,"offset":0}}}
    mostNode(tree, 0, False, internalNodes, 0)
    print(internalNodes)
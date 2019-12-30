# -*- coding: UTF-8 -*-
import math
from tree import Tree
import tree as Tree
#找到二叉树中符合搜索二叉树条件的最大拓扑结构

def longestTree(h):
    if h == None:
        return 0
    max_length = maxTop(h, h)
    max_length = max(longestTree(h.left), max_length)
    max_length = max(longestTree(h.right), max_length)
    return max_length
def maxTop(h, n):
    if h != None and n != None and isBSTNode(h, n, n.value):
        return maxTop(h, n.left) + maxTop(h, n.right) + 1
    return 0
def isBSTNode(h, n, v):
    if h == None:
        return None
    if h == n:
        return True
    if h.value > v:
       return isBSTNode(h.left, n, v)
    else:
       return isBSTNode(h.right, n, v)
def longestTree2(h):
    return preOrder(h, {})


def preOrder(node, map):
    if node == None:
        return 0
    ls = preOrder(node.left, map)
    rs = preOrder(node.right, map)
    modifyMap(node.left, node.value, map, True)
    modifyMap(node.right, node.value, map, False)

    lr = None
    rr = None
    if node.left in map:
        lr = map[node.left]
    if node.right in map:
        rr = map[node.right]
    
    lbst = 0
    rbst = 0
    if lr != None:
        lbst = lr["l"] + lr["r"] + 1
    if rr != None:
        rbst = rr["l"] + rr["r"] + 1
    map[node] = {"l":lbst, "r":rbst}
    return max(ls, rs, (lbst + rbst + 1))

def modifyMap(node, value, map, is_left):
    if node == None or node not in map:
        return 0
    record = map[node]
    if (is_left and node.value > value) or (is_left == False and node.value < value):
        del map[node]
        return record["l"] + record["r"] + 1
    else:
        minus = 0
        if is_left:
            minus = modifyMap(node.right, value, map, is_left)
        else:
            minus = modifyMap(node.left, value, map, is_left)
        if is_left:
            record['r'] = record["r"] - minus
        else:
            record['l'] = record["l"] - minus
        map[node] = record
        return  minus
if __name__ == "__main__":
    t = Tree.decode({"s":"6!1!0!?!?!3!?!?!12!10!4!2!?!?!5!?!?!14!11!?!?!15!?!?!13!20!?!?!16!?!?!"})
    print(longestTree(t))
    print(longestTree2(t))
    pass




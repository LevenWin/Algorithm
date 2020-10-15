# -*- coding: UTF-8 -*-
import math
from tree import Tree

#Morris 后序遍历。以空间复杂度1遍历树
def morrisTree(t):
    cur = t
    mostRight = cur
    while cur != None:
        mostRight = cur.left
        if mostRight != None:
            while mostRight.right != None and mostRight.right != cur:
                mostRight = mostRight.right
            if mostRight.right == None:
                mostRight.right = cur
                cur = cur.left
                continue
            else:
                mostRight.right = None
                printEdge(cur.left)
        cur = cur.right
    printEdge(t)
    pass
def printEdge(node):
    tail = reverse(node)
    cur = tail
    while cur != None:
        print(str(cur.value))
        cur = cur.right
    reverse(tail)
def reverse(node):
    pre = None
    next = None
    while node != None:
        next = node.right
        node.right = pre
        pre = node
        node = next
    return pre

if __name__ == "__main__":
    tree = Tree(0).simpleTree()
    morrisTree(tree)

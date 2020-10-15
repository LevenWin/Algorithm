# -*- coding: UTF-8 -*-
import tree as CTree
from tree import Tree
import sys
import os


def lowestAncestor(node, node1, node2):
    if node == None or node.value == node1.value or node.value == node2.value:
        return node
    left = lowestAncestor(node.left, node1, node2)
    right = lowestAncestor(node.right, node1, node2)
    if left != None and right != None:
        return node
    if left != None:
        return left
    else:
        return right

if __name__ == "__main__":
    t = CTree.simpleTree()
    node = lowestAncestor(t, Tree(6), Tree(8))
    print(str(node.value))

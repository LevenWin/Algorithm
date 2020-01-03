# -*- coding: UTF-8 -*-

from tree import Tree
import sys
import os
# 判断tree1是否是tree2的子树
def containes(node1, node2):
    if node2 == None:
        return True
    return check(node1, node2) or containes(node1.left, node2) or containes(node1.right, node2)
def check(node1, node2):
    if node2 == None:
        return True
    if node1 == None or node1.value != node2.value:
        return False
    return check(node1.left, node2.left) and check(node1.right, node2.right)

if __name__ == "__main__":
    
    pass
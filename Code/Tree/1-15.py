# -*- coding: UTF-8 -*-
import tree as Tree
from tree import Tree as CTree
import sys
import os
import math

def maxDistance(node):
    if node == None:
        return {"height":0, "distance":0}
    result_left = maxDistance(node.left)
    result_right = maxDistance(node.right)
    height = max(result_left["height"], result_right["height"]) + 1
    distance = max(result_left["height"] + result_right["height"] + 1, result_left["distance"], result_right["distance"])
    return {"height":height, "distance":distance}
if __name__ == "__main__":
    node =Tree.simpleTree()
    result = maxDistance(node)
    print(result)

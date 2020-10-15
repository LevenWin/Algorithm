# -*- coding: UTF-8 -*-
import math
from tree import Tree
import tree as Tree
import sys

# 找到二叉树中的最大搜索二叉子树
# 搜索二叉树 节点value比左子树的最大值大，比右子树的最小值小
def bigestSearchTree(node): 
    lData = None
    rData = None
    if node.left:
        lData = bigestSearchTree(node.left)
    else:
        lData = {"node":node,"size":1,"max":node.value,"min":node.value}
    if node.right:
        rData = bigestSearchTree(node.right)
    else:
        rData = {"node":node,"size":1,"max":node.value,"min":node.value}
    max_value = max(node.value, lData["max"], rData["max"])
    min_value = min(node.value, lData["min"], rData["min"])
    size = max(lData['size'], rData['size'])
    target_node = None
    if lData["size"] >= rData["size"]:
        target_node = lData["node"]
    else:
        target_node = rData["node"]
    if lData["node"] == node.left and rData["node"] == node.right and lData["max"] <= node.value and rData["max"] >= node.value:
        target_node = node
        size = lData['size'] + rData['size'] + 1
    return {"node":target_node,"size":size, "max":max_value, "min": min_value}

if __name__ == "__main__":
    t = Tree.decode({"s":"6!1!0!?!?!3!?!?!12!10!7!6!?!?!8!?!?!14!11!?!?!15!?!?!13!20!?!?!16!?!?!"})
    node = bigestSearchTree(t)["node"].value
    print(node)


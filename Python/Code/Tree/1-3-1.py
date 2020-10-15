# -*- coding: UTF-8 -*-

import tree as Tree
import sys
import os
import math
# 判断tree是否是平衡二叉树
def isBalanced(node):
    if node == None:
        return {"level":0, "isBalanced":True}
    b1 = isBalanced(node.left)
    b2 = isBalanced(node.right)
    level = max(b1["level"], b2["level"]) + 1
    ifBalanced = False
    if b1["isBalanced"] and b2["isBalanced"] and math.fabs(b2["level"] - b1["level"]) < 2:
        ifBalanced = True
    return {"level":level, "isBalanced": ifBalanced}
if __name__ == "__main__":
    print(isBalanced(Tree.decode({"s":"1!2!4!?!?!5!8!?!?!?!3!6!?!?!7!?!?!"})))

        
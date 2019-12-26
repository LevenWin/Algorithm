# -*- coding: UTF-8 -*-
import math
from tree import Tree

#Morris 遍历。以空间复杂度1遍历树

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
                print(str(cur.value))
                cur = cur.left
                continue
            else:
                mostRight.right = None
        else:
            print(str(cur.value))
        cur = cur.right
    pass

if __name__ == "__main__":
    tree = Tree(0).simpleTree()
    morrisTree(tree)

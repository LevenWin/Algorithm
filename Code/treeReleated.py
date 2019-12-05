# -*- coding: UTF-8 -*-
from tree import TreeNode
def lastOrder(t):
    if t ==  None:
        return
    lastOrder(t.left)
    lastOrder(t.right)
    print(t.value)
    pass
def inOrder(t):
    if t ==  None:
        return
    inOrder(t.left)
    print(t.value)
    inOrder(t.right)
    pass
def firstOrder(t):
    if t ==  None:
        return
    print(t.value)
    firstOrder(t.left)
    firstOrder(t.right)
    pass

def initTree():
    t1 = TreeNode()
    t1.value = 1
    t2 = TreeNode()
    t2.value = 2
    t3 = TreeNode()
    t3.value = 3
    t4 = TreeNode()
    t4.value = 4
    t5 = TreeNode()
    t5.value = 5
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5 
    return t1
if __name__ == "__main__":
#             1
#        2          3
#    4       5

    t = initTree()
    firstOrder(t)

   

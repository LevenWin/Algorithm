# -*- coding: UTF-8 -*-
from tree import TreeNode
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
    t6 = TreeNode()
    t6.value = 6
    t7 = TreeNode()
    t7.value = 7
    t8 = TreeNode()
    t8.value = 8
    t9 = TreeNode()
    t9.value = 9


    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5 
    t3.left = t6
    t3.right = t7
    t4.left = t8
    t4.right = t9
    return t1

def firstOrder(t):
    if t ==  None:
        return
    print(t.value)
    firstOrder(t.left)
    firstOrder(t.right)
    pass
def reverseTree(t):
    if t == None or t.left == None or t.right == None:
        return
    reverseTree(t.left)
    reverseTree(t.right)
    
    temp = t.left
    t.left = t.right
    t.right = temp

    # t.left = t.left - t.right
    # t.right = t.left + t.right
    # t.left = t.right - t.left

    pass
if __name__ == "__main__":
#                      1
#                  2     3
#                4  5  6   7
#              8  9 
    
    t = initTree()
    firstOrder(t)  
    reverseTree(t)
    print(".....")
    firstOrder(t)
    pass

    
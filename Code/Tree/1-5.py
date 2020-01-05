# -*- coding: UTF-8 -*-
from tree import Tree
import sys
import os
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径
from Code.StackQueue.dqueue import DQueue

# Morris中序遍历 On的事件负责度O1的空间复杂度，来判断一个树是否是搜索二叉树----

def isBST(node):
    cur1 = node
    cur2 = None
    pre = None
    while cur1!= None:
        cur2 = cur1.left
        if cur2 != None:
            while cur2.right != None and cur2.right != cur1:
                cur2 = cur2.right
            if cur2.right == None:
                cur2.right = cur1
                cur1 = cur1.left
                continue
            else:
                cur2.right = None
        if pre != None and pre.value >  cur1.value:
            return False
        pre = cur1
        cur1 = cur1.right
    return True
def isCBT(node):
    q = DQueue()
    q.addTail(node)
    l = None
    r = None
    leaf = False
    while q.isEmpty() == False:
        h = q.pollHead()
        l = h.left
        r = h.right
        if (leaf and (l != None or r != None)) or (l == None and r != None):
            return False
        if l != None:
            q.addTail(l)
        if r != None:
            q.addTail(r)
        else:
            leaf = True
    return True
    #same level traverse
def traverseTree(node):
    q = DQueue()
    q.addTail(node)
    while q.isEmpty()== False:
        h = q.pollHead()
        if h.left != None:
            q.addTail(h.left)
        if h.right != None:
            q.addTail(h.right)
        print(h.value)



if __name__ == "__main__":
    t = Tree(0).simpleTree()
    print(isBST(t))
    print(isCBT(t))

    print(test(t))
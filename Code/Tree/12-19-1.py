# -*- coding: UTF-8 -*-
from tree import Tree
import sys
import os
# 这种奇葩的import。。。实在是不知道了，还是本来就应该这样的import
o_path = os.getcwd() # 返回当前工作目录
print(o_path)
sys.path.append(o_path) # 添加自己指定的搜索路径
from Code.StackQueue.stack import Stack

def initTree():
    t1 = Tree(1)
    t2 = Tree(2)
    t3 = Tree(3)
    t4 = Tree(4)
    t5 = Tree(5)
    t6 = Tree(6)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6
    return t1

def middleTraversal1(t):
    if t != None:
        middleTraversal1(t.left)
        print(t.value)
        middleTraversal1(t.right)

def middleTraversal2(t):
    head = t
    s = Stack([])
    while head != None or s.isEmpty() == False:
        if head != None:
            s.push(head)
            head = head.left
        else:
            n = s.pop()
            print(n.value)
            head = n.right

def firstTraversal1(t):
    if t != None:
        print(t.value)
        firstTraversal1(t.left)
        firstTraversal1(t.right)
    pass

def firstTraversal2(t):
    head = t
    s = Stack([])
    while s.isEmpty() == False or head != None:
        if head != None:
            print(head.value)
            s.push(head)
            head = head.left
        else:
            head = s.pop()
            head = head.right
def lastTraversal1(t):
    if t != None:
        lastTraversal1(t.left)
        lastTraversal1(t.right)
        print(t.value)
# 后序输出，非递归。经典！！
def lastTraversal2(t):
    head = t
    s1 = Stack([])
    s2 = Stack([])
    if head != None:
        s1.push(head)
        while s1.isEmpty() == False:
            head = s1.pop()
            s2.push(head)
            if head.left != None:
                s1.push(head.left)
            if head.right != None:
                s1.push(head.right)
        while s2.isEmpty() == False:
            print(s2.pop().value)

            


if __name__ == "__main__":
    t = initTree()
    # middleTraversal2(t)
    print(".....")
    lastTraversal2(t)
   

 



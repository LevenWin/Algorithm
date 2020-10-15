# -*- coding: UTF-8 -*-
import tree as Tree
import sys
import os

# 这种奇葩的import。。。实在是不知道了，还是本来就应该这样的import
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径
from Code.StackQueue.dqueue import DQueue

#打印出同level的节点
def printLevelNode(node):
    q = DQueue()
    level = 1
    head = node
    q.addTail(node)
    next_right = head
    most_right = head
    level_string = "Level 1: "
    while q.isEmpty() == False:
        h = q.pollHead()
        if h.left != None:
            q.addTail(h.left)
            next_right = h.left
        if h.right != None:
            q.addTail(h.right)
            next_right = h.right
        level_string = level_string + str(h.value) + " "
        if h == most_right and q.isEmpty() == False:
            print(level_string)
            level += 1
            most_right = next_right
            level_string = "Level " + str(level) + ": "
if __name__ == "__main__":
    t = Tree.decode({"s":"6!1!0!?!?!3!?!?!12!10!4!2!?!?!5!?!?!14!11!?!?!15!?!?!13!20!?!?!16!?!?!"})
    printLevelNode(t)

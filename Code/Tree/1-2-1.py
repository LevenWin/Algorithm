# -*- coding: UTF-8 -*-

from tree import Tree
import sys
import os
#打印出通level的节点
# 这种奇葩的import。。。实在是不知道了，还是本来就应该这样的import
o_path = os.getcwd() # 返回当前工作目录
sys.path.append(o_path) # 添加自己指定的搜索路径
from Code.StackQueue.stack import Stack

#中序遍历，看排序出错的node
def wrongsNode(node):
    q = Stack()
    head = node
    q.push(head)
    pre = None
    while q.isEmpty() == False or head != None:
        if head != None:
            q.push(head)
            print(head.value)
            head = head.left
        else:
            head = q.pop()
            if pre != None and pre.value > head.value:
                print(head.value)
            pre = head
            head = head.right

if __name__ == "__main__":
    tree = Tree(0).defatulTree()
    wrongsNode(tree)









    

    
        
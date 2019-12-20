# -*- coding: UTF-8 -*-

class Tree(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def defatulTree(self):
        t1 = Tree(1)
        t2 = Tree(2)
        t3 = Tree(3)
        t4 = Tree(4)
        t5 = Tree(5)
        t6 = Tree(6)
        t7 = Tree(7)
        t1.left = t2
        t1.right = t3
        t2.left = t4
        t2.right = t5
        t3.right = t6
        t6.left  = t7
        return t1

    
# -*- coding: UTF-8 -*-

class Tree(object):
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    def simpleTree(self):
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
    def defatulTree(self):
        t1 = Tree(1)
        t2 = Tree(2)
        t3 = Tree(3)
        t4 = Tree(4)
        t5 = Tree(5)
        t6 = Tree(6)
        t7 = Tree(7)
        t8 = Tree(8)
        t9 = Tree(9)
        t10 = Tree(10)
        t11 = Tree(11)
        t12 = Tree(12)
        t1.left = t2
        t1.right = t3
        t2.left = t4
        t2.right = t5
        t3.left = t6
        t3.right = t7
        t5.left = t8
        t8.right = t10
        t6.right = t9
        t9.left = t11
        t11.left = t12
        return t1
    # printTree(pt)
#                   1
#            2              3
#         4    5          6   7
#            8              9 
#              10         11
#                       12
#
#

    
# -*- coding: UTF-8 -*-
from linkedlist import LinkedLink
from linkedlist import LinkNode
# 删除node,只给出一个node
def deleteNode(node):
    if node.next == None:
        print("哦豁。。删不掉")
    else:
        node.value = node.next.value
        node.next = node.next.next





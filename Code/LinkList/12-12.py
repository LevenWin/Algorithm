# -*- coding: UTF-8 -*-
# 链表转数字相加
from linkedlist import LinkedLink
from linkedlist import LinkNode
import math

##🌟第一个秒解的题目。有进步！
def numAddWithLink(head1, head2):
    cur1 = head1.next
    cur2 = head2.next
    return getNum(cur1)[0] + getNum(cur2)[0]

def getNum(node):
    if node == None:
        return (0, 0)
    (sum, level) = getNum(node.next)
    sum = sum + math.pow(10, level) * node.value
    return (sum, level + 1)

if __name__ == "__main__":
    link1 = LinkedLink()
    link1.addList([1,2,3])
    link2 = LinkedLink()
    link2.addList([2,3])
    print(numAddWithLink(link1.head, link2.head)) # 146



    

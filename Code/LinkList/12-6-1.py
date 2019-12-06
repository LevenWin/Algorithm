# -*- coding: UTF-8 -*-
# 删除链表倒数第k个节点
from linkedlist import LinkedLink
from linkedlist import LinkNode

def removelastNode(k, first):
    cur = first
    while cur != None:
        k = k - 1
        cur = cur.next
        
    if k == 0:
        n = first.next
        n.previous = first.previous
        first.previous.next = n
        
    if k < 0:
        k = k + 1
        while k != 0:
            k = k + 1
            first = first.next
        first.next = first.next.next
        if first.next != None:
            first.next.previous = first
if __name__ == "__main__":
    a = LinkedLink()
    a.add(LinkNode(1))
    a.add(LinkNode(2))
    a.add(LinkNode(3))
    a.add(LinkNode(4))
    a.add(LinkNode(5))
    a.add(LinkNode(6))
    a.add(LinkNode(7))
    removelastNode(10, a.head.next)
    print(str(a))
    removelastNode(1, a.head.next)
    print(str(a))
    removelastNode(6, a.head.next)
    print(str(a))
    removelastNode(4, a.head.next)
    print(str(a))



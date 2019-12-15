# -*- coding: UTF-8 -*-

# 有序链表的共同部分
from linkedlist import LinkedLink
from linkedlist import LinkNode

if __name__ == "__main__":
    a = LinkedLink()
    a.add(LinkNode(1))
    a.add(LinkNode(2))
    a.add(LinkNode(3))
    a.add(LinkNode(4))
    a.add(LinkNode(5))

    b = LinkedLink()
    b.add(LinkNode(2))
    b.add(LinkNode(3))
    b.add(LinkNode(4))

    ha = a.head.next
    hb = b.head.next
    while ha.next != None and hb.next != None:
        if ha.value > hb.value:
            hb = hb.next
        if ha.value < hb.value:
            ha = ha.next
        if ha.value == hb.value:
            print(hb.value)
            ha = ha.next
            hb = hb.next


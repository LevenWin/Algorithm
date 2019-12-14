# -*- coding: UTF-8 -*-
# 每k个节点反转
from linkedlist import LinkedLink
from linkedlist import LinkNode
import math


def reverseK(head, k):
    cur = head.next
    i = 1
    previous = head
    begin = head.next
    next = cur.next
    while cur != None:
        cur = cur.next
        i += 1
        if i == k and cur != None:
            next = cur.next
            i = 1
            begin = previous.next
            previous = reverse(begin, cur, previous, next)
            cur = next

def reverse(begin, end, previous, next):
    cur = begin
    p = next
    while cur != end:
        n = cur.next
        cur.next = p
        p = cur
        cur = n
        
    end.next = p
    previous.next = end
    begin.next = next
    return begin

if __name__ == "__main__":
    link = LinkedLink()
    link.addList([1,2,3,4,5,6,7,8,9,2,3,4,4])
    reverseK(link.head, 3)
    print(str(link))


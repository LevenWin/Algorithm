# -*- coding: UTF-8 -*-
# 删除中间节点

from linkedlist import LinkedLink
from linkedlist import LinkNode
import math

def deleteMiddle(head):
    l = 0
    cur = head
    while cur != None and cur.next != None:
        l = l + 1
        cur = cur.next
    i = math.floor(l / 2)
    if i*2 < l:
        i = i + 1
    while i != 0:
        i = i - 1
        head = head.next
    n = head.next
    n.previous = head.previous
    head.previous.next = n

def deleteItem(p, head):
    if p >=1 or head == None or head.next == None:
        return
    l = 0
    cur = head
    while cur.next != None:
        l += 1
        cur = cur.next
    i = math.ceil(l * p)
    while i !=0 :
        head = head.next
        i -= 1
    n = head.next
    n.previous = head.previous
    head.previous.next = n

if __name__ == "__main__":
    a = LinkedLink()
    a.addList([1,2,3,4,5])
    deleteMiddle(a.head)
    print(str(a))
    deleteItem(3/5, a.head)
    print(str(a))

    

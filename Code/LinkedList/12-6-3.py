# -*- coding: UTF-8 -*-
# 反转链表
from linkedlist import LinkedLink
from linkedlist import LinkNode

## 交换来反转链表
def reverse(head):
    cur = head.next
    while cur != None:
        n = cur.next
        p = cur.previous
        p.previous = cur
        cur.next = p
        if n == None:
            cur.previous = head
            head.next = cur
            head.previous.next = None
            head.previous = None
            break
        else:
            cur = n

## 递归来解决反转链表
def recurse(item):
    if item == None:
        return
    n = item.next
    p = item.previous
    recurse(n)
    item.next = p
    item.previous = n
def reverse2(l):
    recurse(l.head)
    realEnd = l.head.previous
    realEnd.next = None
    end = l.end
    l.end = realEnd
    l.head.next = end
    end.previous = l.head
    l.head.previous = None
    

if __name__ == "__main__":
    link = LinkedLink()
    link.addList([0,1,2,3,4])
    reverse2(link)
    print(str(link))

    

        
    


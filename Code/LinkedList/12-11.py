# -*- coding: UTF-8 -*-
# 左边小右边大，中间相等
from linkedlist import LinkedLink
from linkedlist import LinkNode
import math

def transform2(head, pivot):
    bh = head
    bt = head
    eh = head
    et = head
    sh = head
    st = head
    while head != None:
        n = head.next
        #小于的链表，相等的链表， 大的链表
        #然后小 > 等 > 大
        if head.value > pivot:
            pass
        elif head.value == pivot:
            pass
        else:
            pass

        pass
    

def transform(head, pivot):
    if head == None:
        return head
    h = transform(head.next, pivot)
    if h != None:
        head.next = h
        ifUpdate = False
        if head.value >= pivot:
            cur = head.next
            previous = head
            while cur != None and cur.value <= pivot:
                previous = cur
                cur = cur.next
                ifUpdate = True
            previous.next = head
            head.next = cur
        if ifUpdate:
            return h
        else:
            return head
    else:
        return head
    pass
if __name__ == "__main__":
    link = LinkedLink()
    link.addList([9, 0, 2,7,8,10,32,5,6,4, 5, 1])
    link.head.next = transform(link.head.next, 7)
    print(str(link))
    # 2 4 5 6 7 9 8 6/ 5
    # 2 5 4 6 6 7 9 8/ 6
    

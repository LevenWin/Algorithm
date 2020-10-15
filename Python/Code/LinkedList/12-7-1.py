# -*- coding: UTF-8 -*-

# 反转指定范围的链表
from linkedlist import LinkedLink
from linkedlist import LinkNode

def reverseFromStart(head, l):
    while l != 0 and head.next != None:
        p = head.previous
        n = head.next
        head.previous = n
        head.next = p
        head = n
        l -= 1 
    return head
        

        


def reverse(head, f, t):
    cur = head
    if f <= 0:
        f = 0

    while cur != None:
        if f == 0:
            p = cur.previous
            end = reverseFromStart(cur, t - f)
            endP = end.previous
           
            endN = end.next
            # 最后的指向反转
            end.next = endP

            ## 最后一个
            cur.next = endN
            if endN != None:
                endN.previous = cur
            ## 前一个
            if p != None:
                p.next = end
            end.previous = p
            break
        else:
            cur = cur.next
            f -=1
            t -=1
if __name__ == "__main__":
    link  = LinkedLink()
    link.addList([1,2,3,4,5,6,7,8])
    reverse(link.head, 1, 10)
    print(str(link))



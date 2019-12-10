# -*- coding: UTF-8 -*-
# 回文链表
from linkedlist import LinkedLink
from linkedlist import LinkNode
import math

# 空间复杂度为1 时间复杂度为n 判断是否是回文链表

# 反转右边链表到中间，从前后遍历到中间是否相等

def isPalindrome(head):
    length = 0
    cur = head
    end = cur
    while cur.next != None:
        cur = cur.next
        length += 1
    end = cur
    cur = head.next
    i = 0
    pre = cur
    half = math.ceil(length / 2)
    while cur != None:
        i += 1
        if i > half:
            n = cur.next
            cur.next = pre
            pre = cur
            cur = n  
        else:
            if i == half:
                n = cur.next
                cur.next = None
                pre = cur
                cur = n
            else:
                cur = cur.next
                pre = cur

    cur = head.next
    ifPalindrome = False
    i = 0
    curEnd = end
    while cur.value == curEnd.value:
        cur = cur.next
        curEnd = curEnd.next
        i += 1
        if i == half:
            ifPalindrome = True
            break
    
    cur = end
    pre = None
    i = 0
    while cur != None:
        i += 1
        if i <= half:
            n = cur.next
            cur.next = pre
            pre = cur
            cur = n
        else :
            break
    return ifPalindrome

if __name__ == "__main__":
    link = LinkedLink()
    link.addList([0])
    print(str(link))
    print(isPalindrome(link.head))
    
            

        


    
            
            

    
    
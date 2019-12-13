# -*- coding: UTF-8 -*-
# 入环点
from linkedlist import LinkedLink
from linkedlist import LinkNode
import math


def circleNode(head):
    meetNode = circleMeet(head)
    if meetNode == None:
        return None
    cur = head.next
    while cur != None and meetNode != None:
        if cur == meetNode:
            return cur
        else:
            cur = cur.next
            meetNode = meetNode.next
    return None

    # 入环点
def circleMeet(head):
    cur1 = head.next
    cur2 = head.next
    while cur1 != None and cur2 != None:
        cur1 = cur1.next
        cur2 = cur2.next.next
        if cur1 == cur2:
            return cur1
    return None
def noCircleMeet(head1, head2):
    cur1 = head1.next
    cur2 = head2.next
    l1 = 1
    l2 = 2
    while cur1.next != None:
        l1 += 1
        cur1 = cur1.next
    while cur2.next != None:
        l2 += 1
        cur2 = cur2.next
    if cur1 != cur2:
        return None

    large = l1 - l2
    cur1 = head1.next
    cur2 = head2.next
    if l1 < l2:
        large = l2 - l1
        cur1 = head2.next
        cur2 = head1.next
    while cur1 != None and cur2 != None and cur1 == cur2:
        if large == 0:
            cur2 = cur2.next
        cur1 = cur1.next
    return cur1

def twoCircleMeet(head1, head2, meet1, meet2):
    cur1 = meet1.next
    if meet1 == meet2:
        return twoCircleMeet2(head1, head2, meet1, meet2)
    else:
        while cur1 != None and cur1 != meet1:
            if cur1 == meet2:
                return twoCircleMeet2(head1, head2, meet1, meet2)
        return None # 不相交

    

# 环内相交
def twoCircleMeet1(head1, head2, meet1, meet2):
    # 返回meet1 或者meet2应该都行。
    # return meet1 
    return meet2

# 环外相交。同一个入环点
def twoCircleMeet2(head1, head2, meet):
    cur1 = head1.next
    cur2 = head2.next
    l1 = 0
    l2 = 0
    while cur1 != meet:
        cur1 = cur1.next
        l1 += 1
    while cur2 != meet:
        cur2 = cur2.next
        l2 += 1
    # 后续逻辑跟在两无环链表相交一样
    ...


    pass

if __name__ == "__main__":
    link = LinkedLink()
    node1 = LinkNode(1)
    node2 = LinkNode(2)
    node3 = LinkNode(3)
    node4 = LinkNode(4)
    node5 = LinkNode(5)
    node6 = LinkNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3
    link.head.next = node1
    print(circleNode(link.head).value)
    

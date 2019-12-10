# -*- coding: UTF-8 -*-
# 约瑟夫环
from linkedlist import LinkedLink
from linkedlist import LinkNode
def josephusKill(head, m):
    cur = head.next
    tmp = 1
    while cur.next != None:
        cur = cur.next
        tmp += 1
    tmp = getLive(tmp, m)
    while tmp != 0:
        head = head.next
        tmp -= 1
    return head.value
    
def getLive(i, m):
    if i == 1:
        return 1
    return (getLive(i - 1, m) + m -1)%i + 1

#老 = （新 + m - 1）% i + 1
# 每个坐标这次喊的数字与前一次有关。
# 将设最后是坐标为X的人最后喊1，此时仅存1人
# 那么 上一次他喊 （1 + m - 1）% i + 1,此时仅存2人
# 以此类推递归递归到最开始这个人喊的数字就是他的位置

if __name__ == "__main__":
    link = LinkedLink()
    link.addList([1,2,3])
    print(josephusKill(link.head, 3))

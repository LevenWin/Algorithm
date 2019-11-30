 # -*- coding: UTF-8 -*-
# 汉诺塔问题解决

# 方法一 利用栈
from stack import Stack

def handleProblem(num, left, mid, right):
    lS = Stack([])
    mS = Stack([])
    rS = Stack([])
    count = num
    while count > 0:
        lS.push(count)
        count-=1
    step = 0
    # L to M = 1
    # M to L = 2
    # M to R = 3
    # R to M = 4
    record = [0]
    print(num, len(rS.dataList) != num)
    while len(rS.dataList) != num:
        step += moveStack(record, 2, 1,lS, mS, left, mid)
        step += moveStack(record, 1, 2, mS, lS, mid, left)
        step += moveStack(record, 4, 3, mS, rS, mid, right)
        step += moveStack(record, 3, 4, rS, mS, right, mid)
    return step

def moveStack(record, reverseAction, nowAction, fS, tS, f, t):
    if record[0] != reverseAction and  (fS.peek() < tS.peek() or tS.isEmpty()) and fS.isEmpty() == False:
        tS.push(fS.pop())
        print("move " + str(tS.peek()) + " from " + f + " to " + t)
        record[0] = nowAction
        return 1
    return 0
if __name__ == "__main__":
   count = handleProblem(7, "left", "mid", "right")
   print("共： "+ str(count))
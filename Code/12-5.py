# -*- coding: UTF-8 -*-
# 可见山峰的数量
from stack import Stack
def visibleNum(l):
    length = len(l)
    maxIndex = 0
    for i in range(0, length):
        if maxIndex < l[i]:
            maxIndex = i
    res = 0
    index = nextIndex(maxIndex, len(l))
    s = Stack([])
    s.push([l[maxIndex]])
    while index != maxIndex:
        while s.isEmpty() == False and s.peek()[0] < l[index]:
            k = len(s.pop())
            res = res + getInternalSum(k) + 2 * k
        if s.isEmpty():
            s.push([l[index]])
        elif s.peek()[0] == l[index]:
            s.peek().append(l[index])
        else:
            s.push([l[index]])
        index = nextIndex(index, length)
    
    while len(s.dataList) > 2:
        k = len(s.pop())
        res = res + 2 * k + getInternalSum(k)
    if len(s.dataList) == 2:
        k = len(s.pop())
        res = res + getInternalSum(k)
        if len(s.peek()) == 1:
            res = res + k
        else:
            res = res + k * 2
    res = res + getInternalSum(len(s.pop()))
    return res 
        
def getInternalSum(k):
    if k == 1:
        return 0
    else:
        return k * (k - 1) /2

def nextIndex(index, size):
    if index == size - 1:
        return 0
    else:
        return index + 1

if __name__ == "__main__":
    print(visibleNum([1,2,4,2,6,3]))
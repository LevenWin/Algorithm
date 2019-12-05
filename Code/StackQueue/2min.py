# -*- coding: UTF-8 -*-
from stack import Stack
# 求数组内元素前后小值的index数组
# 单调栈结构
#数组内部有重复值的情况
def twoMin2(l):
    s = Stack([])
    res = []
    for i in range(0, len(l)):
        res.append([-1, -1])
        while s.isEmpty() == False and l[s.peek()[0]] > l[i]:
            tops = s.pop()
            leftIndex = -1
            if s.isEmpty() == False:
               leftIndex = s.peek()[-1]
            for top in tops:
                res[top][0] = leftIndex
                res[top][1] = i
        if s.isEmpty() == False and l[s.peek()[0]] ==l[i]:
            s.peek().append(i)
        else:  
            s.push([i])

    while s.isEmpty() == False:
        tops = s.pop()
        lastIndex = -1
        if s.isEmpty() == False:
            lastIndex = s.peek()[-1]
            for top in tops:
                res[top][0] = lastIndex
                res[top][1] = -1
    return res

# 数组内部没有重复值的情况
def twoMin(l):
    s = Stack([])
    res = []
    for i in range(0, len(l)):
        res.append([-1, -1])
        while s.isEmpty() == False and l[s.peek()] > l[i]:
            top = s.pop()
            ele = res[top]
            ele[1] = i
            if s.isEmpty():
                ele[0] = -1
            else:
                ele[0] = s.peek()        
        s.push(i)
    while s.isEmpty() == False:
        top = s.pop()
        ele = res[top]
        ele[1] = -1
        if s.isEmpty():
            ele[0] = -1
        else:
            ele[0] = s.peek()
    return res
if __name__ == "__main__":
    print(twoMin([2,3,1,4,7,5,8,9,11]))
    print(twoMin2([2,3,1,2,7,3,8,5,3]))

    pass


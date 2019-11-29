 # -*- coding: UTF-8 -*-

#给栈中的元素排序，不能使用其他数据结构，只能使用临时变量

from stack import Stack

def insertSort(stack, obj):
    if stack.isEmpty():
        stack.push(obj)
        return
    else:
        if obj > stack.peek():
            stack.push(obj)
        else:
            ele = stack.pop()
            insertSort(stack, obj)
            stack.push(ele)
def sort(stack):
    if stack.isEmpty():
        return
    else:
       ele = stack.pop()
       sort(stack)
       insertSort(stack, ele)
def print_stack(s):
    print(s.dataList)

# 方法二
def sortStack(s):
    tempS = Stack()
    while s.isEmpty() == False:
        top = s.pop()
        while tempS.isEmpty() == False and tempS.peek() > top:
            s.push(tempS.pop())
        tempS.push(top)
    return tempS


if __name__ == "__main__":
    s = Stack([3,2,1,6,4,5,16])
    # 方法一
    # sort(s)
    # 方法二
    s = sortStack(s)
    print_stack(s)

    # insertSort(s, 7)
    # print_stack(s)

    



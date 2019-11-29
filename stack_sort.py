from stack import Stack
# 给栈中的元素排序，不能使用其他数据结构，只能使用临时变量
def insertSort(stack, obj):
    if stack.isEmpty():
        stack.push(obj)
        return
    else:
        if obj > stack.peak():
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

if __name__ == "__main__":
    s = Stack()
    s.push(3)
    s.push(2)
    s.push(1)
    s.push(6)
    s.push(4)
    s.push(5)
    s.push(16)
    print_stack(s)
    sort(s)

    print_stack(s)
    insertSort(s, 7)

    print_stack(s)

    



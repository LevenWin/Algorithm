# -*- coding: UTF-8 -*-

# 选择排序，从未排序的序列中选择最大/小的插入已排序
def selectMinSort(list):
    for i in range(0, len(list) - 1):
        min = i
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
# 插入排序，从未排序的选择一个插入已排序的序列中
def insertSort(list):
    for i in range(1, len(list)):
        j = i - 1
        index = i
        while j >= 0:
            if list[index] <= list[j]:
                temp = list[index]
                list[index] = list[j]
                list[j] = temp 
                index = j
            j -= 1

# 快速排序。第一轮 小的在左，大的在右。继续将左右进行同样排序
def quickSort(list):
    if len(list) < 2:
        return list
    left = []
    right = []
    mids = []
    mid = list[-1]
    for i in list:
        if i < mid:
            left.append(i)
        if i == mid:
            mids.append(i)
        if i > mid:
            right.append(i)
    if len(left) > 1:
        left = quickSort(left)
    if len(right) > 1:
        right = quickSort(right)
    return left + mids + right

if __name__ == "__main__":
    list = [0, 1, 4, 6, 3, 6 ,7, 3 ,8, 9, 5]
    list = quickSort(list)
    print(list)




# -*- coding: UTF-8 -*-
import math
# 选择排序，从未排序的序列中选择最大/小的插入已排序 N2
def selectMinSort(list):
    for i in range(0, len(list) - 1):
        min = i
        for j in range(i + 1, len(list)):
            if list[min] > list[j]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
# 插入排序，从未排序的选择一个插入已排序的序列中 N2
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

# 快速排序。第一轮 小的在左，大的在右。继续将左右进行同样排序 NlogN
def quickSort(list):
    if len(list) < 2:
        return list
    
    # 如果不允许额外的数组空间，则需要在原素组内交换变量
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
    # 归并排序 NlogN
def mergeSort(list):
    if len(list) > 1:
        mid = math.floor(len(list)/2)
        left = list[:mid]
        right = list[mid:]
        left = mergeSort(left)
        right = mergeSort(right)
        tmp = []
        l = 0
        r = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                tmp.append(left[l])
                l += 1
            else:
                tmp.append(right[r])
                r += 1
        if l < len(left):
           tmp += left[l: len(left)]
        if r < len(right):
           tmp += right[r: len(right)]
        return tmp
    else:
        return list
        
# 计数排序
def countSort(list):
    large = list[0]
    for i in list:
        if large < i:
            large = i

    arr = []
    for i in range(0, large + 1):
        arr.append(0)
    for i in list:
        arr[i] = arr[i] + 1
    sorted = []
    for i in range(0, len(arr)):
        value = arr[i]
        while value != 0:
            sorted.append(i)
            value -= 1
    return sorted



if __name__ == "__main__":
    list = [0,3,2,1,4,2,6,4,8,9,2]
    list = countSort(list)
    print(list)




# -*- coding: UTF-8 -*-
#最大值减去最小值小于或等于num的子数组数量
# 满足这个公式的子数组，而不是所有子数组 max(arr[i..j]) - min(arr[i..j]) <= num
from dqueue import DQueue
def numValid(l, num):
    max = DQueue()
    min = DQueue()
    i = 0
    j = 0
    res = 0
    while i < len(l):
        while j < len(l):
            if min.isEmpty() or min.peekTail() != j:
                while max.isEmpty() == False and l[max.peekTail()] < l[j]:
                    max.pollTail()
                max.addTail(j)
                while min.isEmpty() == False and l[min.peekTail()] > l[j]:
                    min.pollTail()
                min.addTail(j)
            if l[max.peekHead()] - l[min.peekHead()] > num:
                break
            j = j + 1
        res = res + j - i
        for t in range(i+1, j+1):
            print(i, t, l[i:t])
        # 碰到极值，在下轮则移除    
        if min.peekHead() == i:
            min.pollHead()
        if max.peekHead() == i:
            max.pollHead()
        
        i = i + 1
        
    return res
if __name__ == "__main__":
    print(numValid([2,3,4,1,5], 2))

            
        
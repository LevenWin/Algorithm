 # -*- coding: UTF-8 -*-
from dqueue import DQueue
# 滑动窗口 [2,3,5,7,3,4,5,6] 窗口大小为3，输出窗口大值数组
def windowSlide(l, num):
    wIndex = DQueue()
    wMax = []
    for i in range(0, len(l)):
        while wIndex.isEmpty() == False and l[wIndex.peekTail()] < l[i]:
            wIndex.pollTail() 
        wIndex.addTail(i)
        if wIndex.peekHead() < i - num + 1:
            wIndex.pollHead()
        if i >= num - 1:
            wMax.append(l[wIndex.peekHead()])
    return wMax
if __name__ == "__main__":
    wMax = windowSlide([2,5,7,3,4,5,6,4,5,2,3,22,3,4,55,3322,432,5332,2,5,3425,342], 3)
    print(wMax)
# 滑动窗口用来存储经历过的数据的大值排序。 对头始终是最大，至队尾依次变小。检测对头的index是否过期并且移除。

        
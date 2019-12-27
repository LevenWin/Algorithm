# -*- coding: UTF-8 -*-
import math
from tree import Tree
# 未排序数组中累加和为给定值的最长子数组
def longForSameSum(list, k):
    if len(list) == 0:
        return 0
    hashSum = {}
    sum = 0
    length = 0
    for i in range(0, len(list)):
        sum += list[i]
        if str(sum - k) in hashSum:
            if length < i - hashSum[str(sum - k)]:
                length = i - hashSum[str(sum - k)]
        if sum not in hashSum:
            hashSum[str(sum)] = i
    return length
    # 将每个分支看成一个数组
def longForSameSumTree(tree, sum, hashSum, level, k, maxLength):
    if tree == None:
        return maxLength
    curSum = sum + tree.value
    if str(curSum) not in hashSum:
        hashSum[str(curSum)] = level
    if str(curSum - k) in hashSum:
        if maxLength < hashSum[str(curSum - k)]:
            maxLength = hashSum[str(curSum - k)]
    maxLength = longForSameSumTree(tree.left, curSum, hashSum, level + 1, k, maxLength)
    maxLength = longForSameSumTree(tree.right, curSum, hashSum, level + 1, k, maxLength)
    # 离开该分支的开头的树后，需要删除，以免影响其他分支树
    if hashSum[str(curSum)] == level:
        del hashSum[str(curSum)]
    return maxLength

if __name__ == "__main__":
    print(longForSameSum([1,3,-2,7,-3,5,2,8,3], 7))
    




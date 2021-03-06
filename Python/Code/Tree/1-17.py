# -*- coding: UTF-8 -*-

# 给定一个整数N，如果N＜1，代表空树结构，否则代表中序遍历的结果为{1，2，3，…，N}。
# 请返回可能的二叉树结构有多少。

# [1...5]
# 依次已 j = 1...5为root节点，则左边为 j - 1,右边 n - j个节点
# 如果知道 1个，2个，3个节点能组成多少个二叉树，则n个节点我们都可知。
# i 代表共几个节点
# j 代表当前节点作为root节点
# 如果要求出n个节点能够组成多少种搜索二叉树，则需要知道n-1个节点能组成多少个搜索二叉树
# 依次类推，已知 1个节点能组成一个搜索二叉树，则2个点能组成2个搜索二叉树 
# 3个节点能组成 1*2 + 2*1 + 1*1 = 5个搜索二叉树 个搜索二叉树
def numTrees(n):
    if n < 2:
        return 1
    nums = [0 for i in range(n+1)]
    nums[0] = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            nums[i] += nums[j - 1] * nums[i - j]
    return nums[n]
if __name__ == "__main__":
    print(numTrees(5))

    

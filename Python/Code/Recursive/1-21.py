# -*- coding: UTF-8 -*-
import math
def minCoins1(arr, aim):
    if len(arr) == 0:
        return -1
    num = process1(arr, 0, aim)
    print(num)


# i 代表数字的位置
# k 代表位置的数字用几个
    
def process1(arr, i, rest):
    # 如果i等于数组的长度，则代表没有多余的数字可用了。
    # 如果此时剩余的钱还是不等于零，则返回 -1，否则返回0
    if i == len(arr):
        return 0 if rest == 0 else -1
    # 最少要拼凑的数字个数
    res = -1
    # 该位置数字所需要的个数
    k = 0
    while k * arr[i] <= rest:
        next = process1(arr, i+1, (rest - k * arr[i]))
        if next != -1: # 说明拼凑有效
            # 如果res 为 -1，则代表是初始状态回来，
            res = next+k if res == -1 else min(res, next + k)
        
        k+=1
    return res # 已经用了多少个数字拼凑

# 暴力破解 [5,2,3] 10
def process1Copy(arr, i, rest):
    if i == len(arr):
        return 0 if rest == 0 else -1
    res = -1
    k = 0
    while k * arr[i] < rest:
        next = process1Copy(arr, i + 1, rest - k * arr[i])
        if next != -1:
            res = next + k if res == -1 else min(res, next + k)
        k += 1
    return res
def process2Copy(arr, i, rest):
    if i == len(arr):
        return 0 if rest == 0 else -1
    res = -1
    k = 0
    while k * arr[i] <  rest:
        next = process2Copy(arr, i + 1, rest - k * arr[i])
        if next != -1:
            res = next + k if res == -1 else min(res, next + k)
        k += 1
    return res
# 动态规划 
def minCoin(arr, aim):
    if len(arr) == 0 or aim <= 0:
        return 0
    n = len(arr)
    dp = []
    for i in range(n+1):
        temp = []
        for j in range(aim + 1):
            if i == n and j != 0:
                temp.append(-1)
            else:
                temp.append(0)
        dp.append(temp)
    # print(dp)
    i = n-1
    while i >= 0:
        rest = 0 
        while rest <= aim:
            dp[i][rest] = -1
            if dp[i+1][rest] != -1:
                dp[i][rest] = dp[i+1][rest]
            if rest - arr[i] >= 0 and dp[i][rest - arr[i]] != -1:
                if dp[i][rest] == -1:
                    dp[i][rest] = dp[i][rest - arr[i]] + 1
                else:
                    dp[i][rest] = min(dp[i][rest], dp[i][rest-arr[i]] + 1)
            rest += 1
        i -= 1
    return dp[0][aim]
# 从上到下
def minCoin2(arr, aim):
    if len(arr) == 0 or aim <= 0:
        return 0
    n = len(arr)
    dp = []
    for i in range(n):
        temp = []
        for j in range(aim + 1):
            temp.append(-1)   
        dp.append(temp)
    i = 0
    while i < n:
        rest = 0
        while rest <= aim:
            if rest == 0 and i == 0:
                dp[i][rest] = 0
            else:
                dp[i][rest] = -1
            if i > 0 and dp[i-1][rest] != -1:
                dp[i][rest] = dp[i-1][rest]
            if rest - arr[i] >= 0 and dp[i][rest - arr[i]] != -1:
                if dp[i][rest] == -1:
                    dp[i][rest] = dp[i][rest - arr[i]] + 1
                else:
                    dp[i][rest] = min(dp[i][rest], dp[i][rest - arr[i]] + 1)
            rest += 1
        i += 1
    return dp[n-1][aim]


if __name__ == "__main__":
   print(minCoin2([5,2,1,3],10)) 
    # for i in range(10,0,-1):
    #     print(i)

/* 数组中元素和值最大的连续子数组
[1,2,3,-4,5,7,-4,-7,-2,-2,-6,9]
连续子数组最后一个元素肯定是原数组的某个元素。
假设index = 1 结尾， [1] 和值最大为1
假设index = 2 结尾，[1, 2]和值最大为3
假设index = 3 结尾，[1, 2, 3]和值最大为6
假设index = 4 结尾，[1, 2, 3, -4]和值最大为2
假设index = 5 结尾，[1, 2, 3, -4, 5]和值最大为7
假设index = 6 结尾，[1, 2, 3, -4, 5, 7]和值最大为14
假设index = 7 结尾，[1, 2, 3, -4, 5, 7, -4]和值最大为10
假设index = 8 结尾，[1, 2, 3, -4, 5, 7, -4, -7]和值最大为3
假设index = 9 结尾，[1, 2, 3, -4, 5, 7, -4, -7, -2]和值最大为1
假设index = 10 结尾，[1, 2, 3, -4, 5, 7, -4, -7, -2, -2]和值最大为-1
假设index = 11 结尾，[1, 2, 3, -4, 5, 7, -4, -7, -2, -2, -6]和值最大为-6
假设index = 11 结尾，[1, 2, 3, -4, 5, 7, -4, -7, -2, -2, -6, 9]和值最大为3

关联公示
N(n) = num[i] + N(n-1) if N(n-1) > 0
N(n) = num[i] if N(n-1) <= 0

N(n) = Max(num[i] + N(n-1), num[i])

时间复杂度 O(n), 空间复杂度O(n)
*/
function soluation(arr) {
    let res = []
    for (let index = 0; index < arr.length; index++) {
        const element = arr[index];
        if (index == 0) {
            res.push(element)
        } else {
            if (res[index - 1] < 0) {
                res[index] = element
            } else {
                res[index] = element + res[index - 1]
            }
        }
    }
    res.sort((a, b) => a < b)
    return res
}

console.log(soluation([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
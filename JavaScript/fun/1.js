// 奇偶排序
// input: [2,1,5,7,4,9,8,5,6] output: [1,5,7,9,5,2,4,8,6]
// 输入一个整数数组，期望输出的数组里，奇数在前边，偶数在后边

// 双指针
function sort(arr) {
    let i = 0,
        j = arr.length - 1
    while (i < j) {
        if (arr[i] % 2 == 0) {
            if (arr[j] % 2 == 1) {
                arr[i] = arr[i] + arr[j]
                arr[j] = arr[i] - arr[j]
                arr[i] = arr[i] - arr[j]
                j -= 1
                i += 1
            } else {
                j -= 1
            }
        } else {
            i += 1
        }
    }
    console.log(arr)
}
sort([2, 1, 5, 7, 4, 9, 8, 5, 6])
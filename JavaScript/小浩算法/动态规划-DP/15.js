/* 最长的上升子序列
[10,5,3,6,3,7,101,18]
 [2,3,7,101]
 */

function soluation(arr) {
    let res = [1]
    for (let index = 1; index < arr.length; index++) {
        const element = arr[index];
        if (element > arr[index - 1]) {
            res[index] = res[index - 1] + 1
        } else {
            res[index] = res[index - 1]
        }
    }
    return res[arr.length - 1]
}

console.log(soluation([10, 9, 2, 5, 3, 7, 101, 1, 1]))
/*
最短路径
let arr = [
    [1, 3, 1],
    [10, 5, 5],
    [4, 2, 1],
    [3, 10, 4]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
每个点都只能从右边或者上边移过来，比较这两个操作哪个距离更短
*/

function soluation(arr) {
    let res = []
    for (let i = 0; i < arr.length; i++) {
        const elements = arr[i];
        let rows = []
        for (let j = 0; j < elements.length; j++) {
            const element = elements[j];
            if (res.length == 0) {
                rows[j] = j == 0 ? element : (element + rows[j - 1])
            } else {
                rows[j] = j == 0 ? (res[j] + element) : (Math.min(element + rows[j - 1], element + res[j]))
            }
        }
        res = rows
    }
    return res
}
let arr = [
    [1, 3, 1],
    [10, 5, 5],
    [4, 2, 1],
    [3, 10, 4]
]
console.log(soluation(arr))
// 数组数字加1

function soluation(arr) {
    var plus = 0
    for (let index = arr.length - 1; index >= 0; index--) {
        if (index == arr.length - 1) {
            arr[index] += (1 + plus)
        } else {
            arr[index] += plus
        }
        if (arr[index] >= 10) {
            arr[index] = 0
            plus = 1
        } else {
            break
        }
    }
    if (arr[0] == 0 && plus == 1) {
        arr[0] = 0
        arr.unshift(1)
    }
    return arr
}

console.log(soluation([1, 0, 4, 9]))
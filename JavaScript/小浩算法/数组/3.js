// 股票售卖问题

function soluation(arr) {
    var buy = undefined
    var res = 0
    for (let index = 0; index < arr.length; index++) {
        let cur = arr[index]
        if (index < arr.length - 1) {
            let next = arr[index + 1]
            if (next <= cur) {
                if (buy != undefined) {
                    res += (cur - buy)
                    buy = undefined
                }
            } else {
                if (buy == undefined) {
                    buy = cur
                } else if (index == arr.length - 1 - 1) {
                    res += (next - buy)
                }
            }
        }
    }
    return res
}

// console.log(soluation([7, 1, 5, 3, 6, 4]))
console.log(soluation([1, 2, 3, 4, 5]))
console.log(soluation([5, 3, 2, 1]))
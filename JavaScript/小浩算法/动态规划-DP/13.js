// 上N阶梯子。每次能上1个或2个
// N(n) = N(n-1) + N(n-2)
// 动态规划问题总是将大问题化为一个个有关联的小问题

function soluation(n) {
    if (n == 1) {
        return 1
    }
    if (n == 2) {
        return 2
    }
    var arr = [1, 2]
    for (let index = 2; index < n; index++) {
        arr[index] = arr[index - 1] + arr[index - 2]
    }
    return arr
}

console.log(soluation(10))
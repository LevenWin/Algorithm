/*
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

*/

function soluation(arr, sum) {
    let map = new Map()
    let ai = -1, bi = -1
    var exit = false
    arr.map((v, i, a) => {
        if (exit == false) {
            if (map.get(sum-v) != undefined) {
                ai = i
                bi = map.get(sum - v)
                exit = true
            } else {
                map.set(v, i)
            }
        }
    })
    return [ai, bi]
}
console.log(soluation([3,3], 6))
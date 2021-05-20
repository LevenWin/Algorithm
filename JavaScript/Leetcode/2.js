/*
给你两个 非空 的数组，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的数组。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
*/

function soluation(arrA,arrB) {
    let maxLength = Math.max(arrA.length, arrB.length)
    let arrAi = arrA.length - 1
    let arrBi = arrB.length - 1
    let res = []
    let flag = 0
    for (let i = maxLength - 1; i >= 0; i --) {
        let sum = (arrAi < 0 ? 0 : arrA[arrAi]) + (arrBi < 0 ? 0 : arrB[arrBi])
        res.push((sum + flag) % 10)
        flag = Math.floor((sum + flag) / 10)
        arrAi -= 1
        arrBi -= 1
    }
    if(flag > 0) {res.push(flag)}
    return res
}

console.log(soluation([9,9,9,9,9,9,9], [9,9,9,9]))
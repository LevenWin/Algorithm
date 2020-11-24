/*
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
	 偷窃到的最高金额 = 1 + 3 = 4 。
*/

function soluation(arr) {
    let res = []
    for (let index = 0; index < arr.length; index++) {
        const element = arr[index];
        if (index == 0) {
            res = [
                [element, 0]
            ]
        } else {
            res.push(
                [
                    res[index - 1][1] + element,
                    Math.max(res[index - 1][1], res[index - 1][0])
                ]

            )
        }
    }
    // 得到被偷的元素
    var previous = 0
    var nums = []
    for (let index = res.length - 1; index >= 0; index--) {
        const element = res[index];
        if (index == res.length - 1) {
            if (element[0] > element[1]) {
                previous = 1
                nums.push(arr[index])
            }
        } else {
            if (previous == 1) {
                previous = 0
                continue
            } else {
                if (element[0] > element[1]) {
                    previous = 1
                    nums.push(arr[index])
                }
            }
        }
    }

    return nums.reverse()
}
console.log(soluation([2, 5, 4, 9, 30, 1]))
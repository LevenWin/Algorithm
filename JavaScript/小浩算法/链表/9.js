// 删除倒第N个节点
const common = require("../../common")

// 哨兵模式
function soluation(node, k) {
    var num = k
    var n = node
    var originNode = node
    do {
        n = n.next
        if (num == 0) {
            originNode = originNode.next
        } else {
            num -= 1
        }

    } while (num != 0 || n.next != undefined)
    originNode.next = originNode.next.next
}
let node = common.arrToLink([1, 2, 3, 4, 5])
soluation(node, 1)
console.log(node)
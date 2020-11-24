// 两数相加
const common = require("../../common")

function soluation(node1, node2) {
    let plus = 0
    let tail = {}
    let head = tail
    let noneNode = { "val": 0 }
    while (node1.next != undefined || node2.next != undefined) {
        node1 = node1.next == undefined ? noneNode : node1.next
        node2 = node2.next == undefined ? noneNode : node2.next
        var res = node1.val + node2.val + plus
        if (res > 9) {
            plus = 1
            res = res % 10
        } else {
            plus = 0
        }
        tail.next = {}
        tail = tail.next
        tail.val = res
    }
    if (plus > 0) {
        tail.next = {}
        tail = tail.next
        tail.val = plus
    }
    return head
}
console.log(soluation(common.arrToLink([1, 3, 4]), common.arrToLink([9, 7, 6, 5])))
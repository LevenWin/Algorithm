// 206. 反转链表
const common = require("./common")

function soluation(node) {
    if (node.next.val == undefined) {
        return [node, node]
    }
    let result = soluation(node.next)
    result[0].next = node
    return [node, result[1]]
}

function soluation2(node) {
    var tmp = undefined
    do {
        let a = node.next
        node.next = tmp
        tmp = node
        node = a
    } while (node.val != undefined);
    return tmp
}

let l = common.arrToLink([1, 2, 3, 4], )
let node = soluation2(l)
console.log(node)
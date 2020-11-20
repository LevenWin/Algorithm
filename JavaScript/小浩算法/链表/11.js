// 无重复值节点
// 检测环
const common = require("../../common")

function soluation(node) {
    let node1 = node
    let node2 = node
    do {
        node1 = node1.next
        node2 = node2.next.next

    } while (node1.val != node2.val && node1 != undefined && node2 != undefined)
    if (node1.val == node2.val) {
        return true
    } else {
        return false
    }
}

function soluation1(node) {
    let map = {}
    while (node != undefined) {
        if (map[node.val] != undefined) {
            return true
        }
        map[node.val] = node.val
        node = node.next
    }
    return false

}

// 检测环节点
function soluation2(node) {
    let map = {}
    let previous = node.next
    node = node.next.next
    while (node != undefined && map[node.val] != previous.val) {
        map[node.val] = previous.val
        previous = node
        node = node.next
    }
    if (node != undefined) {
        return previous.val
    }
    return undefined
}
// 找到相交点时，思考快慢指针走的距离的特点。
function soluation3(node) {
    let node1 = node
    let node2 = node
    var exitCircle = false
    do {
        if (exitCircle == true) {
            node1 = node1.next
            node2 = node2.next
        } else {
            node1 = node1.next
            node2 = node2.next.next
        }
        if (node1.val == node2.val) {
            if (exitCircle == false) {
                exitCircle = true
                node2 = node
            } else {
                break
            }
        }
    } while (node1 != undefined && node2 != undefined)

    if (node1.val == node2.val) {
        return node1.val
    } else {
        return undefined
    }
}

// 造环
function makeCircle(node1, node2) {
    let head1 = node1
    let head2 = node2
    while (node1.next != undefined) {
        node1 = node1.next
    }

    while (node2.next != undefined) {
        node2 = node2.next
    }

    node1.next = head2.next
    node2.next = node1
    return head1
}

let node1 = common.arrToLink([1, 2, 3, 4])
let node2 = common.arrToLink([5, 6, 7, 8])

let node = makeCircle(node1, node2)
console.log(soluation3(node))
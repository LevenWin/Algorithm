// 116. 填充每个节点的下一个右侧节点指针
const common = require("../JavaScript/common")
    // 1
function soluation(nodeArr, i) {
    if (nodeArr.length == 0) {
        return
    }
    let n = nodeArr.shift()
    if (nodeArr.length == 0) {
        n.next = null
    } else {
        n.next = nodeArr[0].val
    }
    if (n.left != undefined) {
        nodeArr.push(n.left)
    }
    if (n.right != undefined) {
        nodeArr.push(n.right)
    }

    soluation(nodeArr, i + 1)
}

function setNullForRightBorder(node) {
    if (node.right != undefined) {
        node.right.next = undefined
        setNullForRightBorder(node.right)
    }
}
// 2
function soluation2(node) {
    if (node == undefined || node.left == undefined) {
        return undefined
    }
    node.left.next = node.right
    node.right.next = node.next == null ? null : node.next.left
    soluation2(node.left)
    soluation2(node.right)
}

// 1 + 2 + 4 + 8 = 2
let node = common.stringToTree({ "s": common.nodeString })
soluation2(node)
console.log(node)
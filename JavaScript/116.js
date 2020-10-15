// 116. 填充每个节点的下一个右侧节点指针
const common = require("../JavaScript/common")

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
// 1 + 2 + 4 + 8 = 2
let node = common.stringToTree({ "s": common.nodeString })
soluation([node], 1)
setNullForRightBorder(node)
console.log(node)
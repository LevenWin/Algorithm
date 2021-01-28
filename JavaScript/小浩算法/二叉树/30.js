// BST Binary Search Tree 搜索二叉树
// 找到指定节点
const common = require("../../common")

function soluation(node, value) {
    if (node == undefined) { return }
    if (node.val == value) {
        return node
    }
    if (value > node.val) {
        return soluation(node.right, value)
    } else {
        return soluation(node.left, value)
    }
}

function soluation2(node, value) {
    while (node != undefined && node.val != value) {
        if (node.val > value) {
            node = node.left
        } else {
            node = node.right
        }
    }
    return node
}
let node = common.stringToTree({ "s": "4!3!?!?!6!5!?!?!7!?!?!" })
console.log(soluation2(node, 7))
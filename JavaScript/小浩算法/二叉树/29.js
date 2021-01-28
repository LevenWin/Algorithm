// BST Binary Search Tree 搜索二叉树
// 左子节点小于父节点，右子节点大于父节点
const common = require("../../common")

// 递归
function isBST(node, min, max) {
    if (node == undefined) { return true }
    if (node.val < min || node.val > max) { return false }
    if (isBST(node.left, min, node.val)) {
        return isBST(node.right, node.val, max)
    }
    return false
}

let node = common.stringToTree({ "s": "4!3!?!?!6!3!?!?!7!?!?!" })
console.log(isBST(node, -1000, 10000))
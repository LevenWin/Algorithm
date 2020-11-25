// 226. 翻转二叉树
const common = require("../JavaScript/common")

function soluation(node) {
    if (node == undefined) {
        return node
    }
    let left = node.left
    let right = node.right
    soluation(node.left)
    soluation(node.right)
    node.left = right
    node.right = left
    return node
}

function soluation2(node) {
    if (node == undefined) {
        return node
    }
    let arr = Array(node)
    while (arr.length > 0) {
        let item = arr.pop()
        if (item.left != undefined) {
            arr.push(item.left)
        }
        if (item.right != undefined) {
            arr.push(item.right)
        }
        let left = item.left
        let right = item.right
        item.left = right
        item.right = left
    }
}

let node = common.stringToTree({ "s": common.nodeString })
soluation(node)
console.log(node)
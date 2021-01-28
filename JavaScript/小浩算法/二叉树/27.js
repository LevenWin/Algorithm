const common = require("../../common")

// 递归
function soluation(node) {
    if (node == undefined) {
        return 0
    }
    let count1 = soluation(node.left) + 1
    let count2 = soluation(node.right) + 1
    return Math.max(count1, count2)
}

let node = common.stringToTree({ "s": "3!9!?!?!20!15!?!?!7!?!?!" })
console.log(soluation(node))
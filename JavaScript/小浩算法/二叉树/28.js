// BFS
// 广度优先遍历二叉树
const common = require("../../common")

// 广度搜索
function bfs(node) {
    let arr = [node]
    while (arr.length > 0) {
        let n = arr.shift()
        console.log(n.val)
        if (n.left != undefined) {
            arr.push(n.left)
        }
        if (n.right != undefined) {
            arr.push(n.right)
        }
    }
}


// 深度搜索
function dfs(node) {
    let arr = [node]
    while (arr.length > 0) {
        let n = arr.shift()
        console.log(n.val)
        if (n.right != undefined) {
            arr.unshift(n.right)
        }
        if (n.left != undefined) {
            arr.unshift(n.left)
        }

    }
}
let node = common.stringToTree({ "s": "3!9!8!?!?!?!20!15!?!?!7!?!?!" })
bfs(node)
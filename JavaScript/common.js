function stringToTree(s) {
    if (s.s.length == 0) {
        return undefined
    }
    let sArr = s.s.split("!")
    let headValue = sArr[0]
    let newsArr = sArr.slice(1)
    s.s = newsArr.join("!")
    if (headValue == "?") {
        return undefined
    } else {
        let node = {}
        node.val = headValue
        node.left = stringToTree(s)
        node.right = stringToTree(s)
        return node
    }
}

function treeToString(s, n) {
    if (n == undefined) {
        return s + "?!"
    }
    s = s + String(n.val) + "!"
    s = treeToString(s, n.left)
    s = treeToString(s, n.right)
    return s
};

function arrToLink(arr) {
    var node = {}
    var head = node
    for (let item in arr) {
        node.val = arr[item]
        node.next = {}
        node = node.next
    }
    return head
}
let nodeString = "1!2!4!?!?!5!?!?!3!6!?!?!7!?!?!"

module.exports = {
    stringToTree,
    treeToString,
    nodeString,
    arrToLink
}
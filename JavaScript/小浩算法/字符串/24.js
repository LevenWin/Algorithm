/*
字符串匹配
*/

// BF算法，也称为暴力算法，一次一个个匹配
function soluation1(origin, aim) {
    let i = 0
    let j = 0
    while (i < origin.length && j < aim.length) {
        if (origin[i] == aim[j]) {
            i += 1
            j += 1
        } else {
            i -= j - 1
            j = 0
        }
    }
    if (j == aim.length) {
        return i - j
    } else {
        return 0
    }
}
console.log(soluation1("laelao", "lao"))
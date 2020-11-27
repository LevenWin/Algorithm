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


function next2(string) {
    let i = 1
    let j = 0
    let arr = {}
    arr[i] = 0
    while (i < string.length) {
        // j === 0 代表回溯到了第一个点
        if (j == 0 || string[i - 1] == string[j - 1]) {
            i += 1
            j += 1
            arr[i] = j
        } else {
            j = arr[j] // 回溯自身
        }
    }
    return arr
}

function soluation2(string, aim) {
    let i = 1
    let j = 1
    let nextArr = next1(aim)
    while (i <= string.length && j <= aim.length) {
        if (string[i - 1] == aim[j - 1]) {
            i += 1;
            j += 1;
        } else {
            if (j == 1) {
                i += 1
            } else {
                j = nextArr[j]
            }

        }
    }
    if (j > aim.length) {
        return i - aim.length
    }
    return -1
}

// KMP算法
console.log(soluation2("aabbaaaabbccaass", "aabbccaa"))
    // console.log(soluation2("laelao", "w"))
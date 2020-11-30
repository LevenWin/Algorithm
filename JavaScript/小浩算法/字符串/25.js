// 旋转字符串匹配

function soluation(a, b) {
    if (a.length != b.length) {
        return false
    }
    var i = 0
    var j = 0
    var res = 0
    while (i < a.length) {
        while (a[i] == b[j]) {
            i += 1
            j += 1
            res += 1
            if (res == a.length) {
                return true
            }
            if (i == a.length) {
                i = 0
            }
            if (j == b.length) {
                j = 0
            }
        }
        j = 0
        res = 0
        i += 1
    }
    return false
}

function soluation2(a, b) {
    if (a.length != b.length) {
        return false
    }
    var c = a + a
    let next = function(string) {
        let i = 1
        let j = 0
        let arr = {}
        arr[i] = 0
        while (i < string.length) {
            if (j == 0 || string[i - 1] == string[j - 1]) {
                j += 1
                i += 1
                arr[i] = j
            } else {
                j = arr[j]
            }
        }
        return arr
    }
    let kmp = function(string, aim, next) {
        let i = 1
        let j = 1
        while (i <= string.length && j <= aim.length) {
            if (string[i - 1] == aim[j - 1]) {
                i += 1
                j += 1
            } else {
                if (j = 1) {
                    i += 1
                } else {
                    j = next[j]
                }

            }
        }
        if (j == aim.length + 1) {
            return true
        }
        return false
    }
    return kmp(c, b, next(b))
}

console.log(soluation2("abcde", "deabc"))
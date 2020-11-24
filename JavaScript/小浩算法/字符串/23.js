// 回文字符串
// 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

function soluation(string) {
    let start = 0
    let end = string.length - 1

    let check = function(s) {
        let code = s.charCodeAt()
        if ((code >= "A".charCodeAt() && code <= "Z".charCodeAt()) || (code >= "a".charCodeAt() && code <= "z".charCodeAt()) || (code >= 0 && code <= 9)) {
            return 1
        } else {
            return 0
        }
    }
    while (start <= end) {
        let startStr = string[start]
        let endStr = string[end]
        if (check(startStr) == 0) {
            start += 1
            continue
        }
        if (check(endStr) == 0) {
            end -= 1
            continue
        }
        if (startStr.toUpperCase() == endStr.toUpperCase()) {
            start += 1
            end -= 1
        } else {
            return 0
        }
    }
    return 1
}

console.log(soluation("A man, a plan, a canal: Panama"))
console.log(soluation("race a car"))
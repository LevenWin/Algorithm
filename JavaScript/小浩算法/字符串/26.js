// 最后一个单词

function soluation(string) {
    var i = string.length - 1
    var count = 0
    while (i >= 0) {
        let tmp = string.slice(i, i + 1)
        i -= 1
        if (tmp == " ") {
            if (count == 0) {
                continue
            }
            break

        }
        count += 1
    }
    return string.length - (string.length - i - 1 - 1)
}

console.log(soluation("i am good  q  q"))
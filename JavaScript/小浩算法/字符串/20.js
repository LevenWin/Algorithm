// 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1 。
//  您可以假定该字符串只包含小写字母

function soluation(sArr) {
    let res = []
    for (let index = 0; index < sArr.length; index++) {
        const element = sArr[index]
        let findIndex = res.findIndex(a => a == element)
        if (findIndex >= 0) {
            res.splice(findIndex, 1)
        } else {
            res.push(element)
        }
    }
    return res
}

function soluation2(sArr) {
    let res = {}
    for (let index = 0; index < sArr.length; index++) {
        const element = sArr[index];
        res[element] = index
    }

    for (let index = 0; index < sArr.length; index++) {
        const element = sArr[index];
        if (res[element] == index) {
            return { element, index }
        }
    }
}

console.log(soluation2("leetcodelova"))
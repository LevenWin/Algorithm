// 反转字符串

function soluation(sArr) {
    for (let index = 0; index <= (sArr.length - 1) / 2; index++) {
        if (index == (sArr.length - 1) / 2 && sArr.length % 2 == 1) {
            return sArr
        }
        sArr[index] = sArr[sArr.length - 1 - index] + sArr[index]
        sArr[sArr.length - 1 - index] = sArr[index] - sArr[sArr.length - 1 - index]
        sArr[index] = sArr[index] - sArr[sArr.length - 1 - index]

    }
    return sArr
}

console.log(soluation([1, 2, 3, 4, 5]))
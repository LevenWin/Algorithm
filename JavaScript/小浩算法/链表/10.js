//  合并有序数组

function soluation(aArr, bArr) {
    let nArr = []
    let i = 0
    let j = 0
    console.log(aArr.length)
    while (i < aArr.length && j < bArr.length) {
        if (aArr[i] < bArr[j]) {
            nArr.push(aArr[i])
            i += 1
        } else if (aArr[i] > bArr[j]) {
            nArr.push(bArr[j])
            j += 1
        } else {
            nArr.push(aArr[i])
            i += 1
            nArr.push(bArr[j])
            j += 1
        }
    }
    if (i < aArr.length) {
        nArr = nArr.concat(aArr.slice(i, aArr.length))
    }
    if (j < bArr.length) {
        nArr = nArr.concat(bArr.slice(j, bArr.length))
    }
    return nArr
}

console.log(soluation([1, 2, 4, 6, 8, 9], [3, 5, 6, 7]))
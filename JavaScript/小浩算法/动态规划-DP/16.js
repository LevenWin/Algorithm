/*
三角形的最小路径和
*/

function soluation(arr) {
    let res = []

    for (let i = 0; i < arr.length; i++) {
        const elements = arr[i];
        let temArr = []

        for (let j = 0; j < elements.length; j++) {
            const element = elements[j];
            if (res.length == 0) {
                temArr[j] = element
            } else {
                let left = j - 1
                let right = j
                if (left < 0) { left = 0 }
                if (right > res.length - 1) { right = res.length - 1 }
                temArr[j] = Math.min(res[left], res[right]) + element
            }
        }
        res = temArr
    }
    return res
}
let arr = [
    [2],
    [3, 4],
    [10, 10, 10],
    [4, 1, 8, 5],
    [5, 20, 6, 2, 0]
]
console.log(soluation(arr))
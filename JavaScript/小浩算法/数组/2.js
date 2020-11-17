// 最长公共前缀
// 例如 ["abs", "aba", "abb"]
// 输出 "ab"

function soluation1(arr) {
    var short = arr.shift()
    arr.forEach((v, i) => {
        if (short.length > v.length) {
            short = v
        }
    });
    var res = ""
    for (let index = 0; index < short.length; index++) {
        const element = short[index];
        arr.forEach((v, i) => {
            if (v[index] != element) {
                return res
            } else if (i == arr.length - 1) {
                res += element
            }
        });
    }
    return res
}
console.log(soluation1(["abs", "aba", "abc", "abab"]))
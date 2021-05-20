// 692. 前K个高频单词
// 输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
// 输出: ["i", "love"]
// 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
//     注意，按字母顺序 "i" 在 "love" 之前。

function soluation(arr, k) {
    let dict = new Map()
    arr.forEach(ele => {
        dict.set(ele, dict.get(ele) ? dict.get(ele) + 1 : 1)
    });
    return [...dict.keys()].sort((a, b) => {
        let ca = dict.get(a), cb = dict.get(b)
        if (ca == cb) {
            return a > b ? 1 : -1
        }
        return cb - ca
    }).slice(0, k)

}

console.log(soluation(["i", "love", "leetcode", "i", "love", "coding"], 3))

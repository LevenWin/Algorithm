/*
实现 strStr() 函数。给定一个 haystack 字符串和一个 needle 字符串，
在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回 -1。

输入: haystack = "hello", needle = "ll"
输出: 2

输入: haystack = "aaaaa", needle = "bba"
输出: -1
*/

/*
Sunday 匹配
核心思想：在匹配的过程中，模式串发现不匹配的时候，算法尽可能的跳过更多的字符以进行下一次的匹配，从而提高效率
*/

function soluation(origin, aim) {
    if (origin.length == 0 || aim.length == 0) { return -1 }
    if (origin.length < aim.length) { return -1 }
    var originIndex = 0
    var aimIndex = 0
    var startIndex = 0
    while (aimIndex < aim.length && originIndex < origin.length) {
        if (origin[originIndex] == aim[aimIndex]) {
            originIndex += 1
            aimIndex += 1
        } else {
            startIndex = startIndex + aim.length
            if (startIndex > origin.length - 1) {
                return -1
            }
            let findIndex = aim.lastIndexOf(origin[startIndex])
            if (findIndex > -1) {
                startIndex -= findIndex
                aimIndex = 0
                originIndex = startIndex
            } else {
                startIndex = startIndex + 1
                originIndex = startIndex
                aimIndex = 0
            }
        }
    }
    if (aimIndex == aim.length) {
        return startIndex
    } else {
        return -1
    }
}

console.log(soluation("nwoaoaooaoya", "ooa"))
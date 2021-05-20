/*
无重复字符的最长子串
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
*/

function soluation(string) {
    var left = 0, maxlength = 0

    for (let index = 0; index < string.length; index++) {
        if (index == 0) {
            maxlength = 1
        } else {
            for (let j = left; j < index; j++) {
                if (string[j] == string[index]) {
                    left = j+1
                    break
                }
                
            }
            maxlength = Math.max(maxlength, index - left + 1)
        }        
    }
    return maxlength
}                   

console.log(soluation("pwwkew"))
//205. 同构字符串

function soluation(a, b) {
    if (a.length != b.length) {
        return false
    }
    for (let i = 0; i < a.length; i++) {
        for (let j = 0; j < i; j++) {
            if ((a[i] != a[j]) && (b[i] != b[j])) {
                continue
            } else if ((a[i] == a[j]) && (b[i] == b[j])) {
                continue
            } else {
                return false
            }
        }
    }
    return true
}
// 2
var isIsomorphic2 = function(s, t) {
    for (let i = 0; i < s.length; i++) {
        let subS = s[i]
        let a = s.indexOf(s[i])
        let b = t.indexOf(t[i])
        if (a != b) {
            return false;
        }
    }
    return true;
}

console.log(isIsomorphic2("abba", "abab"))
console.log(soluation("abba", "abab"))
/*
N型翻转

leetcodeishiring row = 4
l  d  r
e oe ii
ec ih n
t  s  g

out: ldreoeiiecihntsg
*/
/*
x * 4 + row - 2 = [0...row - 1]

*/
function soluation(string, row) {
    let nArr = []
    for (let index = 0; index < row; index++) {
        nArr.push([])
    }

    function covert(index, rowNum) {
        let x = Math.floor(index / (row + rowNum - 2))
        let y = Math.floor(index % (row + rowNum - 2))
        if (y < rowNum) {
            let column = x * (rowNum - 1) + 0
            let row = y
            return { column, row }
        } else {
            let column = x * (rowNum - 2) + y - rowNum + 1
            let row = rowNum - 2 - (y - rowNum)
            return { column, row }
        }
    }


    for (let index = 0; index < string.length; index++) {
        let res = covert(index, row)
        nArr[res.row].push(string[index])
    }
    var s = ""
    nArr.forEach((a, b) => {
        a.forEach((v, k) => {
            s += v
        })
    })
    return s
}

console.log(soluation("LEETCODEISHIRING", 3))
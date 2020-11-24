/*
大数输出
输入数字 n，输出n位数的前1000个数
*/

function soluation(a) {
    let num = 1000
    var origin = [1]
    if (a == 1) {
        origin = [0]
    }
    for (let index = 0; index < a - 1; index++) {
        origin.push(0)
    }
    var plus = 0
    for (let index = 0; index < num; index++) {
        var j = a - 1
        origin[j] += 1
        plus = Math.floor(origin[j] / 10)
        while (plus > 0) {
            origin[j] = origin[j] % 10
            j -= 1
            origin[j] += plus
            plus = Math.floor(origin[j] / 10)
        }
        console.log(origin.join(""))
    }

}

soluation(50)
// 数组存在两数之和等于某个值

function soluation(arr, sum) {
    let map = {}
    let narr = []
    arr.forEach((v, key) => {
        if (map[sum - v] == 0) {
            narr.push(v, sum - v)
            return;
        }
        map[v] = 0
    });
    return narr
}
// console.log(soluation([1, 4, 5, 6], 5))
// [-1, 0, 1, 2, -1, -4] 0
//  [-4, -1, -1, 0, 1, 2] 0
//  [-4, -1, -1, 0, 1, 2, 2, 3] 0
// 3数之和等于某值
function soluation2(arr, sum) {
    let nArr = []
    for (let index = 0; index < arr.length; index++) {
        const element = arr[index];
        let res = soluation(arr.slice(index + 1), sum - element)
        if (res.length > 0) {
            res.push(element)
            res.sort((a, b) => a - b)
            if (nArr.indexOf(res) < 0) {
                nArr.push(res)
            }
        }
    }
    return nArr
}

function soluation3(arr, sum) {
    arr.sort((a, b) => a - b)
    let nArr = []
    for (let index = 0; index < arr.length; index++) {
        const element = arr[index];
        let l = index + 1
        let r = arr.length - 1
        let target = sum - element
        if (index < arr.length - 2 && (index > 0 && element != arr[index - 1])) {
            do {
                if (arr[l] + arr[r] == target) {
                    nArr.push([element, arr[l], arr[r]])
                    while (l < r && arr[l] == arr[l + 1]) {
                        l += 1
                    }
                    while (l < r && arr[r] == arr[r - 1]) {
                        r -= 1
                    }
                    l += 1
                    r -= 1
                } else if (arr[l] + arr[r] < target) {
                    l += 1
                } else {
                    r -= 1
                }
            } while (l < r)
        }
    }
    return nArr
}

console.log(soluation3([-1, 0, 1, 2, -1, -4, -2, 1, 2], 0))
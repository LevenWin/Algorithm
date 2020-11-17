// 移动数组

function soluation(arr, k) {
    arr = arr.slice(arr.length - k).concat(arr)
    arr = arr.slice(0, arr.length - k)
    return arr
}

function soluation2(arr, k) {
    for (let index = 0; index < k; index++) {
        let value = arr[arr.length - 1]
        for (let j = arr.length - 1; j > 0; j--) {
            arr[j] = arr[j - 1]
        }
        arr[0] = value
    }
    return arr
}

function soluation3(arr, k) {
    function reverse(arr, f, e) {
        for (let index = f; index <= ((e - f - 1) / 2 + f); index++) {
            const element = arr[index];
            arr[index] = arr[e - index + f - 1]
            arr[e - index + f - 1] = element
        }
        return arr
    }
    reverse(arr, 0, arr.length)
    reverse(arr, 0, k)
    reverse(arr, k, arr.length)
    return arr
}


/*
k = 5
[ 1, 2, 3, 4, 5, 6, 7 ]

[ 7, 2, 3, 4, 5, 6, 1]

[ 7, 6, 5, 4, 3, 2, 1 ]

[ 3, 4, 5, 6, 7, 1, 2 ]

*/
console.log(soluation3([1, 2, 3, 4, 5, 6, 7], 5))
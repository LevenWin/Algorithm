// O1额外空间复杂度删除数组指定元素，并返回处理后数组长度

function soluation(arr, v) {
    for (let index = 0; index < arr.length;) {
        const element = arr[index];
        if (element == v) {
            arr = arr.slice(0, index).concat(arr.slice(index + 1, arr.length))
        } else {
            index++;
        }
    }
    return arr
}

// 有序数组删除重复数字 

console.log(soluation([2, 3, 4, 1, 2, 4], 2))
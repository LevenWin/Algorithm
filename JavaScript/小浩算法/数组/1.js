// 求数组的交集
// 例如 let nums1 = [1,2,3], nums2 = [1, 3]
// 交集为 nums = [1, 3]

function soluation1(arr1, arr2) {

    let sArr, bArr
    if (arr1.length > arr2.length) {
        sArr = arr2
        bArr = arr1
    } else {
        sArr = arr1
        bArr = arr2
    }

    var nArr = []
    for (let index = 0; index < sArr.length; index++) {
        for (let j = 0; j < bArr.length; j++) {
            if (bArr[j] == sArr[index]) {
                nArr.push(bArr[j])
            }
        }
    }
    return nArr
}
// 数值命中的问题可以考虑 map来空间换时间
function soluation2(arr1, arr2) {
    let map = {}
    arr2.forEach((v, i) => {
        if (map[v] == undefined) {
            map[v] = 1
        } else {
            map[v] += 1
        }
    });

    let nArr = []
    arr1.forEach((v, i) => {
        if (map[v] > 0) {
            map[v] = 0 // map[v] -= 1 输出具有重复的数据
            nArr.push(v)
        }
    });
    return nArr

}


// 进阶 两个有序从小到大的数组，求重叠数组
// 例如 let num1 = [1, 4, 6, 7, 8], num2 = [1, 6, 8]
// 重叠数组为 num = [1, 6, 8]

// 双指针
function soluation3(arr1, arr2) {
    var nArr = []
    var i = 0,
        j = 0
    for (; i < arr1.length;) {
        const ele1 = arr1[i];
        const ele2 = j == arr2.length ? arr2[j - 1] : arr2[j]
        if (ele1 > ele2) {
            j += 1
            if (j == arr2.length) {
                break
            }
        } else if (ele1 < ele2) {
            i += 1
        } else {
            nArr.push(ele1)
            i += 1
            j += 1
        }
    }
    return nArr
}

let nums2 = [1, 3, 4, 6, 8, 20],
    nums1 = [1, 2, 3, 4, 10, 12, 20]
let nums = soluation3(nums1, nums2)
console.log(nums)
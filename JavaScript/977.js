// 977. 有序数组的平方
function soluation(A) {
    for (let i = 0; i < A.length; i++) {
        A[i] = A[i] * A[i]
        for (let j = i - 1; j >= 0; j--) {
            if (A[j] > A[j + 1]) {
                let tmp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = tmp
            }
        }
    }
    return A
}
console.log(soluation([-4, -1, 0, 3, 10]))
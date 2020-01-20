# -*- coding: UTF-8 -*-


# O(n*n)
def f1(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    r = f1(n-1) + f1(n-2)
    return r

# O(n)
def f2(n):
    n1 = 1
    n2 = 1
    if n < 0 :
        return 0
    if n == 1 or n == 2:
        return n1
    res = n1 + n2
    for i in range(3, n + 1):
        res = n1 + n2
        n1 = n2
        n2 = res
    return res
# n(logn)
def f3(n):
    pass

if __name__ == "__main__":
    print(str(f2(11)))
    print(str(f1(11)))


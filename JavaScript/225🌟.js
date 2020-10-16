// 用队列实现栈

class Stack {

    constructor() {
        this._list = []
    }

    push(x) {
        this._list.push(x)
    }
    pop(x) {
        return this._list.pop()
    }
    top(x) {
        return this._list[this._list.length - 1]
    }
    empty() {
        return this._list.length == 0
    }
}
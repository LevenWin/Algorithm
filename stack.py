class Stack(object):
    def __init__(self, data = []):
        self.dataList = data
    def peek(self):
        if self.isEmpty():
            return 0
        else:
            return self.dataList[-1]
    def push(self, obj):
        self.dataList.append(obj)
    def pop(self):
        return self.dataList.pop()
    def isEmpty(self):
        return len(self.dataList) == 0



        


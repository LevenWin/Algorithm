class Stack(object):
    dataList = []
    def peak(self):
        if self.isEmpty():
            return None
        else:
            return self.dataList[-1]
    def push(self, obj):
        self.dataList.append(obj)
    def pop(self):
        return self.dataList.pop()
    def isEmpty(self):
        return len(self.dataList) == 0



        


 # -*- coding: UTF-8 -*-

class DQueue(object):
    def __init__(self):
        self.dataList = []
    def pollHead(self):
        return self.dataList.pop(0)
    def pollTail(self):
        return self.dataList.pop()
    def peekTail(self):
        return self.dataList[-1]
    def peekHead(self):
        return self.dataList[0]
    def addTail(self, obj):
        self.dataList.append(obj)
    def isEmpty(self):
        return len(self.dataList) == 0
    

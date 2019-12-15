# -*- coding: UTF-8 -*-

class LinkNode(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.previous = None
class LinkedLink(object):
    def __init__(self):
        self.dataList = []
        self.head = LinkNode()
        self.end = self.head
        self.count = 0
    def addList(self,l):
        for i in l:
            self.add(LinkNode(i))
        
    def __str__(self):
        p = "H"
        h = self.head.next
        while h != None:
           p = p + "->" + str(h.value)
           h = h.next
        p = p + "->E"
        return p

    def add(self, node):
        node.previous = self.end
        self.end.next = node     
        self.count = self.count + 1
        self.end = node
    def peekHead(self):
        return self.head
    def peekEnd(self):
        return self.end
    def isEmpty(self):
        return self.count == 0
    def removeEnd(self):
        if self.isEmpty() == False:
            previous = self.end.previous
            previous.next = None
            self.end = previous
            return previous
        return None
    def removeHead(self):
        if self.isEmpty() == False:
            next = self.head.next
            next.previous = self.head
            self.head.next = next
            return next
        return None
    
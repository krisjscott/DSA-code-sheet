class dequeue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    def insertAtLast(self, value):
        self.items.append(value)
    def insertAtFirst(self,value):
        self.items.insert(0,value)
    def deleteAtFront(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.items.pop(0)
    def deleteAtBack(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.items.pop()
    def printll(self):
        print(self.items)

q = dequeue()
q.insertAtFirst(0)
q.printll()
q.insertAtLast(1)
q.printll()
q.insertAtLast(2)
q.insertAtFirst(-1)
q.printll()

print(q.deleteAtBack())
q.printll()
print(q.deleteAtFront())
q.printll()



class queue:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items) == 0
    def insert(self, value):
        self.items.append(value)
    def delete(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.items.pop(0)
    def printll(self):
        print(self.items)
    
q = queue()
q.insert(0)
q.insert(1)
q.insert(2)
q.printll()
q.insert(3)
print(q.delete())
q.printll()
print(q.delete())
q.printll()
print(q.delete())
print(q.delete())
q.printll()
# print(q.delete())




class CircularQueue:
    def __init__(self,size):
        self.items = [None]*size
        self.size = size
        self.front = self.rear = -1
    
    def isEmpty(self):
        return self.items==None
    
    def insert(self,value):
        if ((self.rear+1) % self.size == self.front):
            print("Queue is Full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.items[self.rear] = value
        else:
            self.rear = (self.rear+1) % self.size
            self.items[self.rear] = value
    
    def delete(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.rear == self.front:
            print(self.items[self.front])
            self.front = self.rear = -1
        else:
            print(self.items[self.front])
            self.front = (self.front+1) % self.size
    def printll(self):
        print(self.items)
    

obj=CircularQueue(5)
obj.insert(1)
obj.insert(2)
obj.insert(3)
obj.insert(4)
obj.insert(5)
# obj.insert(6)
obj.printll()
obj.delete()
obj.insert(6)
obj.insert(7)
obj.printll()

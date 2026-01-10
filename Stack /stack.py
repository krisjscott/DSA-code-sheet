class stack:
    def __init__(self):
        self.s=[]

    def length(self):
        return len(self.s)
    def push(self,value):
        self.s.append(value)
    def peek(self):
        if len(self.s) == 0:
            raise Exception("stack empty")
        return self.s[-1]
    def pop(self):
        if len(self.s) == 0:
            raise Exception("stack empty")
        return self.s.pop()

obj = stack()
obj.push(0)
obj.push(1)
obj.push(2)
obj.push(3)

print(obj.peek())
print(obj.length())
print(obj.pop())
print(obj.pop())
print(obj.peek())

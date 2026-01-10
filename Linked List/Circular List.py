class Node:
    def __init__(self, info, next=None):
        self.data=info
        self.next=None
class circular:
    def __init__(self, head=None):
        self.head=head

    def insertion(self, value):
        t = Node(value)
        if (self.head==None):
            self.head=t
            t.next=self.head
            return 
        temp = self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next = t
        t.next = self.head
    
    def insertionAtStart(self,value):
        temp=Node(value)
        t=self.head
        if self.head is None:
            self.head=temp
            temp.next=self.head
            return
        while t.next!=self.head:
            t=t.next
        temp.next=self.head
        t.next=temp
        self.head=temp

    def insertionBasedValue(self,value,x):
        temp=Node(value)
        t=self.head
        while t.next!=self.head:
            if t.data == x:
                temp.next=t.next
                t.next=temp
            t=t.next

    def printFF(self):
        if self.head is None:
            return
        t = h = self.head
        
        # if t.next is None:
        #     return t
        
        while(t.next!=self.head):
            print(t.data, end = " --> ")
            t=t.next
        print(f"{t.data} --> {h.data}")
        

obj = circular()
obj.insertion(10)
obj.insertion(20)
obj.insertion(30)
obj.insertionAtStart(5)
obj.insertionBasedValue(15,10)
obj.printFF()
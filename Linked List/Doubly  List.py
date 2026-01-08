class Node:
    def __init__(self,value=None):
        self.data = value #same value passed in function
        self.next = None #Initalizing next pointer to None
        self.prev = None #Initalizing prev pointer to None
class DoublyList:
    def __init__(self):
        self.head=None
    
    def insetionAtEnd(self,value):
        t = Node(value)
        if (self.head==None):
            self.head=t
            return 
        temp = self.head
        while temp.next!=None:
            temp=temp.next
        temp.next = t
        t.prev = temp
    
    def insertAtBegin(self,value):
        t = Node(value)
        if (self.head == None):
            self.head=t
            return
        t.next=self.head
        self.head.prev=t
        self.head = t
    
    def insertionAtMiddle(self,value,x):#Value: Value which needs to be added; x: Value at which VALUE needs to be added after the 'x'
        t = self.head
        while(t.next!=None):
            if(t.data == x):
                break
            else:
                t=t.next
        temp = Node(value)

        temp.next=t.next
        t.next.prev=temp
        t.next=temp
        temp.prev=t
    
    def deletion(self,value):
        if self.head==None:
            print("Link list is empty")
            return 
        
        t=self.head

        if t.data==value:
            self.head=t.next
            self.next.prev=None
            return 
        while (t.next!=None):
            if t.data==value:
                t.prev.next=t.next
                t.next.prev=t.prev
                return
            else:
                t=t.next #if data not found, just move the pointer t to next element
        if(t.data==value):
            t.prev.next=None
            return
            
        

    def printFF(self):
        t = self.head
        while(t.next!=None):
            print(t.data, end = " <--> ")
            t=t.next
        print(t.data)

obj=DoublyList()
obj.insetionAtEnd(10)
obj.insetionAtEnd(20)
obj.insetionAtEnd(30)
obj.insertAtBegin(5)
obj.insertionAtMiddle(25,20)
obj.deletion(30)
obj.printFF()

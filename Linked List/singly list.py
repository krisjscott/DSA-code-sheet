class NODE:
    def __init__(self, info, next=None):
        self.data=info
        self.next=next
class singlylinkedlist:
    def __init__(self, head=None):
        self.head=head
     
    def insertAtEnd(self,value):
        temp = NODE(value)
        if(self.head!=None):
            t = self.head
            while(t.next!=None):
                t=t.next
            t.next=temp
        else:
            self.head=temp
    def deleteValue(self,value):
        temp=NODE(value)
        t=self.head
        prev=t
        if(t.data==value):
            self.head=t.next
        while (t.next!=None):
            if(t.data==value):
                prev.next=t.next
                break
            else:
                prev=t
                t=t.next
        if (t.data==value):
            # if(t.next==None):
                prev.next=None

    def insertAtBegining(self,value):
        temp=NODE(value)
        temp.next=self.head
        self.head=temp
    
    def insertAtMiddle(self,value,x):
        temp=NODE(value)
        t=self.head
        while (t.next!= None):
            if(t.data == x):
                temp.next=t.next
                t.next=temp
            t=t.next
    def reverse(self):
        prev, start = None, self.head
        while start:
            temp=start.next
            start.next=prev
            prev=start
            start=temp
        while(prev.next!=None):
            print(prev.data, end = " --> ")
            prev=prev.next
        print(prev.data)
    def printLL(self):
        t = self.head
        while(t.next!=None):
            print(t.data, end = " --> ")
            t=t.next
        print(t.data)

obj = singlylinkedlist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBegining(5)
obj.insertAtMiddle(40,20)
# obj.deleteValue(30)
obj.printLL()
obj.reverse()





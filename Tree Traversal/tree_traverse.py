class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value
    
    def preOrder(self):
        print(self.data, end ="  ")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
    
    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self.data, end = " ")
        if self.right:
            self.right.inOrder()
    
    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self.data, end = " ")

# def preOrder(root):
#     if root!=None:
#         print(root, end=" ")
#         preOrder(root.left)
#         preOrder(root.right)
        
# def inOrder(root):
#     if root!=None:
#         inOrder(root.left)
#         print(root, end=" ")
#         inOrder(root.right)

# def postOrder(root):
#     if root!=None:
#         postOrder(root.left)
#         postOrder(root.right)
#         print(root, end=" ")


        
        


root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.right.right = Node(8)
root.left.right = Node(4)
# obj = Node(root)
# obj.preOrder()
# preOrder(root)
# inOrder(root)
print("Pre-order: ")
root.preOrder()
print()

print("in-order: ")
root.inOrder()
print()


print("Post-order: ")
root.postOrder()
print()

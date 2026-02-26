class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value
    
def insert(root,value):
    if not root:
        return Node(value)
    if root.data == value:
        return root
    if root.data > value:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right, value) 
        
    return root

def search(root, value):
    # Base case: Element is not in the tree or the current node is the element
    if not root or root.data == value:
        return root
    
    # Value is smaller than root's data, search in the left subtree
    if value < root.data:
        return search(root.left, value)
    
    # Value is larger than root's data, search in the right subtree
    return search(root.right, value)

def Inorder(root):
    if root!=None:
        Inorder(root.left)
        print(root.data, end = " ")
        Inorder(root.right)

root = insert(None,20)
root = insert(root,15)
root = insert(root,30)
root = insert(root,40)
root = insert(root,12)
root = insert(root,18)
root = insert(root,25)
root = insert(root,50)
target_value = 40
found_node = search(root, target_value)

if found_node:
    print(f"Element {target_value} found in the tree.")
else:
    print(f"Element {target_value} not found.")

target_value_missing = 99
found_node_missing = search(root, target_value_missing)

if found_node_missing:
    print(f"Element {target_value_missing} found in the tree.")
else:
    print(f"Element {target_value_missing} not found.")
# Inorder(root)
# root.Inorder()
# print()
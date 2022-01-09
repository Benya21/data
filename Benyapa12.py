class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree():
    def PreOrder(self,tree):
        if tree:
           print(tree.data,end = ' ')
           self.PreOrder(tree.left)
           self.PreOrder(tree.right)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        x = y.left
        y.left = z
        z.right = x
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        x = y.right
        y.right = z
        z.left = x 
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right)) 
        return y
    
    def insert(self, root, key):        
        if not root:
            return Node(key)
        elif key < root.data:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and key < root.left.data:
            return self.rightRotate(root)      
        if balance > 1 and key > root.left.data:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.data:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        if balance < -1 and key > root.right.data:
            return self.leftRotate(root)
 
        return root

myTree= AVL_Tree()
root= None
while True:
    data = int(input("โปรดป้อนจำนวนเต็มเพื่อสร้าง AVL tree : "))
    if data == 1234:
        break
    else:
        data>0
        root = myTree.insert(root, data)
        continue
    
print('ผลลัพธ์ที่ได้จากการท่องไปใน AVL tree ด้วยขั้นตอนวิธีแบบ Pre-order')
myTree.PreOrder(root)
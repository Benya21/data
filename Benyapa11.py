class Node:
    def __init__(self):
        self.data = None
        self.leftChild = None
        self.rightChild = None

    def PreOrder(self,tree):
        if tree:
            print(tree.data, end = '  ')
            self.PreOrder(tree.leftChild)
            self.PreOrder(tree.rightChild)

    def InOrder(self, tree):
        if tree:
            self.InOrder(tree.leftChild)
            print(tree.data, end = '  ')
            self.InOrder(tree.rightChild)

    def PostOrder(self, tree):
        if tree:
            self.PostOrder(tree.leftChild)
            self.PostOrder(tree.rightChild)
            print(tree.data, end = '  ')

    def insert(self, data):
        if self.data == None:
            self.data = data
        elif data < self.data:
            if self.leftChild == None:
                self.leftChild  = Node()
                self.leftChild.data  = data
            else:
                self.leftChild.insert(data)
        elif data > self.data:
            if self.rightChild == None:
                self.rightChild  = Node()
                self.rightChild.data  = data
            else:
                self.rightChild.insert(data)

    def MinimumValue(self):
        if self.leftChild == None:
            return self.data
        return self.leftChild.MinimumValue()

    def MaximumValue(self):
        if self.rightChild == None:
            return self.data
        return self.rightChild.MaximumValue()
    
BST = Node()
n = int(input("โปรดระบุจำนวนโหนดใน Binary search tree :"))
mylist = []*n
print("โปรดป้อนจำนวนเต็มเพื่อจัดเก็บใน Binary search tree")
for i in range(n):
    data = int(input("Data = "))
    if data in mylist:
        continue
    else:
        BST.insert(data)
        mylist.append(data)
        
print('ผลลัพธ์จากการท่องไปในต้นไม้แบบทวิภาคแบบ In-order คือ' )
BST.InOrder(BST)
print("")
print("จำนวนเต็มมากที่สุดจัดเก็บใน Binary serch tree คือ",BST.MaximumValue())

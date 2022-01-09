class node:
    def __init__(self):

        self.leftChild = None
        self.rightChild = None
        self.data = None

    def insert(self, data):
        if data != -1:
            self.data = data
        else:
            return 
        
        print('โปรดป้อนหมายเลขของโหนด Left child ของ ',self.data, '(ถ้าไม่มีให้ป้อน -1): ', end = '')
        data = int(input())
        if data != -1:
            self.leftChild = node()
            self.leftChild.insert(data)
        
        
        print('โปรดป้อนหมายเลขของโหนด Right child ของ ',self.data, '(ถ้าไม่มีให้ป้อน -1): ', end = '')
        data = int(input())
        if data != -1:
            self.rightChild = node()
            self.rightChild.insert(data)
        

    def PreOrder(self, tree):
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

data = int(input('โปรดป้อนจำนวนเต็มเพื่อจัดเก็บที่ Root node :'))
tree = node()
tree.insert(data)

print("ทางเลือกในการแสดงผลลัพธ์")
print("1. ท่องไปในต้นไม้ทวิภาคแบบ Pre-Order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่มีค่ามากกว่า 50 ทางจอภาพ")
print("2. ท่องไปในต้นไม้ทวิภาคแบบ In-Order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่เป็นเลขคู่ทางจอภาพ")
print("3. ท่องไปในต้นไม้ทวิภาคแบบ Post-Order และแสดงจำนวนเต็มที่จัดเก็บในแต่ละโหนดที่เป็นเลขคี่ทางจอภาพ")
print("โปรดระบุทางเลือก:",end=' ')

choice = int(input())
if choice == 1:
    tree.PreOrder(tree)
elif choice ==2:
    tree.InOrder(tree)
else :
    choice == 3
    tree.PostOrder(tree)
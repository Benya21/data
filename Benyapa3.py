class Node:
    def __init__(self, info = None):
        self.info = info
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def AtTheBegining(self, data):
        if self.head != None:
            NewNode = Node(data)
            NewNode.next = self.head
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode

    def AtTheEnd(self, data):
        if self.head == None:
            NewNode = Node(data)
            NewNode.next = None
            self.head = NewNode
            self.tail = NewNode
        else:
            NewNode = Node(data)
            NewNode.next = None
            self.tail.next = NewNode
            self.tail = NewNode
   
    def listPrint(self):
        i = 1
        Status = self.head
        print('head = ',self.head.info)
        while Status is not None:
            print('i = ',i,'info = ',Status.info)
            Status = Status.next
            i+=1
        print('tail = ',self.tail.info)

listA = SLinkedList()
listB = SLinkedList()
B = SLinkedList()
print("โปรดป้อนตัวแปรตัวเลขจำนวนเต็มเพื่อสร้าง Sigly Linked List A โดยโปรแกรมจะหยุดการวนซ้ำเมื่อตัวเลขำนวนเต็มที่ผู้ใช้ป้อนมีค่าเป็น 12345")

while True:
    data1 = int(input("Data = "))
    if data1 == 12345:
        break
    else:
        listA.AtTheEnd(data1)
print("โปรดป้อนตัวแปรตัวเลขจำนวนเต็มเพื่อสร้าง Sigly Linked List B โดยโปรแกรมจะหยุดการวนซ้ำเมื่อตัวเลขำนวนเต็มที่ผู้ใช้ป้อนมีค่าเป็น 12345")
while True:
    data2 = int(input("Data = "))
    if data2 == 12345:
        break
    else:  
        listB.AtTheEnd(data2)
        B.AtTheEnd(data2)
while listA.head:
    listB.AtTheBegining(listA.head.info)
    listA.head = listA.head.next
print("A")
listB.listPrint()
print("B")
B.listPrint()
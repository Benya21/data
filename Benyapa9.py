def bubble_sort(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist)-1):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1] = mylist[j+1],mylist[j]
    return mylist
        
n = int(input("โปรดระบุจำนวนข้อมูลที่ต้องการเรียงลำดับ : "))
mylist = []*n

print("โปรดป้อนข้อมูลที่ต้องการเรียงลำดับ")
mylist = [(int(input('ข้อมูล : '))) for i in range(n)]
print("ข้อมูลก่อนเรียงลำดับ คือ")
print(mylist)
print("ข้อมูลที่เรียงลำดับจากน้อยไปมาก คือ")
print(bubble_sort(mylist))

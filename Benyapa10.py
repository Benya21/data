def shellsort(mylist):
    gap_size = n //2
    while gap_size > 0:
        for i in range(gap_size,n):
            temp = mylist[i]
            x = i
            while x >= gap_size and mylist[x - gap_size] > temp:
                mylist[x] = mylist[x - gap_size]
                x = x-gap_size
            mylist[x] = temp
        gap_size = gap_size//2
    print(mylist)
        
n = int(input("โปรดระบุจำนวนข้อมูลที่ต้องการเรียงลำดับ : ")) 
print('โปรดป้อนข้อมูลที่ต้องการเรียงลำดับ')
mylist = [(int(input("ข้อมูล : "))) for x in range(n)]
print("ข้อมูลก่อนเรียงลำดับ คือ")
print(mylist)
print("ข้อมูลที่เรียงลำดับจากน้อยไปมาก คือ")
shellsort(mylist)

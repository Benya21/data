n = int(input("โปรดป้อนขนาดตารางแฮช : "))

hashtable = [None]*n
collision = 0

while True:
    key = int(input("โปรดป้อนค่าคีย์(key)ที่เป็นจำนวนเต็มบวกที่มีค่าตั้งแต่ 1 ขึ้นไป : "))
    data = input("โปรดป้อนข้อมูล(data)ที่เป็นข้อความเพื่อจัดเก็บข้อมูลในตารางแฮช : ")
    print("")
    if key <= 1 :
        break
    else:
        a = key%n
        if hashtable[a] != None:
            print("จัดเก็บข้อมูลในตารางแฮชไม่ได้เพราะ Collision")
            collision = collision+1
            print("")
        else:
            hashtable[a] = data
            
print("ข้อมูลที่จัดเก็บในตารางแฮช")
for i in hashtable:
    if i != None:
        print("index = ",hashtable.index(i),"ข้อมูลที่จัดเก็บคือ",i)
print("")        
print("จำนวนครั้งที่เกิด Collision = ",collision)
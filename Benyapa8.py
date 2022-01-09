n = int(input("โปรดป้อนขนาดตารางแฮช : "))
hashtable = [None]*n
i = 0

while True:
    key = int(input("โปรดป้อนค่าคีย์(key)ที่มีค่ามากกว่าหรือเท่ากับ 0 : "))
    data = input("โปรดป้อนข้อมูลชื่อสินค้าเพื่อจัดเก็บในตารางแฮช : ")
    if key < 0:
        break
    else:
        key = key%n
        if hashtable[key] != None:
            i = 0
            while True :
                i = i+1
                H = (key+i)%n
                if hashtable[H] != None:continue
                else:
                    hashtable[H] = data
                    print(f"Address = {H}")
                    print("")
                    break
        else:
            hashtable[key] = data
            print(f"Address = {key}")
            print("")

a = 0
print("ข้อมูลที่จัดเก็บในตารางแฮช")
for x in hashtable:
    if x == None:
        print("Address = ",a, "-")
        a = a+1
    else:
        print("Address = ",a,"ข้อมูลที่จัดเก็บคือ ",x)
        a = a+1
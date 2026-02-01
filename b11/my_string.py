# ------------------------
#khai báo sau kí tự
chuoi_rong =""
fullName ="Ma Ky Ky"
#------------------
#duyet xau
# truy cap phan tu
for chart in fullName:
    print(chart, end="")

for index in range(len(fullName)):
    #truy cap phan tu
    print(f"{index}: {fullName[index]}")
#------------------------------
# + xau ki tu
sentence = "My fullname is" + fullName + "."
print(sentence)
#-------------
#xau con
firstName = "Ma"
lastName = "Hieu"
#----------------------
#tim xau con trong danh sach(in)
print(firstName in fullName)
print(lastName in fullName)
#--------------------
# chinh kieu string
print(fullName.lower())
print(fullName.upper())
print(fullName.capitalize())
#-----------------------------
# tim vi tri xau con (find)
d_index = fullName.find ("d")
print(d_index) # khong co tra ve -1
# NOTE: find(ki tu can tim, start,stop)
k_index = fullName.find("k", 4) # neu trung ki tu thi lay ki tu dau tien (start, stop)
print(k_index)
#--------------------------
#str -> list(split)
nameList = fullName.split(" ")
print(nameList)
#-------------------
# thay doi phan tu (gia tri)
# replace(gia tri can thay, gia tri moi, so luong can thay) -> ham co return
# NOTE: neu khong co <so luong can thay> -> sua het
newName = fullName.replace("Ky", "Hieu")
print(newName)
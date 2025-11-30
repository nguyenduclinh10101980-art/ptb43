#Đế: nhập 2 số
#1.tìm số lớn hơn
# 2. tính tổng hai số
#3.chia lấy phần nguyên
#=================
#xác định kiểu dữ liệu
#truyền 2 số vào từ bàn phím với input
a = input("a: ")
b = input("b: ")
print(a, type(a))
print(b, type(b))

#=========================
#ép kiểu
# str -> float (có thể có dấu .)
# str -> int (không thể có dấu .)
# float -> int (bị bỏ phần thập phân - chỉ lấy phần nguyên)
a = int(a)
b = int(b)
print(type(a),  type(b))
if a > b:
    print("a là lớn hơn")
else:
 print("b là lớn hơn")
tong = a + b
print("Tổng 2 số:", tong)
chia_phan_nguyen = a//b
print("chia a cho b, lấy phần nguyên:", chia_phan_nguyen)
chia_phan_du = a%b
print("chia a cho b, lấy phần dư:", chia_phan_du)
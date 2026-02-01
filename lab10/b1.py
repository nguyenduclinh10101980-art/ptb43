danhsach_diem = []
# them diem
so_bai_kiemtra = int(input("Nhập số bài kiểm tra:"))
while so_bai_kiemtra <= 0:
    so_bai_kiemtra = int(input("Nhập lại số bài kiểm tra > 0:"))

for i in range(so_bai_kiemtra):
    diem = float(input(f"Nhap diem bai {i + 1}:"))   
    # them vao danh sach 
    danhsach_diem.append(diem)

print("Danh sach diem:", danhsach_diem)
#1. Sắp xếp danh sách điểm số theo chiều tăng dần
danhsach_diem.sort(reverse=False)
print("Danh sach sau khi sort:", danhsach_diem)
#2. Xóa số điểm nhỏ nhất (Nếu có hai số điểm nhỏ nhất thì xóa cả hai)
if (so_bai_kiemtra == 1): print("Khong the xoa do danh sach 1 phan tu")
else:
    diem_nn = min(danhsach_diem)
    # lap toi khi xoa het diem nho nhat(neu trung)
    while diem_nn in danhsach_diem:
        danhsach_diem.remove(diem_nn)
print("da xoa diem nho nhat:", diem_nn)
print("danh sau khi xoa:", danhsach_diem)
#3.Xuất danh sách điểm sau khi đã xử lý yêu cầu 1 và 1
#4.đếm số lượng điểm lớn hơn hoặc bằng 8 và xuất ra màn hình
counter = 0
for value in danhsach_diem:
    if value >= 8: counter+=1
print("So luong diem >= 8:", counter)

danhsach_diem_lonhon8 = [value for value in danhsach_diem if value >= 8]
print(len(danhsach_diem_lonhon8)) # do dai danh sach diem >= 8
danh_sach_1 = [1, "a", "abc123", 12.3, False]
for i in range(len(danh_sach_1)):
    print(danh_sach_1[i])
for value in danh_sach_1:
    print(value)
danh_sach_1.append(100)
print(danh_sach_1)
danh_sach_1.insert(len(danh_sach_1) -1, "new")
print(danh_sach_1)
danh_sach_1[4] = "updated item"
print(danh_sach_1)
del_item = danh_sach_1.pop()
print(f"{del_item} da duoc xoa khoi danh sach {danh_sach_1}")
del_item_1 = danh_sach_1.pop(-1)
print(f"{del_item_1} da duoc xoa khoi danh sach {danh_sach_1}")
del_item_2 = danh_sach_1.remove(1)
print(danh_sach_1)
danh_sach_2 = ['a', 'm', 'A', 'x', '-']
danh_sach_2.sort(reverse=True)
print(danh_sach_2)
print(danh_sach_2.sort(reverse=False))
print(danh_sach_2)
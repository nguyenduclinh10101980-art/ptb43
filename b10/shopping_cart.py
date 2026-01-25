cart = []
funcs = [
    "0. In gio hang",
    "1. Them vao gio",
    "2. Chinh sua mon hang",
    "3. xoa mon hang (theo index)",
    "4. sap xep theo ten",
    "5. thoat chuong trinh"
]
# bat dau chuong trinh
print("------------SHOPPING CART---------")
while True:
    #in danh sach tinh nang
    for value in funcs:
        print(value)
    # chon 1 chuc nang
    choice = int(input("chon 1 chuc nang: "))
    # neu khong dung -> bao loi
    while (choice > 5 or choice < 0):
        choice = int(input("chon 1 chuc nang ( 0 -> 5) :"))

    # func 5:
    if choice == 5:
        print("Bye!")
        break

    # func 0 :
    if choice == 0:
        if len(cart) == 0:
            print("Gio hang rong")
            continue
        for i in range(len(cart)):
            print(f"{i}: {cart[i]}")
    #funcs 1:
    elif choice ==1:
        pass
    # funcs 2:
    elif choice == 2:
        pass
    # funcs 3:
    elif choice == 3:
        pass
    # funcs 4:
    elif choice == 4:
        pass
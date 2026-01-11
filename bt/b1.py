a = int(input("Nhap canh a: "))
b = int(input("Nhap canh b: "))
c = int(input("Nhap canh c: "))
if a + b > c và b + c > a và a + c > b:
    print(f"{a}, {b}, {c} là cạnh của tam giác: ")
else:
    print(f"{a}, {b}, {c} không phải là cạnh của tam giác: ")

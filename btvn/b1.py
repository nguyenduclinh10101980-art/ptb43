n = -1
while n <= 0:
    n = int(input("Nhap so nguyen n > 0: "))
# muon chay chan -> start: so chan + buoc nhay: 2
tong = 0
for i in range(2, n + 1, 2):
    tong += i

print(f"Tong cac so chan tu 1 den {n} la: {tong}")

def tinhluong(giolam, luonggio):
    tongluong = giolam * luonggio
    return tongluong
def inthongtin(ten, giolam, luonggio, tongluong):
    print(f"Ten: {ten}")
    print(f"Gio lam: {giolam}")
    print(f"Luong gio: {luonggio}")
    print(f"Tong luong: {tongluong}")

tongluong = tinhluong(12, 150)
inthongtin("Nguyen Van A", 12, 150, tongluong)
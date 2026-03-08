# name :(@nguyenduclinh101)
# ---------------------------------
a = int(input())
b = int(input())
c = int(input())

# kiểm tra không phải tam giác
if a + b <= c or a + c <= b or b + c <= a:
    print("Khong phai tam giac")

# tam giác vuông
elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
    print("Tam giac vuong")

# tam giác đều
elif a == b == c:
    print("Tam giac deu")

# tam giác cân
elif a == b or b == c or a == c:
    print("Tam giac can")

# tam giác thường
else:
    print("Tam giac thuong")

# ---------------------------------
# tìm giá trị lớn nhất, bé nhất
nums = list(map(int, input().split()))

print(max(nums))
print(min(nums))

# ---------------------------------
# Họ và tên
def tach_ho_ten():

    ho_ten = input().strip()

    tu = ho_ten.split()
    

    if len(tu) < 2:
        return


    ho = tu[0]
    ten = tu[-1]
    

    if len(tu) > 2:
        ten_dem = " ".join(tu[1:-1])
    else:
        ten_dem = ""


    print(f"Ho: {ho}")
    if ten_dem:
        print(f"Ten dem: {ten_dem}")
    print(f"Ten: {ten}")

if __name__ == "__main__":
    tach_ho_ten()

# ---------------------------------
# ngày tháng năm 
def isLeap(y):
    if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
        return True
    return False


date = input()
d, m, y = map(int, date.split('/'))

valid = True

if m < 1 or m > 12:
    valid = False

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

if isLeap(y):
    days[2] = 29

if d < 1 or d > days[m]:
    valid = False

if valid:
    print("YES")
else:
    print("NO")
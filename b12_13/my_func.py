# ham khong co tra ve (co print)
def hello():
    name = input("Nhap ten cua ban:")
    print(f"Hi {name}!")


    # -----------------
    #ham co tra ve (return)
    def sum_two_num():
        a = int(input("Nhap so thu nhat:"))
        b = int(input("Nhap so thu hai:"))
        return a + b


#-----------------------
#ham co dau vao(tham so - parameters)
def duplicate_str(s:str, n:int):
    return s*n

#--------------------------
#bien global
global_count = 0
def counter_to_n(n:int):
    global global_count 
    print(global_count)
    for i in range(n+1):
        global_count += 1
    print(global_count)
#----------------
# goi lai ham de chay
if __name__ == "__main__"
    # phai di kem()moi chay ham
    # hello()
    #hello()
    #print(sum_two_num())
    # print(duplicate_str("a", 3))
    counter_to_n(5)

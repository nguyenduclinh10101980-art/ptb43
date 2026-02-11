def tinh_diem_trung_binh(diem_so):
    tong_diem = sum(diem_so)
    tong_he_so = len(diem_so) + 1
    diem_trung_binh = tong_diem / tong_he_so
    print(f"trung bình điểm là: {diem_trung_binh}")
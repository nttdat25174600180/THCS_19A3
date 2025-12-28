def sap_xep_tang_dan(danh_sach):
    return sorted(danh_sach)

def lay_gia_tri(tu_dien, khoa):
    return tu_dien.get(khoa, "Không tìm thấy")

ds = [5, 1, 8, 3]
td = {"a": 10, "b": 20}

print("Danh sách tăng dần:", sap_xep_tang_dan(ds))
print("Giá trị khóa a:", lay_gia_tri(td, "a"))

gia = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng: "))

tong_chi_phi = gia * so_luong
vat = tong_chi_phi * 0.10
tong_tien = round(tong_chi_phi + vat, 2)

print("Tổng tiền phải trả:", tong_tien)

luong_cb = float(input("Lương cơ bản: "))
ngay = int(input("Số ngày công: "))

luong_ngay = luong_cb / 22
luong_thang = luong_ngay * ngay

if ngay > 22:
    luong_thang *= 1.10
elif ngay < 22:
    luong_thang *= 0.95

print("Lương thực nhận:", luong_thang)

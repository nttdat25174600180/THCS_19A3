keo = int(input("Nhập tổng số kẹo: "))
hs = int(input("Nhập số học sinh: "))

moi_hs = keo // hs
thua = keo % hs

print("Mỗi học sinh nhận:", moi_hs)
print("Còn thừa:", thua)

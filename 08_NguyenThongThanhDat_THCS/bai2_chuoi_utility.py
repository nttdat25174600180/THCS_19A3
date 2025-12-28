def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]

def dem_so_tu(chuoi):
    return len(chuoi.split())

s = "Python rat de hoc"
print("Chuỗi đảo ngược:", dao_nguoc_chuoi(s))
print("Số từ:", dem_so_tu(s))

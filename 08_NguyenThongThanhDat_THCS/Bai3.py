s = input("Nhập chuỗi: ")
ket_qua = ""
tam = ""
# Loại bỏ khoảng trắng đầu/cuối và chuẩn hóa giữa
for char in s:
    if char != " ":
        tam += char
    else:
        if tam != "":
            if ket_qua != "":
                ket_qua += " " + tam
            else:
                ket_qua = tam
            tam = ""
if tam != "":
    if ket_qua != "":
        ket_qua += " " + tam
    else:
        ket_qua = tam
print(f"Chuỗi sau khi xử lý: '{ket_qua}'")
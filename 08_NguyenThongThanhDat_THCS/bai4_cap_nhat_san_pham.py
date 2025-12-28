# Bài 4: Cập nhật giá sản phẩm
data = [
    "ID,Ten,Gia",
    "1,Laptop,1200",
    "2,Chuot,25",
    "3,Ban phim,75"
]

with open("san_pham.txt", "w") as f:
    for line in data:
        f.write(line + "\n")

id_update = "2"
gia_moi = "30"

lines = []
with open("san_pham.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if parts[0] == id_update:
            parts[2] = gia_moi
            line = ",".join(parts) + "\n"
        lines.append(line)

with open("san_pham.txt", "w") as f:
    f.writelines(lines)

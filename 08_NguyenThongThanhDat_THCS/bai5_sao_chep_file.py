# Bài 5: Sao chép file nhị phân
with open("nguon.bin", "wb") as f:
    f.write(b"Hello")

with open("nguon.bin", "rb") as src, open("dich.bin", "wb") as dst:
    while True:
        block = src.read(1024)
        if not block:
            break
        dst.write(block)

# Bài 1: Đọc file và đếm số từ
with open("vanban.txt", "w", encoding="utf-8") as f:
    f.write("Python là một ngôn ngữ lập trình mạnh mẽ và dễ học")

with open("vanban.txt", "r", encoding="utf-8") as f:
    noi_dung = f.read()
    so_tu = len(noi_dung.split())
    print("Số từ trong file:", so_tu)

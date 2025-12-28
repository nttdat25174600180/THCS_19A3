# Bài 7: Tạo cấu trúc thư mục
import os

os.makedirs("test_folder", exist_ok=True)
open("test_folder/file1.txt", "w").close()
print(os.listdir("test_folder"))

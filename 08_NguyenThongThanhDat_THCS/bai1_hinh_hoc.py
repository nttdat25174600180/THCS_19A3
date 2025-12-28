import math

def chu_vi_hinh_vuong(canh):
    return 4 * canh

def chu_vi_hinh_tron(ban_kinh):
    return 2 * math.pi * ban_kinh

print("Chu vi hình vuông cạnh 5:", chu_vi_hinh_vuong(5))
print("Chu vi hình tròn bán kính 3:", chu_vi_hinh_tron(3))

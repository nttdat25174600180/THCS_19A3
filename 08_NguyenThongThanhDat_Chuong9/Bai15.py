def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 2) + 1):
        if n % i == 0:
            return False
    return True

# Nhập n và kiểm tra
n = int(input("Nhập n: "))
print("Là số nguyên tố?" , la_so_nguyen_to(n))

# In số nguyên tố từ 100 đến 500
for x in range(100, 501):
    if la_so_nguyen_to(x):
        print(x, end=" ")

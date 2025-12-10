
def la_so_nguen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
n = int(input("nhap n:"))
print("là số nguyên tố : ", la_so_nguen_to(n))

print("các số nguyên tố trong khoảng từ 100 đén 500:")
for x in range(100, 501):
    if la_so_nguen_to(x):
        print(x, end=" ")
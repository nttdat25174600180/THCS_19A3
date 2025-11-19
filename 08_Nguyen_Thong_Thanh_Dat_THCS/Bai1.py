import math

n = int(input("Nhập số n: "))
if n >= 0 and int(math.sqrt(n))**2 == n:
    print(n, "là số chính phương")
else:
    print(n, "không phải số chính phương")

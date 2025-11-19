#S1 = 1 + 2 + 3 + ... + n
n = int(input("Nhập n: "))

S1 = 0
for i in range(1, n+1):
    S1 += i

print("S1 =", S1)

#S2 = 1 * 2 * 3 * ... * (n − 1)
n = int(input("Nhập n: "))

S2 = 1
for i in range(1, n):
    S2 *= i

print("S2 =", S2)

#S3 = 1 − 1/2 + 1/3 − 1/4 + ... + ((−1)ⁿ)/n
n = int(input("Nhập n: "))

S3 = 0
for i in range(1, n+1):
    S3 += ((-1)**(i+1)) * (1/i)

print("S3 =", S3)

#S4 = Σ (k / (k + 2)) từ k = 0 → n
n = int(input("Nhập n: "))

S4 = 0
for k in range(0, n+1):
    S4 += k / (k + 2)

print("S4 =", S4)

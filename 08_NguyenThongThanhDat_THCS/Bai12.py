A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

r1 = 0
for _ in A: 
    r1 += 1
c1 = 0
for _ in A[0]: 
    c1 += 1

r2 = 0
for _ in B: 
    r2 += 1
c2 = 0
for _ in B[0]: 
    c2 += 1

if c1 != r2:
    print("Không thể nhân hai ma trận do kích thước không phù hợp!")
else:
    C = []
    for i in range(r1):
        row = []
        for j in range(c2):
            row += [0]
        C += [row]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    print("Ma trận kết quả A * B là:")
    for row in C:
        print(row)
        
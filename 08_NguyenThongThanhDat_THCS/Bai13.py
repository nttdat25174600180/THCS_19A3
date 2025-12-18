
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

rows = 0
for _ in matrix:
    rows += 1

if rows == 0:
    print("Ma trận rỗng!")
else:
    cols = 0
    for _ in matrix[0]:
        cols += 1
    if rows != cols:
        print("Đây không phải ma trận vuông, nên không thể là ma trận đơn vị.")
    else:
        is_unit = True
        for i in range(rows):
            for j in range(cols):
                if i == j:
                
                    if matrix[i][j] != 1:
                        is_unit = False
                        break
                else:
                    if matrix[i][j] != 0:
                        is_unit = False
                        break
            if not is_unit:
                break
        
        if is_unit:
            print("Đây là ma trận đơn vị.")
        else:
            print("Đây là ma trận vuông nhưng KHÔNG PHẢI ma trận đơn vị.")
            
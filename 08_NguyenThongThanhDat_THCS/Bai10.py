matrix = [[1, 2, 3], [10, 20, 30], [5, 5, 5]]
max_sum = -float('inf')
max_row_index = 0

row_idx = 0
for row in matrix:
    current_row_sum = 0
    for element in row:
        current_row_sum += element
    
    if current_row_sum > max_sum:
        max_sum = current_row_sum
        max_row_index = row_idx
    row_idx += 1

print(f"Hàng có tổng lớn nhất là hàng {max_row_index} với tổng = {max_sum}")

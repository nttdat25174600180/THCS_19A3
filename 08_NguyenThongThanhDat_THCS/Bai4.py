lst = [10, 20, 4, 45, 99, 99, 45]
max1 = max2 = -float('inf')
for x in lst:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x
print("Giá trị lớn thứ hai:", max2)
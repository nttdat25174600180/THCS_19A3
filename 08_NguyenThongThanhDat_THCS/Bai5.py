lst = [1, 2, 2, 3, 4, 4, 5, 1]
unique_lst = []
for x in lst:
    found = False
    for y in unique_lst:
        if x == y:
            found = True
            break
    if not found:
        unique_lst += [x]
print("Danh sách duy nhất:", unique_lst)
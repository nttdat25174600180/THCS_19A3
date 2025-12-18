d = {'A': 70, 'B': 40, 'C': 90, 'D': 30}
filtered_dict = {}

for key in d:
    if d[key] > 50:
        filtered_dict[key] = d[key]
print("Kết quả lọc:", filtered_dict)
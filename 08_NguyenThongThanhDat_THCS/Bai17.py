d = {'a': 10, 'b': 50, 'c': 20}
max_val = -float('inf')
max_key = None

for key in d:
    if d[key] > max_val:
        max_val = d[key]
        max_key = key
print("Key có giá trị lớn nhất:", max_key)
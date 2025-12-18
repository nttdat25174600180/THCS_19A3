data = {'An': 8, 'Bình': 7, 'Chi': 8, 'Đông': 9}
grouped = {}

for name in data:
    diem = data[name]
    if diem not in grouped:
        grouped[diem] = [name]
    else:
        grouped[diem] += [name] # Không dùng append() để an toàn
print(grouped)
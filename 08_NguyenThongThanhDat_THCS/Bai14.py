A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Hiệu A - B
hieu_A_B = set()
for x in A:
    if x not in B:
        hieu_A_B.add(x)

# Hiệu B - A
hieu_B_A = set()
for x in B:
    if x not in A:
        hieu_B_A.add(x)

# Giao (A & B)
giao = set()
for x in A:
    if x in B:
        giao.add(x)

# Hợp (A | B)
hop = set()
for x in A: hop.add(x)
for x in B: hop.add(x)

print(f"A-B: {hieu_A_B}, B-A: {hieu_B_A}, Giao: {giao}, Hợp: {hop}")
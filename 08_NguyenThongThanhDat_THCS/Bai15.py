t = (1, 2, 3, 4, 5, 6)
chan = ()
le = ()
tong_chan = 0
tong_le = 0

for x in t:
    if x % 2 == 0:
        chan += (x,)
        tong_chan += x
    else:
        le += (x,)
        tong_le += x

print(f"Tuple chẵn: {chan}, Tổng: {tong_chan}")
print(f"Tuple lẻ: {le}, Tổng: {tong_le}")

s = input()
chu = so = dac_biet = 0
for ch in s:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        chu += 1
    elif '0' <= ch <= '9':
        so += 1
    else:
        dac_biet += 1
print(chu, so, dac_biet)

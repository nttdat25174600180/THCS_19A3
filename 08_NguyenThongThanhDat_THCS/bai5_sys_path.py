def kiem_tra_so_nguyen_to(so):
    if so < 2:
        return False
    for i in range(2, int(so ** 0.5) + 1):
        if so % i == 0:
            return False
    return True

print("7 có phải số nguyên tố không?", kiem_tra_so_nguyen_to(7))

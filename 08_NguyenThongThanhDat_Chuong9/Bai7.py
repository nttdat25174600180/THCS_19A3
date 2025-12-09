def la_so_hoan_hao(n):
    tong = sum(i for i in range(1, n) if n % i == 0)
    return tong == n

def tinh_tong_so_hoan_hao(a, b):
    tong = 0
    for n in range(a, b + 1):
        if la_so_hoan_hao(n):
            tong += n
    return tong

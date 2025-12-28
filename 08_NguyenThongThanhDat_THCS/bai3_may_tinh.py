import math

def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def luy_thua(co_so, so_mu):
    return co_so ** so_mu

def can_bac_hai(so):
    return math.sqrt(so)

print("Cộng:", cong(3, 4))
print("Trừ:", tru(10, 5))
print("Lũy thừa:", luy_thua(2, 3))
print("Căn bậc hai:", can_bac_hai(16))

# 2. Máximo Común Divisor (MCD)
def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
print(f"El MCD de {n1} y {n2} es {mcd(n1, n2)}")

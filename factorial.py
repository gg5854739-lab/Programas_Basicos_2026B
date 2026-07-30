# Factorial de un número - for
n = int(input("Número: "))
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"Factorial de {n} es {fact}")

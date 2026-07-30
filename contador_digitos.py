# Contador de dígitos - while
num = int(input("Número: "))
contador = 0
if num == 0:
    contador = 1
else:
    while num != 0:
        num //= 10
        contador += 1
print(f"Tiene {contador} dígitos")

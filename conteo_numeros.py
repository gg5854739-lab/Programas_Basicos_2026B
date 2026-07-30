# Conteo mayores, menores e iguales a cero
mayores = menores = iguales = 0
for i in range(5):
    num = float(input(f"Número {i+1}: "))
    if num > 0:
        mayores += 1
    elif num < 0:
        menores += 1
    else:
        iguales += 1
print(f"Mayores: {mayores}, Menores: {menores}, Iguales a 0: {iguales}")

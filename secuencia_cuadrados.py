# Generar secuencia de cuadrados - do-while
n = int(input("Cuántos cuadrados: "))
i = 1
while True:
    print(f"{i}^2 = {i**2}")
    i += 1
    if i > n:
        break

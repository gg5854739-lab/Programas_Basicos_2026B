# Media de números positivos - termina con negativo
suma = 0
cont = 0
while True:
    num = float(input("Número (negativo para terminar): "))
    if num < 0:
        break
    suma += num
    cont += 1

if cont > 0:
    print(f"Media: {suma/cont:.2f}")
else:
    print("No se ingresaron positivos")

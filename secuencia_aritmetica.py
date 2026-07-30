# Generar secuencia aritmética - do-while
inicio = int(input("Inicio: "))
diferencia = int(input("Diferencia: "))
cantidad = int(input("Cantidad: "))

cont = 0
actual = inicio
while True:
    print(actual, end=" ")
    actual += diferencia
    cont += 1
    if cont >= cantidad:
        break

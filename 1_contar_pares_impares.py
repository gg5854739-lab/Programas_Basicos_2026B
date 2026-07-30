# 1. Contar pares e impares
def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for num in lista:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

numeros = [1, 2, 3, 4, 5, 6, 7, 8]
p, imp = contar_pares_impares(numeros)
print(f"Lista: {numeros}")
print(f"Pares: {p}, Impares: {imp}")

# Prueba con entrada del usuario
entrada = input("Ingresa números separados por espacio: ")
lista_user = list(map(int, entrada.split()))
p2, imp2 = contar_pares_impares(lista_user)
print(f"Pares: {p2}, Impares: {imp2}")

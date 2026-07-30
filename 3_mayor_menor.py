# 3. Encontrar mayor y menor
def mayor_menor(lista):
    return max(lista), min(lista)

numeros = [34, 12, 89, 5, 67]
mayor, menor = mayor_menor(numeros)
print(f"Lista: {numeros}")
print(f"Mayor: {mayor}, Menor: {menor}")

entrada = input("Ingresa números separados por espacio: ")
lista_user = list(map(int, entrada.split()))
may, men = mayor_menor(lista_user)
print(f"Mayor: {may}, Menor: {men}")

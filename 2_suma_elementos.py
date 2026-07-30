# 2. Suma de elementos
def suma_lista(lista):
    return sum(lista)

numeros = [5, 10, 15, 20]
print(f"Lista: {numeros}")
print(f"Suma: {suma_lista(numeros)}")

entrada = input("Ingresa números separados por espacio: ")
lista_user = list(map(int, entrada.split()))
print(f"Suma de tu lista: {suma_lista(lista_user)}")

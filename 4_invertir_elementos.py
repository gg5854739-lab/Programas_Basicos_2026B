# 4. Invertir elementos
def invertir_lista(lista):
    return lista[::-1]

numeros = [1, 2, 3, 4, 5]
print(f"Original: {numeros}")
print(f"Invertida: {invertir_lista(numeros)}")

entrada = input("Ingresa palabras o números separados por espacio: ")
lista_user = entrada.split()
print(f"Tu lista invertida: {invertir_lista(lista_user)}")

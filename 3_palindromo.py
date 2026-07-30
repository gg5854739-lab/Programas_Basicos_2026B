# 3. Palíndromo
def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]

palabra = input("Palabra o frase: ")
if es_palindromo(palabra):
    print("Es palíndromo")
else:
    print("No es palíndromo")

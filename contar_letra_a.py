# Contar letras 'a' en una palabra
palabra = input("Palabra: ").lower()
contador = 0
for letra in palabra:
    if letra == 'a':
        contador += 1
print(f"La letra 'a' aparece {contador} veces")

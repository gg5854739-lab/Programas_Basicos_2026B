# Vocales o consonantes - termina con espacio
texto = input("Escribe texto (termina con espacio): ")
vocales = consonantes = 0
for letra in texto:
    if letra == " ":
        break
    if letra.lower() in "aeiou":
        vocales += 1
    elif letra.isalpha():
        consonantes += 1
print(f"Vocales: {vocales}, Consonantes: {consonantes}")

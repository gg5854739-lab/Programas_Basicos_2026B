# Adivinar número 1-100
import random
secreto = random.randint(1, 100)
intento = 0
while intento != secreto:
    intento = int(input("Adivina (1-100): "))
    if intento < secreto:
        print("Más alto")
    elif intento > secreto:
        print("Más bajo")
print("¡Acertaste!")

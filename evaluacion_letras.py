# Evaluación con letras A, B, C, D, F
cal = float(input("Calificación 0-100: "))

if cal >= 90:
    letra = "A"
elif cal >= 80:
    letra = "B"
elif cal >= 70:
    letra = "C"
elif cal >= 60:
    letra = "D"
else:
    letra = "F"

print(f"Calificación: {letra}")

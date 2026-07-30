# Calculadora calificaciones 40% parciales, 30% proyecto, 30% examen
parciales = float(input("Calificación parciales (0-100): "))
proyecto = float(input("Calificación proyecto (0-100): "))
examen = float(input("Calificación examen (0-100): "))

final = parciales*0.4 + proyecto*0.3 + examen*0.3

if final >= 90:
    print(f"Final: {final:.2f} - Excelente")
elif final >= 80:
    print(f"Final: {final:.2f} - Bueno")
elif final >= 70:
    print(f"Final: {final:.2f} - Suficiente")
else:
    print(f"Final: {final:.2f} - Reprobado")

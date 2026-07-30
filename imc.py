# Programa 3: Índice de Masa Corporal (IMC)
# Fórmula: IMC = peso / altura^2

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"Tu IMC es: {imc:.2f}")

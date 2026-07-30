# Convertidor Celsius a Fahrenheit o Kelvin
celsius = float(input("Grados Celsius: "))
print("1. Fahrenheit\n2. Kelvin")
opcion = int(input("Elige opción: "))

match opcion:
    case 1:
        f = celsius * 9/5 + 32
        print(f"{celsius}°C = {f:.2f}°F")
    case 2:
        k = celsius + 273.15
        print(f"{celsius}°C = {k:.2f}K")
    case _:
        print("Opción no válida")

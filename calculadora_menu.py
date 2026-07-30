# Calculadora básica con menú - emulación do-while
while True:
    print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")
    op = input("Opción: ")
    if op == "5":
        print("Saliendo...")
        break
    a = float(input("Num 1: "))
    b = float(input("Num 2: "))
    if op == "1":
        print(f"Resultado: {a+b}")
    elif op == "2":
        print(f"Resultado: {a-b}")
    elif op == "3":
        print(f"Resultado: {a*b}")
    elif op == "4":
        if b != 0:
            print(f"Resultado: {a/b}")
        else:
            print("No se puede dividir entre 0")

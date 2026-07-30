# Verificar edad para votar
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes votar")
else:
    print(f"No puedes votar, te faltan {18-edad} años")

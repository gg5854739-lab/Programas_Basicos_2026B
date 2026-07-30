# Calcular precio con descuento por rangos
precio = float(input("Precio del producto: $"))

if precio <= 100:
    desc = 0
elif precio <= 200:
    desc = 10
elif precio <= 500:
    desc = 20
else:
    desc = 30

total = precio - (precio * desc / 100)
print(f"Descuento: {desc}%")
print(f"Total a pagar: ${total:.2f}")

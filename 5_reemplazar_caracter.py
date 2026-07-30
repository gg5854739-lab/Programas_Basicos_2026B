# 5. Reemplazar carácter
def reemplazar_caracter(texto, viejo, nuevo):
    return texto.replace(viejo, nuevo)

texto = input("Texto: ")
viejo = input("Carácter a reemplazar: ")
nuevo = input("Carácter nuevo: ")
print(f"Resultado: {reemplazar_caracter(texto, viejo, nuevo)}")

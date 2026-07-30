# 6. Raíz cuadrada
import math

def raiz_cuadrada(n):
    if n < 0:
        return "No se puede calcular raíz de negativo"
    return math.sqrt(n)

num = float(input("Número: "))
print(f"Raíz cuadrada de {num} es {raiz_cuadrada(num)}")

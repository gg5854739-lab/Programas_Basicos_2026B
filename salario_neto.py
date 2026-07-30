# Programa 4: Salario neto
# Fórmula: salario_neto = salario_bruto - (salario_bruto * impuestos / 100) - deducciones

salario_bruto = float(input("Ingresa el salario bruto: $"))
porcentaje_impuestos = float(input("Ingresa el porcentaje de impuestos (%): "))
deducciones = float(input("Ingresa las deducciones adicionales: $"))

impuestos = salario_bruto * (porcentaje_impuestos / 100)
salario_neto = salario_bruto - impuestos - deducciones

print(f"Impuestos calculados: ${impuestos:.2f}")
print(f"El salario neto es: ${salario_neto:.2f}")

# Contador de números impares - do-while
n = int(input("Hasta qué número: "))
i = 1
while True:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
    if i > n:
        break

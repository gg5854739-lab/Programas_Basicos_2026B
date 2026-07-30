# Brindar información - match-case
print("1. Bad Bunny\n2. Interstellar\n3. Breaking Bad\n4. Taylor Swift\n5. Avatar\n6. Stranger Things")
op = int(input("Elige (1-6): "))

match op:
    case 1:
        print("Bad Bunny: Artista puertorriqueño, reggaetón y trap latino.")
    case 2:
        print("Interstellar: Película de ciencia ficción de Nolan, 2014.")
    case 3:
        print("Breaking Bad: Serie sobre un profesor de química que se vuelve fabricante.")
    case 4:
        print("Taylor Swift: Cantautora estadounidense, pop/country.")
    case 5:
        print("Avatar: Película de James Cameron, mundo de Pandora, 2009.")
    case 6:
        print("Stranger Things: Serie de Netflix, misterio en los 80s.")
    case _:
        print("Opción no válida")

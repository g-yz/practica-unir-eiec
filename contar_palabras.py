texto = input("Escribe una oración: ")

conteo = {}

for caracter in texto:
    if caracter in conteo:
        conteo[caracter] += 1
    else:
        conteo[caracter] = 1

print("\nFrecuencia de caracteres:")
for caracter, cantidad in conteo.items():
    print(f"'{caracter}': {cantidad}")

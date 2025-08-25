texto = "hola mundo"

conteo = {}

for caracter in texto:
    if caracter in conteo:
        conteo[caracter] += 1
    else:
        conteo[caracter] = 1

for caracter, cantidad in conteo.items():
    print(f"'{caracter}': {cantidad}")

#Ejercicio 10: Invertir un diccionario
original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for pais, capital in original.items():
    invertido[capital] = pais 

print("Diccionario original:")
for pais, capital in original.items():
    print(f"{pais}: {capital}")

print("\nDiccionario invertido:")
for capital, pais in invertido.items():
    print(f"{capital}: {pais}")
    
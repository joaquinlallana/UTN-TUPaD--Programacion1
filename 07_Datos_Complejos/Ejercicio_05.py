#Ejercicio 5: Palabras únicas y conteo
def contador_palabras(palabra, lista_palabras):
    contador = 0
    for p in lista_palabras:
        if p == palabra:
            contador += 1
    return contador

frase = input("Ingrese una frase: ").strip()
while frase == "":
    print("Error: la frase no puede estar vacía.")
    frase = input("Ingrese una frase: ").strip()

recuento_palabras = {}
lista_palabras = frase.lower().split()

palabras_unicas = set(lista_palabras)

print(f"Las palabras unicas de la frase son: {palabras_unicas}")

for palabra in palabras_unicas:
    recuento_palabras[palabra] = contador_palabras(palabra, lista_palabras)

print(f"Recuento: {recuento_palabras}")

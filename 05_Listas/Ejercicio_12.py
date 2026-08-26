numeros_enteros= []
contador = 1

print("Ingrese 8 números enteros: ")

while contador <= 8 : 
    numero = input("> ")
    while not (numero.isdigit() or (numero.startswith("-") and numero[1:].isdigit())):
        numero = input("Ingrese solo numeros enteros : ")
    numeros_enteros.append(int(numero))
    contador += 1

print("La lista original es : ")

for i in numeros_enteros:
    print(f"> {i}")

print("La lista ordenada de menor a mayor es :")

ordenados = sorted(numeros_enteros)

for i in ordenados:
    print(f"> {i}")

print("La lista ordenada de mayor a menor es :")

ordenados_inversa = sorted(numeros_enteros,reverse=True)

for i in ordenados_inversa:
    print(f"> {i}")
import random

lista_numeros =[]
numeros_pares = []
numeros_impares = []

for i in range(15):
    numero = random.randint(1,100)
    lista_numeros.append(numero)

for numero in lista_numeros:
    resto = numero % 2 
    if resto == 0 :
        numeros_pares.append(numero)
    else :
        numeros_impares.append(numero)

cantidad_pares = len(numeros_pares)
cantidad_impares = len(numeros_impares)

print(f"Cantidad de numeros pares es de {cantidad_pares} y la de numeros impares es de {cantidad_impares}")
print("\n")
print("Los numeros pares son: ")
print(numeros_pares)
print("\n")
print("Los numeros impares son: ")
print(numeros_impares)
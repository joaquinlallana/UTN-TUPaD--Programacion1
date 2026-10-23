#Ejercicio 3: Agregar try-except
a = 10
b = input("Introduce un número: ")
#Corrección 1: la división se pone dentro de un try para que el TypeError no frene el programa.
try:
    result = a / b
    print(f"Resultado: {result}")
#El except atrapa cualquier error y muestra un mensaje en lugar de cortar la ejecución.
except Exception as error:
    print(f"No se pudo realizar la división: {error}")

numbers = [1, 2, 3]
#Corrección 2: el acceso a la lista se pone en su propio try para que el IndexError tampoco frene el programa.
try:
    print(numbers[5])
except Exception as error:
    print(f"No se pudo acceder al elemento de la lista: {error}")

print("El programa terminó sin interrumpirse.")

#Ejercicio 4: Excepciones múltiples
a = 10
b = input("Introduce un número: ")
#Corrección 1: en lugar de un except general, se usa un except para cada tipo de error posible en la división.
try:
    result = a / b
    print(f"Resultado: {result}")
#Atrapa el error detectado: 'b' es un string y no se puede dividir.
except TypeError:
    print("Error de tipo: no se puede dividir un número por un texto.")
#Atrapa el caso en que el divisor sea 0.
except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")

numbers = [1, 2, 3]
#Corrección 2: se usa un except para cada tipo de error posible al acceder a la lista.
try:
    print(numbers[5])
#Atrapa el error detectado: el índice 5 no existe en la lista.
except IndexError:
    print(f"Error de índice: la lista solo tiene {len(numbers)} elementos.")
#Atrapa el caso en que el índice no sea un número entero.
except TypeError:
    print("Error de tipo: el índice de una lista debe ser un número entero.")

print("El programa terminó sin interrumpirse.")

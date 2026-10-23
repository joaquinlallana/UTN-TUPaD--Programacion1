#Ejercicio 5: Agregar else y finally
a = 10
b = input("Introduce un número: ")
#Corrección 1: el try queda solo con la línea riesgosa (la división).
try:
    result = a / b
except TypeError:
    print("Error de tipo: no se puede dividir un número por un texto.")
except ZeroDivisionError:
    print("Error: no se puede dividir por cero.")
#Corrección 2: el print del resultado pasa al else, que solo se ejecuta si no hubo error.
else:
    print(f"Resultado: {result}")
#Corrección 3: el finally se ejecuta siempre, haya habido error o no.
finally:
    print("Fin del intento de división.")

numbers = [1, 2, 3]
#Corrección 4: el acceso a la lista se guarda en una variable para dejar en el try solo lo riesgoso.
try:
    elemento = numbers[5]
except IndexError:
    print(f"Error de índice: la lista solo tiene {len(numbers)} elementos.")
except TypeError:
    print("Error de tipo: el índice de una lista debe ser un número entero.")
#Si el índice existe, el else muestra el elemento encontrado.
else:
    print(f"Elemento encontrado: {elemento}")
#El finally avisa siempre que terminó el acceso a la lista.
finally:
    print("Fin del acceso a la lista.")

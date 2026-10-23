#Ejercicio 6: Validar un número ingresado
valor = input("Ingrese un número: ")
#Se intenta convertir el texto ingresado a número; es la única línea que puede fallar.
try:
    numero = float(valor)
#Si lo ingresado no es numérico, float() lanza un ValueError.
except ValueError:
    print("Debe ingresar un número válido")
#Cualquier otro error se atrapa acá y se muestra junto al mensaje.
except Exception as error:
    print(f"Se produjo un error inesperado: {error}")
#Si la conversión salió bien, se muestra el número.
else:
    print(f"El número ingresado es: {numero}")

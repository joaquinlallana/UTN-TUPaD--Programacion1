#Ejercicio 7: Permitir reintentar el ingreso
#Corrección: se agrega un while True para que el usuario pueda volver a ingresar el número después de un error.
while True:
    valor = input("Ingrese un número: ")
    try:
        numero = float(valor)
    #Si hay un error se muestra el mensaje y el ciclo vuelve a pedir el número.
    except ValueError:
        print("Debe ingresar un número válido. Intente nuevamente.")
    except Exception as error:
        print(f"Se produjo un error inesperado: {error}. Intente nuevamente.")
    #Si el número es válido se muestra y el break corta el ciclo.
    else:
        print(f"El número ingresado es: {numero}")
        break

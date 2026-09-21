#Definición de la función
def tabla_multiplicar(numero):
    return print(f"Tabla de multiplicación del {numero}: \n {numero} x 1 = {numero * 1}\n {numero} x 2 = {numero * 2}\n {numero} x 3 = {numero * 3}\n {numero} x 4 = {numero * 4}\n {numero} x 5 = {numero * 5}\n {numero} x 6 = {numero * 6}\n {numero} x 7 = {numero * 7}\n {numero} x 8 = {numero * 8}\n {numero} x 9 = {numero * 9}\n {numero} x 10 = {numero * 10}")

#Programa principal
numero_usuario = int(input("Por favor, ingrese un número para ver su tabla de multiplicar: "))

tabla_multiplicar(numero_usuario)

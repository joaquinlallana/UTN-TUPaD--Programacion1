#Definicion de la función
def saludar_usuario(nombre):
    return print(f"Hola {nombre}!")

#Programa principal
nombre_usuario = input("Por favor, ingrese su nombre: ")

saludar_usuario(nombre_usuario)
#Definición de la función
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

#Programa principal
nombre_usuario = input("Por favor, ingrese su nombre: ")

print(saludar_usuario(nombre_usuario))

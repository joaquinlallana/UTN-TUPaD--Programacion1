#Definicion de función
def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nnombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Programa principal
nombre_usuario = input("Por favor, ingrese su nombre: ")
apellido_usuario = input("Por favor, ingrese su apellido: ")
edad_usuario = input("Por favor, ingrese su edad: ")
residencia_usuario = input("Por favor, ingrese su lugar de residencia: ")

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)
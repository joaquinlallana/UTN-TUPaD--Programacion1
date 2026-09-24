#Definición de la función
def tabla_multiplicar(numero):
    tabla = f"Tabla de multiplicación del {numero}:"
    for i in range(1, 11):
        tabla += f"\n{numero} x {i} = {numero * i}"
    return tabla

#Programa principal
numero_usuario = int(input("Por favor, ingrese un número para ver su tabla de multiplicar: "))

print(tabla_multiplicar(numero_usuario))

#Definicion de la función
def segundos_a_horas(segundos):
    return segundos / 3600

#Programa principal

segundos_usuario = float(input("Por favor, ingrese la cantidad de segundos: "))

print(f"{segundos_usuario} segundos son equivalentes a {segundos_a_horas(segundos_usuario)} horas.")
#Definicion de la función
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#Programa principal
celsius_usuario = float(input("Por favor, ingrese la temperatura en grados Celsius: "))

print(f"{celsius_usuario} grados Celsius son equivalentes a {celsius_a_fahrenheit(celsius_usuario)} grados Fahrenheit.")
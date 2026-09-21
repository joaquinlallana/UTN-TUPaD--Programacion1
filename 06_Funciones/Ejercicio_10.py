#Definición de la función
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa principal
numero1 = int(input("Por favor, ingrese el primer número: "))
numero2 = int(input("Por favor, ingrese el segundo número: "))
numero3 = int(input("Por favor, ingrese el tercer número: "))

print(f"El promedio de los números ingresados es: {calcular_promedio(numero1, numero2, numero3)}")

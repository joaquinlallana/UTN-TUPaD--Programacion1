#Definición de la función
def operaciones_basicas(a, b):
    return a + b , a - b, a * b , a / b

#Programa principal
numero1 = int(input("Por favor, ingrese el primer número: "))
numero2 = int(input("Por favor, ingrese el segundo número: "))

resultado = operaciones_basicas(numero1, numero2)

print(f"Los resultados de las operaciones basicas son: \n Suma: {resultado[0]} \n Resta: {resultado [1]} \n Multiplicación: {resultado[2]} \n División: {resultado[3]}")
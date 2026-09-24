#Definición de la función
def operaciones_basicas(a, b):
    return a + b, a - b, a * b, a / b

#Programa principal
numero1 = int(input("Por favor, ingrese el primer número: "))
numero2 = int(input("Por favor, ingrese el segundo número: "))

while numero2 == 0:
    print("El segundo número no puede ser 0, ya que no se puede dividir por cero.")
    numero2 = int(input("Por favor, ingrese el segundo número nuevamente: "))

suma, resta, multiplicacion, division = operaciones_basicas(numero1, numero2)

print("Los resultados de las operaciones básicas son:")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division:.2f}")

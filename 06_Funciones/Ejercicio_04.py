import math
#Definición de las funciones
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

#Programa principal
radio_usuario = float(input("Por favor, ingrese el radio del círculo: "))

area = calcular_area_circulo(radio_usuario)

perimetro = calcular_perimetro_circulo(radio_usuario)

print(f"El area del circulo es: {area:.2f}")
print(f"El perímetro del circulo es: {perimetro:.2f}")

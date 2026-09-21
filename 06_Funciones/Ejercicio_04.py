#Definición de las funciones
def calcular_area_circulo(radio):
    return 3.14159 * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * 3.14159 * radio

#Programa principal
radio_usuario = float(input("Por favor, ingrese el radio del círculo: "))

area = calcular_area_circulo(radio_usuario)

perimetro = calcular_perimetro_circulo(radio_usuario)

print(f"El area del circulo es: {area}")
print (f"El perímetro del circulo es: {perimetro}")
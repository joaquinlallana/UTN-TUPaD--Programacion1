#Definición de la función
def calcular_imc(peso, altura):
    resultado = peso / (altura ** 2)
    return resultado

#Programa principal
peso_usuario = float(input("Por favor, ingrese su peso en kilogramos: "))
altura_usuario = float(input("Por favor, ingrese su altura en metros: "))

imc = calcular_imc(peso_usuario, altura_usuario)

print(f"Su indice de masa corporal (IMC) es: {imc:.2f}")
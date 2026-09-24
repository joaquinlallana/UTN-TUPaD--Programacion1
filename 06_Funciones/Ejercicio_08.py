#Definición de la función
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

#Programa principal
peso_usuario = float(input("Por favor, ingrese su peso en kilogramos: "))
altura_usuario = float(input("Por favor, ingrese su altura en metros: "))

if altura_usuario <= 0:
    print("La altura debe ser mayor a cero.")
else:
    imc = calcular_imc(peso_usuario, altura_usuario)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

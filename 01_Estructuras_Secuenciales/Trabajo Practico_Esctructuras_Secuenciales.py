#Ejercicio 1

print("Hola Mundo")

#Ejercicio 2

nombre = input("Ingrese su nombre: ")

print(f"Hola {nombre}!")

#Ejercicio 3

nombre = input("Ingrese su nombrre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Ejercicio 4

radio = float(input("Ingrese el radio de una circunferencia: "))
area = 3.14159 * radio ** 2
perimetro = 2 * 3.14159 * radio

print(f"El area de la circunferencia es: {area} y su perimetro es de: {perimetro}.")

#Ejercicio 5

segundos = int(input("Ingrese un tiempo en segundos: "))
horas = float(segundos // 3600)

print(f"Los segundos ingresados equivalen a {horas} horas.")

#Ejercicio 6

numero = int(input("ingrese un numero entero: "))

print(f"La tabla de multiplicar de dicho numero es: {numero} x 1 = {numero * 1}\n {numero} x 2 = {numero * 2}\n {numero} x 3 = {numero * 3}\n {numero} x 4 = {numero * 4}\n {numero} x 5 = {numero * 5}\n {numero} x 6 = {numero * 6}\n {numero} x 7 = {numero * 7}\n {numero} x 8 = {numero * 8}\n {numero} x 9 = {numero * 9}\n {numero} x 10 = {numero * 10}")

#Ejercicio 7

numero1 = int(input("Ingrese un numero entero distinto de cero: "))
numero2 = int(input("Ingrese otro numero entero distinto de cero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"La suma de los numeros ingresados es: {suma}\n La resta de los numeros ingresados es: {resta}\n La multiplicacion de los numeros ingresados es: {multiplicacion}\n La division de los numeros ingresados es: {division}")

#Ejercicio 8

altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / (altura ** 2)

print(f"Su indice de masa corporal es: {imc}")

#Ejercicio 9

temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (temperatura * 9/5) + 32

print(f"La temperatura ingresada en grados Fahrenheit es de: {fahrenheit}")

#Ejercicio 10

a = float(input("Ingrese un numero: "))
b = float(input("Ingrese otro numero: "))
c = float(input("Ingrese otro numero: "))

promedio = (a + b + c) / 3

print(f"El promedio de los numeros ingresados es: {promedio}")



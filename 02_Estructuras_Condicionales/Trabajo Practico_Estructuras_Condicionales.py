#Ejercicio 1

edad = int(input("Por favor, ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")

#-----------#

#Ejercicio 2

nota = int(input("Ingrese su nota: "))

if nota >= 6 :
    print("Aprobado")
else :
    print("Reprobado")

#-----------#

#Ejercicio 3

numero = int(input("Ingrese un numero: "))

if (numero % 2) == 0 :
    print("Ha ingresado un numero par")
else :
    print("Por favor, ingrese un numero par")

#-----------#

#Ejercicio 4

edad = int(input("Por favor, ingrese su edad: "))

if edad < 12 :
    print("Niño/a")
elif edad >= 12 and edad < 18 :
    print("Adolescente")
elif edad >= 18 and edad < 30 :
    print("Adulto/a joven")
elif edad >= 30 :
    print("Adulto/a")

#-----------#

#Ejercicio 5

password = input("Por favor, ingrese su contraseña: ")

if len(password) >= 8 and len(password) <= 14 :
    print("Ha ingresado la contraseña correcta")
else :
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#-----------#

#Ejercicio 6

consumo = int(input("Ingrese, por favor, su consumo mensaul de energia electrica en kilovatios (kWh): "))

if consumo < 150 :
    print("Consumo bajo")
elif consumo >=150 and consumo <= 300 :
    print("Consumo medio")
elif consumo > 300 :
    print("Consumo alto")
    if consumo > 500 :
        print("Considere medidas de ahorro energético")

#-----------#

#Ejercicio 7

sentencia = input("Ingrese una frase o palabra: ")

if sentencia[-1] == "a" or sentencia[-1] == "e" or sentencia[-1] == "i" or sentencia[-1] == "o" or sentencia[-1] == "u" :
    print(f"{sentencia}!")
else :
    print(sentencia)

#-----------#

#Ejercicio 8

nombre = input("Ingrese su nobre: ")
opcion = int(input('Ingrese el número de la opción que desea realizar \n 1. Si quiere su nombre en mayúsculas \n 2. Si quiere su nombre en minúsculas \n 3. Si quiere su nombre con la primera letra en mayúscula \n '))
if opcion == 1 :
    print(nombre.upper())
elif opcion == 2 :
    print(nombre.lower())
elif opcion == 3 :
    print(nombre.title()) 

#-----------#

#Ejercicio 9

terremoto = float(input("Ingrese la magintud del terremoto en escala de Richter: "))

if terremoto < 3 :
    print("Muy leve (imperceptible)")
elif terremoto >= 3 and terremoto < 4 :
    print("Leve (ligeremente perceptible)")
elif terremoto >= 4 and terremoto  < 5 :
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif terremoto >= 5 and terremoto  < 6 :
    print("Fuerte (puede causar daños en estructuras débiles)")
elif terremoto >= 6 and terremoto < 7 :
    print("Muy fuerte (puede causar daños significativos)")
elif terremoto >= 7 :
    print("Extremo (puede causar graves daños a gran escala)")

#-----------#

#Ejercicio 10

hemisferio = input("Por favor, ingrese en que hemisferio se encuentra Norte o Sur: ").lower()
mes = int(input("Por favor, ingrese el mes en el que se encuentra, en número (1-12): "))
dia = int(input("Por favor, ingrese el día en el que se encuentra: "))

if hemisferio == "norte":
    #[21/12 al 20/3]#
    if ((mes == 12 and dia >= 21 )) or mes == 1  or mes == 2 or (mes == 3 and dia <= 20) :
        print("Es invierno")
    #[21/3 al 20/6]#
    elif ( (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20)) :
        print("Es primavera")
    #[21/6 al 20/9]#
    elif( (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20)) :
        print("Es verano")
    #[21/9 al 20/12]#
    elif( (mes == 9 and dia >= 21) or mes ==10 or mes == 11 or (mes == 12 and dia <= 20)) :
        print("Es otoño")
elif hemisferio == "sur":
    #[21/6 al 20/9]#
    if ((mes == 6 and dia >= 21 )) or mes == 7  or mes == 8 or (mes == 9 and dia <= 20) :
        print("Es invierno")
    #[21/9 al 20/12]#
    elif ( (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20)) :
        print("Es primavera")
    #[21/12 al 20/3]#
    elif( (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20)) :
        print("Es verano")
    #[21/3 al 20/6]#
    elif( (mes == 3 and dia >= 21) or mes ==4 or mes ==5 or (mes ==6 and dia <=20)) :
        print("Es otoño")

#-----------#
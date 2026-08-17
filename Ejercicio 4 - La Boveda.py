energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial= ""
bloqueado = False

print(" ESCAPE ROOM - LA BOVEDA ")

nombre = input("Ingrese su nombre: ")
forzar_seguidas = 0

while nombre.isalpha() == False or nombre == "":
    print("El nombre ingresado no es válido. Por favor, ingrese un nombre válido.")
    nombre = input("Ingrese su nombre: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:
    print(f"\nHola {nombre}, tienes {energia} de energia y {tiempo} minutos para escapar de la boveda.")
    print("Elige que accion haccer \n 1) Forzar la cerradura \n 2) Hackear panel \n 3) Descansar")

    opcion = input("Seleccione una opcion: ")

    while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 3:
        print("La opción ingresada no es válida. Por favor, ingrese una opción válida del 1 al 3.")
        opcion = input("Seleccione una opcion: ")
    
    opcion = int(opcion)
    
    match opcion:
        case 1:
            energia -= 20
            tiempo -= 2
            forzar_seguidas += 1

            if forzar_seguidas == 3: #REGLA ANTI-SPAM
                alarma = True
                print ("La cerradura se trabo! Se activo la alarma")
            
            elif energia < 40 :
                numero = input("Ingresa un numero del 1 a 3 :")

                while numero.isdigit() == False or int(numero) < 1 or int(numero) > 3 :
                    print("Ingrese un numero correcto!")
                    numero = input("Ingresa un numero del 1 a 3 :")

                numero = int(numero)    

                if numero == 3 : 
                    alarma = True
                else:
                    cerraduras_abiertas += 1

            else:
                cerraduras_abiertas += 1
        case 2:
            forzar_seguidas = 0
            energia -= 10 
            tiempo -= 3

            print("Desencriptando...")

            for letra in range(1,5) :
                print(" * ")
                codigo_parcial += "A"

            if cerraduras_abiertas < 3 and len(codigo_parcial) >= 8 :
                print("Abriendo una cerradura")
                cerraduras_abiertas += 1
        case 3:
            forzar_seguidas = 0
            energia += 15 
            if energia > 100 : 
                energia = 100
            tiempo -= 1
            if alarma == True :
                energia -= 10

    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        bloqueado = True

if cerraduras_abiertas == 3:
    print(f"\n¡VICTORIA, {nombre}! Escapaste de la bóveda.")
elif bloqueado:
    print("\nDERROTA: el sistema se bloqueó por la alarma.")
elif energia <= 0:
    print("\nDERROTA: te quedaste sin energía.")
elif tiempo <= 0:
    print("\nDERROTA: se te acabó el tiempo.")


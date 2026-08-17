print("====== BIENVENIDO A LA ARENA ======")

nombre_gladiador = input("Ingresa el nombre de tu gladiador: ")

while nombre_gladiador.isalpha() == False or nombre_gladiador == "" :
    print("Error: Solo se permiten letras")
    nombre_gladiador = input("Ingresa el nombre de tu gladiador: ")

vida_gladiador = 100 
vida_enemigo = 100
pociones = 3
daño_base = 15
daño_base_enemigo = 12 
turno_gladiador = True

while vida_gladiador > 0 and vida_enemigo > 0 :
    print(f"{nombre_gladiador} - {vida_gladiador}HP vs  Gladiador enemigo - {vida_enemigo}HP | Pociones: {pociones}")

    print("--- TURNO DEL JUGADOR ---")
    while turno_gladiador == True :
        print("Elige accion: \n 1) Ataque pesado \n 2) Rafaga Veloz \n 3) Curar ")
        opcion = input("Opcion: ")
            
        while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 3:
            print("Error: Ingrese un numero válido ")
            print("Elige accion: \n 1) Ataque pesado \n 2) Rafaga Veloz \n 3) Curar ")
            opcion = input("Opcion: ")
            
        opcion = int(opcion)

        match opcion:
            case 1:
                if vida_enemigo < 20 :
                    golpe_critico = daño_base * 1.5 
                    vida_enemigo = vida_enemigo - golpe_critico
                    print(f">> Atacaste al enemigo con un Golpe Crítico, por {golpe_critico} puntos de daño ")
                else:
                    vida_enemigo = vida_enemigo - daño_base
                    print(f">> Atacaste al enemigo por {daño_base} puntos de daño ")

                turno_gladiador = False

            case 2:
                print(" >> Inicias una rafaga de golpes ")
                for golpe in range(3):
                    print(">Golpe conectado por 5 de daño")
                    vida_enemigo -= 5

                turno_gladiador = False

            case 3:
                if pociones > 0 :
                    print(" >> Te tomaste una poción para curar tu salud")
                    vida_gladiador += 30
                    if vida_gladiador > 100 :
                        vida_gladiador = 100
                    pociones -= 1
                    turno_gladiador = False
                else:
                    print("No quedan pociones!")
                    turno_gladiador = False

    if vida_enemigo > 0:
        print("--- TURNO DEL ENEMIGO ---")
        vida_gladiador -= daño_base_enemigo
        print(f" >> El enemigo te atacó por {daño_base_enemigo} puntos de daño")
        print("========================")

    turno_gladiador = True

if vida_gladiador <= 0:
    print("DERROTA. Has caído en combate.")
else:
    print(f"VICTORIA!! {nombre_gladiador} ha ganado la batalla en la Arena")

    
nombre = input("Ingrese su nombre: ")
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

while nombre.isalpha() == False or nombre == "":
    print("El nombre ingresado no es válido. Por favor, ingrese un nombre válido.")
    nombre = input("Ingrese su nombre: ")

print(f"Bienvenido {nombre} a la agenda de turnos")

continuar = True

while continuar:
    print("Menu de opciones: \n 1) Reservar turno \n 2) Cancelar turno (por nombre) \n 3) Ver agenda del dia \n 4) Ver resumen general \n 5) Cerrar sistema")

    opcion = input("Ingrese la opcion deseada del 1 al 5: ")

    while opcion.isdigit() == False or 1 < int(opcion) > 5:
        print("La opción ingresada no es válida. Por favor, ingrese una opción válida del 1 al 5.")
        opcion = input("Ingrese la opcion deseada del 1 al 5: ")

    opcion = int(opcion)

    match opcion:
        case 1:
            dia_turno = input("Elige el dia para reservar el turno \n 1) Lunes \n 2) Martes :")
            while dia_turno.isdigit() == False or int(dia_turno) > 1 and int(dia_turno) > 2:
                print("La opción ingresada no es válida. Por favor, ingrese una opción válida del 1 al 2.")
                dia_turno = input("Elige el dia para reservar el turno \n 1) Lunes \n 2) Martes :")

            nombre_paciente = input("Ingrese el nombre del paciente: ")
            while nombre_paciente.isalpha() == False or nombre_paciente == "":
                print("El nombre ingresado no es válido. Por favor, ingrese un nombre válido.")
                nombre_paciente = input("Ingrese el nombre del paciente: ")

            if dia_turno == "1":
                if nombre_paciente == lunes1 or nombre_paciente == lunes2 or nombre_paciente == lunes3 or nombre_paciente == lunes4:
                    print(f"{nombre_paciente} ya tiene un turno reservado el Lunes.")
                elif lunes1 == "":
                    lunes1 = nombre_paciente
                    print(f"Turno reservado para {nombre_paciente} el Lunes a las 9:00 AM")
                elif lunes2 == "":
                    lunes2 = nombre_paciente
                    print(f"Turno reservado para {nombre_paciente} el Lunes a las 10:00 AM")
                elif lunes3 == "":
                    lunes3 = nombre_paciente
                    print(f"Turno reservado para {nombre_paciente} el Lunes a las 11:00 AM")
                elif lunes4 == "":
                    lunes4 = nombre_paciente
                    print(f"Turno reservado para {nombre_paciente} el Lunes a las 12:00 PM")
                else:
                    print("No hay turnos disponibles el Lunes.")

            elif dia_turno == "2":
                if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                    print(f"{nombre_paciente} ya tiene un turno reservado el Martes.")
                elif martes1 == "":
                    martes1 = nombre_paciente
                    print(f"Turno reservado para {nombre_paciente} el Martes a las 9:00 AM")
                elif martes2 == "":
                    martes2 = nombre_paciente
                    print(f"Turno reservado para {nombre_paciente} el Martes a las 10:00 AM")
                elif martes3 == "":
                    martes3 = nombre_paciente
                    print(f"Turno reservado para {nombre_paciente} el Martes a las 11:00 AM")
                else:
                    print("No hay turnos disponibles el Martes.")

        case 2:
            dia_cancelar = input("Elige el dia para cancelar el turno \n 1) Lunes \n 2) Martes :")
            while dia_cancelar.isdigit() == False or 1 < int(dia_cancelar) > 2:
                print("La opción ingresada no es válida. Por favor, ingrese una opción válida del 1 al 2.")
                dia_cancelar = input("Elige el dia para cancelar el turno \n 1) Lunes \n 2) Martes :")

            nombre_cancelar = input("Ingrese el nombre del paciente a cancelar el turno: ")
            while nombre_cancelar.isalpha() == False or nombre_cancelar == "":
                print("El nombre ingresado no es válido. Por favor, ingrese un nombre válido.")
                nombre_cancelar = input("Ingrese el nombre del paciente a cancelar el turno: ")

            if dia_cancelar == "1":
                if nombre_cancelar == lunes1:
                    lunes1 = ""
                    print(f"Turno cancelado para {nombre_cancelar} el Lunes a las 9:00 AM")
                elif nombre_cancelar == lunes2:
                    lunes2 = ""
                    print(f"Turno cancelado para {nombre_cancelar} el Lunes a las 10:00 AM")
                elif nombre_cancelar == lunes3:
                    lunes3 = ""
                    print(f"Turno cancelado para {nombre_cancelar} el Lunes a las 11:00 AM")
                elif nombre_cancelar == lunes4:
                    lunes4 = ""
                    print(f"Turno cancelado para {nombre_cancelar} el Lunes a las 12:00 PM")
                else:
                    print(f"No se encontró un turno reservado para {nombre_cancelar} el Lunes.")
            else:
                if nombre_cancelar == martes1:
                    martes1 = ""
                    print(f"Turno cancelado para {nombre_cancelar} el Martes a las 9:00 AM")
                elif nombre_cancelar == martes2:
                    martes2 = ""
                    print(f"Turno cancelado para {nombre_cancelar} el Martes a las 10:00 AM")
                elif nombre_cancelar == martes3:
                    martes3 = ""
                    print(f"Turno cancelado para {nombre_cancelar} el Martes a las 11:00 AM")
                else:
                    print(f"No se encontró un turno reservado para {nombre_cancelar} el Martes.")

        case 3:
            dia_ver = input("Elige el dia para ver la agenda \n 1) Lunes \n 2) Martes ")
            while dia_ver.isdigit() == False or 1 < int(dia_ver) > 2:
                print("La opción ingresada no es válida. Por favor, ingrese una opción válida del 1 al 2.")
                dia_ver = input("Elige el dia para ver la agenda \n 1) Lunes \n 2) Martes ")

            if dia_ver == "1" :
                print("Agenda del Lunes:")
                print(f"Turno 1 - {lunes1 if lunes1 else '(libre)'}")
                print(f"Turno 2 - {lunes2 if lunes2 else '(libre)'}")
                print(f"Turno 3 - {lunes3 if lunes3 else '(libre)'}")
                print(f"Turno 4 - {lunes4 if lunes4 else '(libre)'}")
            else:
                print("Agenda del Martes:")
                print(f"Turno 1 - {martes1 if martes1 else '(libre)'}")
                print(f"Turno 2 - {martes2 if martes2 else '(libre)'}")
                print(f"Turno 3 - {martes3 if martes3 else '(libre)'}")

        case 4:
            print("Resumen general de turnos:")

            ocupados_lunes = 0
            if lunes1 != "":
                ocupados_lunes += 1
            if lunes2 != "":
                ocupados_lunes += 1
            if lunes3 != "":
                ocupados_lunes += 1
            if lunes4 != "":
                ocupados_lunes += 1
            disponibles_lunes = 4 - ocupados_lunes

            ocupados_martes = 0
            if martes1 != "":
                ocupados_martes += 1
            if martes2 != "":
                ocupados_martes += 1
            if martes3 != "":
                ocupados_martes += 1
            disponibles_martes = 3 - ocupados_martes

            print(f"Lunes: {ocupados_lunes} turno(s) ocupado(s), {disponibles_lunes} disponible(s)")
            print(f"Martes: {ocupados_martes} turno(s) ocupado(s), {disponibles_martes} disponible(s)")

            if ocupados_lunes > ocupados_martes:
                print("El día con más turnos reservados es el Lunes.")
            elif ocupados_martes > ocupados_lunes:
                print("El día con más turnos reservados es el Martes.")
            else:
                print("Hay un empate entre Lunes y Martes en turnos reservados.")

        case 5:
            print("Cerrando el sistema. ¡Hasta luego!")
            continuar = False

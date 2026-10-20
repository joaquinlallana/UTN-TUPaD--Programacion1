#Ejercicio 9: Agenda por día y hora
agenda = {
("lunes", "10:00"): "Reunión",
("martes", "15:00"): "Clase de inglés"
}

# Se aceptan los días con o sin tilde y se guardan siempre sin tilde
dias_validos = {
    "lunes": "lunes",
    "martes": "martes",
    "miercoles": "miercoles",
    "miércoles": "miercoles",
    "jueves": "jueves",
    "viernes": "viernes",
    "sabado": "sabado",
    "sábado": "sabado",
    "domingo": "domingo"
}

def menu():
    print("\nMenu de opciones:")
    print("1. Consultar agenda")
    print("2. Agregar evento")
    print("3. Salir")

def pedir_dia():
    while True:
        dia = input("Ingrese el día de la semana: ").strip().lower()
        if dia in dias_validos:
            return dias_validos[dia]
        print("Día inválido. Ingrese un día de la semana (ej: lunes).")

def pedir_hora():
    while True:
        hora = input("Ingrese la hora (formato HH:MM): ").strip()
        partes = hora.split(":")
        if len(partes) == 2 and partes[0].isdigit() and partes[1].isdigit():
            horas = int(partes[0])
            minutos = int(partes[1])
            if 0 <= horas <= 23 and 0 <= minutos <= 59 and len(partes[1]) == 2:
                # Se normaliza para que "9:00" y "09:00" sean la misma hora
                return f"{horas:02d}:{minutos:02d}"
        print("Hora inválida. Use el formato HH:MM (ej: 09:30).")

def pedir_evento():
    while True:
        evento = input("Ingrese el nombre del evento: ").strip()
        if evento:
            return evento
        print("El nombre del evento no puede estar vacío.")

def consultar_agenda(dia, hora):
    return agenda.get((dia, hora))

def agregar_evento(dia, hora, evento):
    if (dia, hora) in agenda:
        print(f"Ya hay un evento programado para el {dia} a las {hora}.")
    else:
        agenda[(dia, hora)] = evento
        print(f"Evento '{evento}' agregado para el {dia} a las {hora}.")


while True:
    menu()
    opcion = input("Seleccione una opción (1-3): ").strip()

    if opcion == "1":
        dia = pedir_dia()
        hora = pedir_hora()
        evento = consultar_agenda(dia, hora)
        if evento:
            print(f"El {dia} a las {hora} tenés: {evento}.")
        else:
            print(f"No hay eventos programados para el {dia} a las {hora}.")

    elif opcion == "2":
        dia = pedir_dia()
        hora = pedir_hora()
        evento = pedir_evento()
        agregar_evento(dia, hora, evento)

    elif opcion == "3":
        print("Saliendo de la agenda.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

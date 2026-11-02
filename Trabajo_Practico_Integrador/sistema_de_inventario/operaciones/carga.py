# Opciones que agregan herramientas al inventario: carga múltiple (1) y alta (5)

from auxiliares.validaciones import pedir_entero, validar_nombre_nuevo


def cargar_herramientas(inventario):
    # Opción 1: carga múltiple de herramientas con su stock inicial
    while True:  # Pide cuántas herramientas distintas se van a cargar (entero mayor o igual a 1)
        try:
            cantidad_herramientas = pedir_entero("Ingrese la cantidad de herramientas distintas a cargar: ", 1)
            break
        except ValueError as e:
            print(f"Error: {e}")

    for i in range(cantidad_herramientas):
        while True:  # Pide el nombre hasta que no esté vacío ni repetido en el inventario
            try:
                nombre = input(f"Ingrese el nombre de la herramienta {i + 1}: ")
                nombre = validar_nombre_nuevo(inventario, nombre)
                break
            except ValueError as e:
                print(f"Error: {e}")

        while True:  # Pide el stock inicial (entero mayor o igual a 0) conservando el nombre
            try:
                stock = pedir_entero(f"Ingrese el stock inicial de {nombre}: ", 0)
                break
            except ValueError as e:
                print(f"Error: {e}")

        inventario.append({'herramienta': nombre, 'cantidad': stock})


def alta_producto(inventario):
    # Opción 5: agrega una herramienta nueva al final del inventario.
    # Los errores no se capturan acá: los recibe el except de main().
    nombre = input("Ingrese el nombre de la herramienta que desea agregar al inventario: ")
    nombre = validar_nombre_nuevo(inventario, nombre)

    stock = pedir_entero(f"Ingrese el stock inicial de {nombre}: ", 0)

    inventario.append({'herramienta': nombre, 'cantidad': stock})
    print("Herramienta agregada con éxito")

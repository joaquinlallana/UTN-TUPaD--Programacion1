# Opción que modifica el stock de una herramienta existente: venta o ingreso (6)

from auxiliares.validaciones import pedir_entero, validar_nombre
from auxiliares.busqueda import buscar_herramienta


def actualizar_stock(inventario):
    # Opción 6: registra una venta o un ingreso de unidades
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    nombre = input("Ingrese el nombre de la herramienta cuyo stock desea actualizar: ")
    nombre = validar_nombre(nombre)
    producto = buscar_herramienta(inventario, nombre)
    if producto == None:
        print("La herramienta ingresada no existe en el inventario.")
        return

    movimiento = input("¿Qué desea registrar? \n 1) Venta \n 2) Ingreso \n Elija una opción >> ")
    if movimiento != '1' and movimiento != '2':
        print("No se seleccionó ninguna opción válida.")
        return

    unidades = pedir_entero("Ingrese la cantidad de unidades: ", 1)

    if movimiento == '1':
        if producto['cantidad'] < unidades:
            raise ValueError(f"La herramienta {producto['herramienta']} no tiene suficiente stock.")
        producto['cantidad'] = producto['cantidad'] - unidades
        print(f"Venta registrada: {unidades} unidades de {producto['herramienta']}. Stock actual: {producto['cantidad']}.")
    else:
        producto['cantidad'] = producto['cantidad'] + unidades
        print(f"Ingreso registrado: {unidades} unidades de {producto['herramienta']}. Stock actual: {producto['cantidad']}.")

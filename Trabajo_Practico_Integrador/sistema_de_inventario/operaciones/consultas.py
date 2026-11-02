# Opciones que consultan el inventario sin modificarlo: listado (2), consulta (3) y agotados (4)

from auxiliares.validaciones import validar_nombre
from auxiliares.busqueda import buscar_herramienta


def mostrar_inventario(inventario):
    # Opción 2: muestra todas las herramientas con su stock
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    print("\n >>> Inventario de herramientas:")
    for producto in inventario:
        print(f"Herramienta: {producto['herramienta']}, Stock: {producto['cantidad']}")


def consultar_stock(inventario):
    # Opción 3: muestra el stock de una herramienta buscada por nombre
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    nombre = input("Ingrese el nombre de la herramienta cuyo stock desea consultar: ")
    nombre = validar_nombre(nombre)
    producto = buscar_herramienta(inventario, nombre)
    if producto == None:
        print("La herramienta no se encuentra en el inventario.")
        return

    print(f"La herramienta {producto['herramienta']} cuenta con un stock de {producto['cantidad']}")


def reporte_agotados(inventario):
    # Opción 4: muestra solo las herramientas con stock cero
    if len(inventario) == 0:
        print("Todavía no hay herramientas cargadas.")
        return

    contador_agotados = 0
    for producto in inventario:
        if producto['cantidad'] == 0:
            contador_agotados += 1

    if contador_agotados == 0:
        print("Todas las herramientas en el inventario tienen stock disponible.")
    else:
        print("Las herramientas que se encuentran sin stock son: ")
        for producto in inventario:
            if producto['cantidad'] == 0:
                print("> ", producto['herramienta'])

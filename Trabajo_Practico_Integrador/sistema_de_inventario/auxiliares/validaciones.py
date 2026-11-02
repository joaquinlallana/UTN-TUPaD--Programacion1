# Funciones auxiliares de validación de datos ingresados por el usuario

from auxiliares.busqueda import buscar_herramienta


def pedir_entero(mensaje, minimo):
    # Pide un número entero y verifica que no sea menor que el mínimo.
    # Si no se puede convertir, captura el ValueError de int() 
    # y lo relanza con un mensaje en español.
    try:
        numero = int(input(mensaje))
    except ValueError:
        raise ValueError("Debe ingresar un número entero (no letras, símbolos ni decimales).")
    if numero < minimo:
        raise ValueError(f"El valor ingresado debe ser mayor o igual a {minimo}.")
    return numero


def validar_nombre(nombre):
    # Rechaza un nombre vacío o con solo espacios y lo devuelve sin espacios en los extremos
    if nombre.strip() == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")
    return nombre.strip()


def validar_nombre_nuevo(inventario, nombre):
    # Valida el nombre y además que la herramienta no esté ya cargada en el inventario
    nombre = validar_nombre(nombre)
    if buscar_herramienta(inventario, nombre) != None:
        raise ValueError(f"La herramienta '{nombre}' ya existe en el inventario.")
    return nombre

# Función auxiliar de búsqueda de herramientas en el inventario


def buscar_herramienta(inventario, nombre):
    # Devuelve la herramienta cuyo nombre coincide (sin importar mayúsculas ni espacios), o None
    for producto in inventario:
        if producto['herramienta'].lower() == nombre.strip().lower():
            return producto
    return None

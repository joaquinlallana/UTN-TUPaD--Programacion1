# Texto del menú principal y lectura de la opción elegida


def mostrar_menu():
    # Imprime las 7 opciones del menú
    print("\nOpciones:")
    print("1. Carga de herramientas con existencias iniciales")
    print("2. Visualización del inventario")
    print("3. Consulta de stock")
    print("4. Reporte de agotados")
    print("5. Alta de nuevo producto")
    print("6. Actualización de stock (venta / ingreso)")
    print("7. Salir")


def pedir_opcion():
    # Pide la opción del menú. Si no se puede convertir a entero (letras, símbolos o decimales),
    # captura el ValueError de int() y lo relanza con un mensaje en español para que lo muestre main().
    try:
        return int(input("Seleccione una opción: "))
    except ValueError:
        raise ValueError("Solo se pueden ingresar números enteros del 1 al 7 (no letras, símbolos ni decimales).")

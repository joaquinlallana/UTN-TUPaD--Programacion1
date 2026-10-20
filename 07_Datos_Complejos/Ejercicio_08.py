#Ejercicio 8: Stock de productos
stock = {"arroz": 10, "fideos": 5, "azucar": 8}

def agregar_cantidad(producto, cantidad):
    if producto in stock:
        stock[producto] += cantidad
    else:
        stock[producto] = cantidad

def consultar_stock(producto):
    return stock[producto]

def mostrar_menu():
    print("\nMenu de opciones:")
    print("1. Consultar stock de un producto")
    print("2. Agregar un producto")
    print("3. Agregar cantidad a un producto existente")
    print("4. Salir")

def pedir_producto(mensaje):
    producto = input(mensaje).strip().lower()
    while producto == "":
        print("El nombre no puede estar vacío.")
        producto = input(mensaje).strip().lower()
    return producto

def pedir_cantidad(mensaje):
    cantidad = input(mensaje).strip()
    while not cantidad.isdigit() or int(cantidad) == 0:
        print("Cantidad inválida. Ingrese un número entero mayor a 0.")
        cantidad = input(mensaje).strip()
    return int(cantidad)

def pedir_confirmacion(mensaje):
    respuesta = input(mensaje).strip().lower()
    while respuesta not in ("s", "n"):
        print("Respuesta inválida. Ingrese 's' o 'n'.")
        respuesta = input(mensaje).strip().lower()
    return respuesta == "s"

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        producto = pedir_producto("Ingrese el nombre del producto a consultar: ")
        if producto in stock:
            print(f"Stock de {producto}: {consultar_stock(producto)}")
        else:
            print(f"El producto {producto} no existe en el stock.")

    elif opcion == "2":
        producto = pedir_producto("Ingrese el nombre del producto a agregar: ")
        if producto in stock:
            print(f"El producto {producto} ya existe. Use la opción 3 para agregar cantidad.")
            continue

        cantidad = pedir_cantidad("Ingrese la cantidad del producto: ")
        agregar_cantidad(producto, cantidad)
        print(f"Producto {producto} agregado con cantidad {cantidad}.")

    elif opcion == "3":
        producto = pedir_producto("Ingrese el nombre del producto existente: ")
        if producto not in stock:
            print(f"El producto {producto} no existe en el stock.")
            if pedir_confirmacion("¿Desea agregarlo? (s/n): "):
                cantidad = pedir_cantidad("Ingrese la cantidad del producto: ")
                agregar_cantidad(producto, cantidad)
                print(f"Producto {producto} agregado con cantidad {cantidad}.")
            continue

        cantidad = pedir_cantidad("Ingrese la cantidad a agregar: ")
        agregar_cantidad(producto, cantidad)
        print(f"Cantidad {cantidad} agregada al producto {producto}.")

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

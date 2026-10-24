# ----- FUNCIONES DEL SISTEMA DE INVENTARIO -----

def cargar_herramientas(inventario):
    # Función para cargar herramientas con existencias iniciales
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de herramientas distintas a cargar: "))
            validar_cantidad(cantidad,1)
            break
        except ValueError as e:
            print(f"Error: {e}")

    for i in range(cantidad):
        while True: #Verifica que el nombre de la herramienta no esté vacío y que no exista en el inventario
            try:
                nombre = input(f"Ingrese el nombre de la herramienta {i+ 1}: ")
                nombre = validar_nombre(nombre)
                existencia = validar_existencia(inventario, nombre)
                if existencia:
                    raise ValueError(f"La herramienta '{nombre}' ya existe en el inventario.")
                break
            except ValueError as e:
                print(f"Error: {e}")
        while True:#Verifica que el stock inicial sea un número positivo
            try:    
                stock = int (input(f"Ingrese el stock inicial de {nombre}: "))
                validar_cantidad(stock,0)
                break
            except ValueError as e:
                print(f"Error: {e}")

        inventario.append({'herramienta' : nombre, 'cantidad': stock})

def mostrar_inventario(inventario):
    # Función para mostrar el inventario completo
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return

    print("\n >>> Inventario de herramientas:")
    for producto in inventario:
        print(f"Herramienta: {producto['herramienta']}, Stock: {producto['cantidad']}")

def consultar_stock(inventario):
    # Función para consultar el stock de un producto específico
    pass  # Implementar la lógica de consulta de stock

def reporte_agotados(inventario):
    #Funcion para mostrar las herramientas que estan sin stock
    contador = 0

    if len(inventario) == 0:
        print("El inventario esta vacio.")
        return
    for herramienta in inventario:
        if herramienta['cantidad'] == 0 : 
            contador += 1
    if contador == 0:
        print("Todas las herramientas en el inventario tienen stock disponible.")
    else:
        print("Las herramientas que se encuentran sin stock son: ")
        for herramienta in inventario:
            if herramienta['cantidad'] == 0:
                print("> ", herramienta['herramienta'])

def alta_producto(inventario):
    # Función para dar de alta un nuevo producto en el inventario
    pass  # Implementar la lógica de alta de nuevo producto

def actualizar_stock(inventario):
    # Función para actualizar el stock de un producto (venta o ingreso)
    pass  # Implementar la lógica de actualización de stock

# ----- FUNCIONES AUXILIARES DE VALIDACION -----

def validar_cantidad(cantidad, minimo):
    # Función para validar la cantidad ingresada
    if cantidad < minimo:
        raise ValueError(f"El valor ingresado deber ser mayor o igual a {minimo}.")
    return cantidad

def validar_nombre (herramienta):
    # Función para validar el nombre de la herramienta
    if herramienta.strip() == "":
        raise ValueError("El nombre de la herramienta no puede estar vacío.")
    return herramienta.strip()

def validar_existencia (inventario, herramienta):
    # Función para validar si la herramienta existe en el inventario
    busqueda = herramienta.strip().lower()
    for producto in inventario:
        if producto['herramienta'].lower() == busqueda:
            return True
    return False




# Código principal del sistema de inventario
def main(): 

    print("===== Bienvenido al Sistema de control de Inventario =====")

    inventario = [] # Lista para almacenar los productos en diccionarios

    while True:
        print("\nOpciones:")
        print("1. Carga de herramientas con existencias iniciales")
        print("2. Visualización del inventario")
        print("3. Consulta de stock")
        print("4. Reporte de agotados")
        print("5. Alta de nuevo Producto")
        print("6. Actualizacion de stock (venta / ingreso)")
        print("7. Salir")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                cargar_herramientas(inventario)
            elif opcion == 2:
                mostrar_inventario(inventario)
            elif opcion == 3:
                consultar_stock(inventario)
            elif opcion == 4:
                reporte_agotados(inventario)
            elif opcion == 5:
                alta_producto(inventario)
            elif opcion == 6:
                actualizar_stock(inventario)
            elif opcion == 7:
                print("Saliendo del sistema...")
                break
            else:
                raise ValueError("Opción fuera de rango. Ingrese un número del 1 al 7.")
        except ValueError as e:
            print(f"Error: {e}")
        
main()  # Llamada a la función principal para iniciar el programa
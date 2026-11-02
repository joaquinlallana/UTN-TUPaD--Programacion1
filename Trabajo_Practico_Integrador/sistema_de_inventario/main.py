# Sistema de Control de Inventario - TPI Programación 1
# Punto de entrada del programa. Este archivo contiene la función principal que inicia el sistema de control de inventario.

from interfaz.menu import mostrar_menu, pedir_opcion
from operaciones.carga import cargar_herramientas, alta_producto
from operaciones.consultas import mostrar_inventario, consultar_stock, reporte_agotados
from operaciones.movimientos import actualizar_stock


def main():
    print("===== Bienvenido al Sistema de control de Inventario =====")

    inventario = []  # Lista de diccionarios con las herramientas

    while True:
        mostrar_menu()
        try:
            opcion = pedir_opcion()
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

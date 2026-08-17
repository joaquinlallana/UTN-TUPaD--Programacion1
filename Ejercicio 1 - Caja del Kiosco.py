print("Bienvenido al Kiosco")

nombre = input("Ingrese su nombre: ")

while nombre.isalpha() == False or nombre == "":
    print("El nombre ingresado no es válido. Por favor, ingrese un nombre válido.")
    nombre = input("Ingrese su nombre: ")

cantidad = input("Ingrese la cantidad de productos que desea comprar: ")

while cantidad.isdigit() == False or int(cantidad) <= 0:
    print("La cantidad ingresada no es válida. Por favor, ingrese una cantidad válida.")
    cantidad = input("Ingrese la cantidad de productos que desea comprar: ")

cantidad = int(cantidad)

precio_total_sin_descuento = 0
precio_total_con_descuento = 0
ahorro_total = 0

print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")

for producto in range(cantidad):

    precio = input(f"Ingrese el precio del producto {producto + 1}: ")

    while precio.isdigit() == False:
        print("El precio ingresado no es válido. Por favor, ingrese un precio válido.")
        precio = input(f"Ingrese el precio del producto {producto + 1}: ")

    precio = int(precio)

    precio_total_sin_descuento += precio

    descuento = input("Ingrese si el producto posee o no descuento (S/N): ")

    while descuento.upper() not in ["S", "N"]:
        print("La opción ingresada no es válida. Por favor, ingrese S para sí o N para no.")
        descuento = input("Ingrese si el producto posee o no descuento (S/N): ")

    if descuento.upper() == "S":
        precio_descontado = precio * 0.10
        precio_total = precio - precio_descontado
        ahorro_total += precio_descontado
    else:
        precio_total = precio

    precio_total_con_descuento += precio_total

    print(f"Producto {producto + 1} - Precio: ${precio} - Descuento (S/N): {descuento.upper()}")

precio_promedio_por_producto = float(precio_total_con_descuento / cantidad)

print(f"Total sin descuentos: ${precio_total_sin_descuento}")
print(f"Total con descuentos: ${precio_total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${precio_promedio_por_producto:.2f}")




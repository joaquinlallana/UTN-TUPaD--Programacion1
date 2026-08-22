lista_productos = []
cantidad_productos = 5
cantidad = 1

print("Ingrese 5 productos a la lista")

while cantidad <= cantidad_productos :
    producto = input("Ingrese el nombre del producto: ")
    lista_productos.append(producto)
    cantidad += 1

lista_productos.sort()

print(f"Los productos ingresados a la lista son: {lista_productos}")

producto_a_eliminar = input("Ingrese que producto desea eliminar: ")


if producto_a_eliminar in lista_productos :
    lista_productos.remove(producto_a_eliminar)
else:
    print("El producto no se encuentra en la lista")

print("La lista al final quedaria con los siguientes productos: ")
print(lista_productos)


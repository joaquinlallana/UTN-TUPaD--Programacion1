lista_productos = []
cantidad_productos = 5
cantidad = 1

print("Ingrese 5 productos a la lista")

while cantidad <= cantidad_productos :
    producto = input("Ingrese el nombre del producto: ")
    lista_productos.append(producto)
    cantidad += 1

lista_productos = sorted(lista_productos)

print("Los productos ingresados a la lista, ordenados alfabéticamente, son: ")
for producto in lista_productos :
    print(f"> {producto}")

producto_a_eliminar = input("Ingrese que producto desea eliminar: ")


if producto_a_eliminar in lista_productos :
    lista_productos.remove(producto_a_eliminar)
else:
    print("El producto no se encuentra en la lista")

print("La lista al final quedaria con los siguientes productos: ")
for producto in lista_productos :
    print(f"> {producto}")


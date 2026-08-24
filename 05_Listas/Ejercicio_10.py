productos = ["Jabon" , "Detergente" , "Shampoo", "Lavandina"]
dias = ["Domingo","Lunes","Martes", "Mércoles", "Jueves", "Viernes", "Sábado"]
registro_ventas = [[10,2,4,1], [5,3,5,2], [3,1,13,5], [2,10,7,12], [4,5,9,1], [5,12,4,10], [1,4,6,16]]
registro_total_semana = [0]*7
registro_total_productos = [0, 0, 0, 0]

for indice, i in enumerate(registro_ventas) :
    sumatoria = 0
    for indice_2, j in enumerate(i) :
        sumatoria += j
        registro_total_productos[indice_2] += j

    registro_total_semana[indice] = sumatoria

producto_mas_vendido = max(registro_total_productos)
indice_mas_vendido = registro_total_productos.index(producto_mas_vendido)

mayor_venta_semanal = max(registro_total_semana)
indice_mayor_venta = registro_total_semana.index(mayor_venta_semanal)

print("--- VENTAS TOTALES POR PRODUCTOS ---")
for indice, i in enumerate(productos) :
    print(f" > {i} : {registro_total_productos[indice]}")

print("\n")
print("-- PRODUCTO MAS VENDIDO -- ")
print(f"El producto mas vendido de la semana fue {productos[indice_mas_vendido]} con un total de ventas de {producto_mas_vendido} unidades.")

print("\n")
print("-- DIA DE MAYORES VENTAS -- ")
print(f"El dia que se registraron mas ventas es el {dias[indice_mayor_venta]} con un total de ventas de {mayor_venta_semanal} unidades entre todos los productos.")
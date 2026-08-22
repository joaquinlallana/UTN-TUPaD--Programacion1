notas = [10 , 5 , 6 , 8 , 7 , 6.4 , 3 , 7.5 , 4 , 9 ]
sumatoria = 0
nota_alta = 0
nota_baja = 11

for nota in notas :
    print(nota)
    sumatoria += nota
    if nota > nota_alta :
        nota_alta = nota
    elif nota < nota_baja : 
        nota_baja = nota

promedio = float( sumatoria / 10)

print(f"El promedio de las notas es de {promedio}")
print(f"La nota mas alta es: {nota_alta}")
print(f"La nota mas baja es: {nota_baja}")



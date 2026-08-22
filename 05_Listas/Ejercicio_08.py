notas_alumnos = [[10,8,7], [6,7,9], [1,5,7], [7,3,8], [5,10,7]]
sumatoria_materia_1 = 0
sumatoria_materia_2 = 0
sumatoria_materia_3 = 0

for i in notas_alumnos:
    alumno = notas_alumnos.index(i) + 1
    promedio = 0
    sumatoria_notas = 0
    for indice, j in enumerate(i):
        sumatoria_notas += j
        if indice == 0 :
            sumatoria_materia_1 += j
        elif indice == 1 :
            sumatoria_materia_2 += j
        else :
            sumatoria_materia_3 += j

    promedio = sumatoria_notas / 3

    print(f"El promedio del alumno {alumno} es de {promedio:.2f}")

promedio_materia_1 = sumatoria_materia_1 / 5 
promedio_materia_2 = sumatoria_materia_2 / 5 
promedio_materia_3 = sumatoria_materia_3 / 5

print(f"El promedio de la materia 1 es de {promedio_materia_1:.2f}")
print(f"El promedio de la materia 2 es de {promedio_materia_2:.2f}")
print(f"El promedio de la materia 3 es de {promedio_materia_3:.2f}")



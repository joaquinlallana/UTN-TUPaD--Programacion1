pronostico_semana = [[15,3], [16,5], [15,7], [19,9], [24,14], [21,12], [21,11]]
temperatura_mas_baja =100
temperatura_mas_alta =0
sumatoria_maximas = 0
sumatoria_minimas =0
mayor_amplitud = 0
dia_mayor_amplitud = -1

for i in pronostico_semana :
    sumatoria_maximas += i[0]
    sumatoria_minimas += i[1]
    for j in i :
        if j < temperatura_mas_baja : 
            temperatura_mas_baja = j
        elif j > temperatura_mas_alta : 
            temperatura_mas_alta = j
        else : 
            pass
    amplitud = i[0] - i[1]
    if amplitud > mayor_amplitud :
        mayor_amplitud = amplitud
        dia_mayor_amplitud = pronostico_semana.index(i)

promedio_maximas = sumatoria_maximas / 7
promedio_minimas = sumatoria_minimas / 7

print(f"El promedio de temperaturas maximas es de {promedio_maximas:.2f} y el promedio de temperaturas minimas es de {promedio_minimas:.2f}")

match dia_mayor_amplitud:
    case 0:
        print(f"El dia de mayor amplitud fue el Domingo con una maxima de {pronostico_semana[0][0]} y la minima es de {pronostico_semana[0][1]}")
    case 1:
        print(f"El dia de mayor amplitud fue el Lunes con una maxima de {pronostico_semana[1][0]} y la minima es de {pronostico_semana[1][1]}")
    case 2:
        print(f"El dia de mayor amplitud fue el Martes con una maxima de {pronostico_semana[2][0]} y la minima es de {pronostico_semana[2][1]}")
    case 3:
        print(f"El dia de mayor amplitud fue el Miercoles con una maxima de {pronostico_semana[3][0]} y la minima es de {pronostico_semana[3][1]}")
    case 4:
        print(f"El dia de mayor amplitud fue el Jueves con una maxima de {pronostico_semana[4][0]} y la minima es de {pronostico_semana[4][1]}")
    case 5:
        print(f"El dia de mayor amplitud fue el Viernes con una maxima de {pronostico_semana[5][0]} y la minima es de {pronostico_semana[5][1]}")
    case 6:
        print(f"El dia de mayor amplitud fue el Sabado con una maxima de {pronostico_semana[6][0]} y la minima es de {pronostico_semana[6][1]}")

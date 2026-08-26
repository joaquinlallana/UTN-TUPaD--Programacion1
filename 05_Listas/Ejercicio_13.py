puntajes = [450, 1200, 875, 990, 300, 1500, 640]
mayor = max(puntajes)
menor = min(puntajes)
posicion_buscada = 0

puntajes.sort(reverse=True)

print(f"-- El puntaje mas alto es de : {mayor}")
print(f"-- El puntaje mas bajo es de : {menor}")

print(f">> RANKING << ")
for index , puntaje in enumerate(puntajes) : 
    print(f"> {index + 1} <  - {puntaje} ")
    if puntaje == 990 : 
        posicion_buscada = index

print(f"-- El puntaje de 990 se encuentra en la posicion {posicion_buscada +1} en el Ranking" )


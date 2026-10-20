#Ejercicio 6: Promedio de notas por alumno
alumnos = {}
i = 0

def agregar_alumno(nombre, notas):
    alumnos[nombre] = notas

def calcular_promedio(nombre):
    if nombre in alumnos:
        notas = alumnos[nombre]
        promedio = sum(notas) / len(notas)
        return promedio
    else:
        return None

while i < 3 : 
    nombre = input("Ingrese el nombre del alumno: ").strip()
    if nombre == "" or not nombre.replace(" ", "").isalpha():
        print("Nombre inválido. Ingrese un nombre válido.")
        continue
    elif nombre in alumnos:
        print("El alumno ya existe. Ingrese otro nombre.")
        continue

    notas = []
    while len(notas) < 3:
        entrada = input(f"Ingrese la nota {len(notas)+1} del alumno {nombre}: ")
        if not entrada.replace(".", "", 1).isdigit():
            print("Nota inválida. Debe ser un número.")
            continue
        nota = float(entrada)
        if nota < 0 or nota > 10:
            print("Nota inválida. Ingrese una nota entre 0 y 10.")
            continue
        notas.append(nota)
    notas = tuple(notas)
    agregar_alumno(nombre, notas)
    i += 1 

print("\nPromedios de los alumnos:")
for nombre in alumnos:
    promedio = calcular_promedio(nombre)
    print(f"{nombre}: {promedio:.2f}")

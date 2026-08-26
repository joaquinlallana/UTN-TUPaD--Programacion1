estudiantes = ["Joaquin" , "Martina" , "Maria" , "Javier" , "Ulises" , "Delfina" , "Lautaro" , "Frodo" , "Legolas" , "Aragorn"]

buscado = input("Ingrese el nombre del estudiante a buscar: ").strip()

while buscado == "" or not buscado.replace(" " , "").isalpha() :
    if buscado == "" :
        buscado = input("> El nombre no puede estar vacio. Ingrese el nombre del estudiante a buscar: ").strip()
    else :
        buscado = input("> El nombre solo puede contener letras. Ingrese el nombre del estudiante a buscar: ").strip()

estudiantes_lower = [nombre.lower() for nombre in estudiantes]

if buscado.lower() in estudiantes_lower :
    print("> El estudiante buscado se encuntra en la lista !")

    for index , nombre in enumerate(estudiantes) :
        if buscado.lower() == nombre.lower() :
            print(f">> El estudiante {buscado} se encuentra en la posicion {index + 1}")
else:
    print("> El estudiante no se encuentra en la lista")
    
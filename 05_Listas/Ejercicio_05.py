estudiantes = ["Martin" , "Joaquin" , "Agustina", "Ludmila" , "Carlos", "Esteban" , "Solange", "Matias"]

print("Que acción desea realizar? \n 1) Agregar nuevo Estudiante \n 2) Eliminar alumno existente")

opcion = input("Ingrese la opcion: ")

while not (opcion.isdigit() and 1 <= int(opcion) <= 2):
    print("La opcion ingresada no es valida, por favor ingrese una opcion valida")
    opcion = input("Ingrese la opcion: ")

opcion = int(opcion)

if opcion == 1 :
    nombre = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nombre)
    print("\n ---ESTUDIANTE NUEVO AGREGADO A LA LISTA--- \n")
elif opcion == 2 :
    nombre = input("Ingrese el nombre del estudiante que desea eliminar de la lista: ")
    if nombre in estudiantes : 
        estudiantes.remove(nombre)
        print("\n ---ESTUDIANTE ELIMINADO CON EXITO--- \n")
    else :
        print("---ESTUDIANTE NO ENCONTRADOO---")
        print("El nombre ingresado no se encuentra en la lista de estudiantes.")

print(f"La lista de estudiantes actualizada quedo conformada de la siguiente manera:\n{estudiantes}")


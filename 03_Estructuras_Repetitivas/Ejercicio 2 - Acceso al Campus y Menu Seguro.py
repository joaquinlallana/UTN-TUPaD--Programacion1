usuario = "alumno"
clave = "python123"
intentos = 1

while intentos <= 3:
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    clave_usuario = input("Ingrese su clave: ")

    if nombre_usuario == usuario and clave_usuario == clave:
        print("¡Bienvenido al campus virtual!")
        salir = True

        while salir:
            print(" 1) Estado de inscripción \n 2) Cambiar clave \n 3) Mostrar mensaje motivacional \n 4) Salir")
            opcion = input("Seleccione una opcion: ")

            if opcion.isdigit() and 1 <= int(opcion) <= 4:
                opcion =int(opcion)

                match opcion:
                    case 1:
                        print("Estado de inscripción: Inscrito")

                    case 2:
                        nueva_clave = input("Ingrese su nueva clave: ")
                        while len(nueva_clave) < 6:
                            print("La clave debe tener al menos 6 caracteres.")
                            nueva_clave = input("Ingrese su nueva clave: ")
                        confirmacion = input("Confirme su nueva clave: ")
                        while confirmacion != nueva_clave:
                            print("Las claves no coinciden. Intente nuevamente.")
                            confirmacion = input("Confirme su nueva clave: ")
                        clave = nueva_clave
                        print("Clave cambiada exitosamente.")

                    case 3:
                        print("Esforzate que los resultados llegarán")

                    case 4:
                        print("Saliendo del menú seguro...")
                        salir = False
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

        break  # login correcto y menú cerrado -> cortar el while de intentos

    else:
        print("Nombre de usuario o clave incorrectos. Intente nuevamente.")
        intentos += 1

if intentos > 3:
    print("Ha excedido el número máximo de intentos. Cuenta bloqueada")

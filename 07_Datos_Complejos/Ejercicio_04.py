#Ejercicio 4: Agenda de contactos
agenda = {}

def pedir_telefono(nombre):
    while True:
        telefono = input(f"Ingrese el teléfono de {nombre}: ").strip()
        if telefono == "" or telefono.isdigit() == False:
            print("Por favor, ingrese un teléfono válido (solo números).")
        elif len(telefono) > 15:
            print("El teléfono no puede tener más de 15 caracteres. Por favor, ingrese un teléfono válido.")
        else:
            # Se guarda como texto para no perder los 0 iniciales
            return telefono

while len(agenda) < 5:
    nombre = input("Ingrese el nombre del contacto: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío. Por favor, ingrese un nombre válido.")
        continue
    elif nombre in agenda:
        print("El contacto ya existe. Por favor, ingrese un nombre diferente.")
        continue
    elif nombre.replace(" ", "").isalpha() == False:
        print("El nombre solo puede contener letras. Por favor, ingrese un nombre válido.")
        continue
    elif len(nombre) > 20:
        print("El nombre no puede tener más de 20 caracteres. Por favor, ingrese un nombre válido.")
        continue

    agenda[nombre] = pedir_telefono(nombre)

print("--------------------------------")
print("Agenda completa.")

contacto = input("Ingrese el nombre del contacto que desea buscar: ").strip()
while contacto == "":
    print("El nombre no puede estar vacío. Por favor, ingrese un nombre válido.")
    contacto = input("Ingrese el nombre del contacto que desea buscar: ").strip()

if contacto in agenda:
    print(f"El número de teléfono de {contacto} es: {agenda[contacto]}")
else:
    print(f"El contacto {contacto} no se encuentra en la agenda.")

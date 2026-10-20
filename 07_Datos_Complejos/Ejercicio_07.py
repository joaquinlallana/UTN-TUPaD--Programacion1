#Ejercicio 7: Asistencia a una capacitación
asistencias = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "Ana"]
registro_asistencias = {}

print("Registro de asistencias original:")
for nombre in asistencias:
    print(nombre)

print("\nRegistro de asistencias sin duplicados:")
asistencias_sin_duplicados = set(asistencias)
for nombre in asistencias_sin_duplicados:
    print(nombre)

print("\nRegistro de asistencias con conteo:")
for nombre in asistencias:
    registro_asistencias[nombre] = registro_asistencias.get(nombre, 0) + 1

for nombre, conteo in registro_asistencias.items():
    print(f"{nombre}: {conteo}")

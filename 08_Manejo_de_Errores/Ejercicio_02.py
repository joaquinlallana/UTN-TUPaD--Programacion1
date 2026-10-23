#Ejercicio 2: Corregir sin excepciones
a = 10
b = input("Introduce un número: ").strip()
#Corrección 1: se valida que 'b' sea un número entero mayor a 0 antes de usarlo (evita también dividir por cero).
while not b.isdigit() or int(b) == 0:
    print("Valor inválido. Ingrese un número entero mayor a 0.")
    b = input("Introduce un número: ").strip()
#Corrección 2: se convierte 'b' de string a int para que se pueda dividir (soluciona el TypeError).
b = int(b)

result = a / b
print(f"Resultado: {result}")

numbers = [1, 2, 3]
indice = 5
#Corrección 3: se verifica que el índice exista en la lista antes de acceder (soluciona el IndexError).
if indice < len(numbers):
    print(numbers[indice])
else:
    print(f"El índice {indice} no existe. La lista tiene {len(numbers)} elementos.")

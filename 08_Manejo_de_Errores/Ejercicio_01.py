#Ejercicio 1: Identificar los errores
a = 10
b = input("Introduce un número: ") # input() siempre devuelve un string, aunque se escriba un número.
result = a / b # Error: TypeError. 'a' es un int y 'b' es un string, no se puede dividir un número por un texto.
print(f"Resultado: {result}") # No llega a ejecutarse porque el programa se frena en la línea anterior.

numbers = [1, 2, 3]
print(numbers[5]) # Error: IndexError. La lista tiene 3 elementos (índices 0, 1 y 2), el índice 5 no existe.

# UTN TUPaD — Programación I

Acá guardo los ejercicios que voy resolviendo en **Programación I** (Tecnicatura Universitaria en Programación a Distancia, UTN — 2026).

Cada carpeta es una unidad de la materia. Adentro están los ejercicios de esa unidad, escritos en **Python**.

## 🗂️ Resumen rápido

| Carpeta | ¿De qué trata? |
|---|---|
| `01_Estructuras_Secuenciales` | Pedir datos, hacer cuentas y mostrar resultados |
| `02_Estructuras_Condicionales` | Tomar decisiones con `if` / `elif` / `else` |
| `03_Estructuras_Repetitivas` | Repetir pasos con `while` y `for` |
| `05_Listas` | Guardar varios datos juntos en listas y tablas |
| `06_Funciones` | Armar bloques de código reutilizables |
| `07_Datos_Complejos` | Diccionarios, conjuntos (`set`) y tuplas |
| `08_Manejo_de_Errores` | Atrapar errores con `try` / `except` / `else` / `finally` |
| `Trabajo_Practico_Integrador` | Sistema de control de inventario para una ferretería (TPI) |

## 📂 Ejercicios por unidad

### 01 — Estructuras Secuenciales
El programa corre de arriba hacia abajo, paso por paso: pide datos, calcula y muestra.

- `Trabajo Practico_Esctructuras_Secuenciales.py` — trabajo práctico de la unidad.

### 02 — Estructuras Condicionales
El programa elige qué hacer según se cumpla o no una condición.

- `Trabajo Practico_Estructuras_Condicionales.py` — trabajo práctico de la unidad.

### 03 — Estructuras Repetitivas
El programa repite pasos hasta que se cumple algo (por ejemplo, hasta que el usuario elige "salir").

| Ejercicio | Qué hace |
|---|---|
| 1 — Caja del Kiosco | Suma las ventas hasta cerrar la caja |
| 2 — Acceso al Campus y Menú Seguro | Pide usuario y clave con intentos, y muestra un menú |
| 3 — Agenda de Turnos con nombres | Carga turnos uno por uno |
| 4 — La Bóveda | Juego de escape: abrir cerraduras antes de quedarse sin tiempo |
| 5 — La Arena del Gladiador | Juego de pelea por turnos |

### 05 — Listas
Una lista guarda varios datos en una sola variable. Una lista de listas funciona como una tabla (filas y columnas).

| Ejercicio | Qué hace |
|---|---|
| 01 | Calcula suma, promedio, nota más alta y más baja |
| 02 | Carga productos y los ordena alfabéticamente |
| 03 | Genera números al azar y los separa en pares e impares |
| 04 | Quita los elementos repetidos |
| 05 | Menú para agregar y quitar estudiantes |
| 06 | Mueve el último elemento al principio |
| 07 | Tabla del clima: máximas, mínimas y diferencia por día |
| 08 | Tabla de notas: promedio por alumno y por materia |
| 09 | Juego del Ta-Te-Ti |
| 10 | Ventas: total por día y por producto |
| 11 | Busca un estudiante en la lista |
| 12 | Carga 8 números enteros (acepta negativos) |
| 13 | Ranking de puntajes de mayor a menor |

### 06 — Funciones
Una función es un bloque de código con nombre que se puede usar muchas veces. Puede recibir datos (parámetros) y devolver un resultado (`return`).

| Ejercicio | Qué hace |
|---|---|
| 01 | Muestra "Hola Mundo!" |
| 02 | Saluda a una persona por su nombre |
| 03 | Muestra datos personales |
| 04 | Área y perímetro de un círculo |
| 05 | Pasa segundos a horas |
| 06 | Tabla de multiplicar |
| 07 | Suma, resta, multiplicación y división a la vez |
| 08 | Calcula el IMC |
| 09 | Pasa grados Celsius a Fahrenheit |
| 10 | Promedio de tres números |

### 07 — Datos Complejos
Nuevas formas de guardar datos:

- **Diccionario:** guarda pares `clave: valor`, como una agenda (nombre → teléfono).
- **Conjunto (`set`):** guarda datos sin repetidos.
- **Tupla:** como una lista, pero no se puede modificar.

| Ejercicio | Qué hace |
|---|---|
| 01 | Crea un diccionario de precios de frutas y le agrega más |
| 02 | Actualiza algunos precios |
| 03 | Saca la lista de nombres de frutas |
| 04 | Agenda de 5 contactos y búsqueda por nombre |
| 05 | Muestra las palabras de una frase sin repetir y cuántas veces aparece cada una |
| 06 | Guarda notas de alumnos y calcula sus promedios |
| 07 | Lista de asistencia: quita repetidos y cuenta cuántas veces vino cada uno |
| 08 | Menú para consultar y cargar stock de productos |
| 09 | Agenda por día y hora (usa tuplas como clave) |
| 10 | Da vuelta un diccionario: país → capital pasa a capital → país |

### 08 — Manejo de Errores
Cuando algo sale mal (por ejemplo, dividir por un texto o pedir un elemento que no existe), Python lanza un **error**. Con `try` / `except` el programa lo atrapa y sigue funcionando en vez de cortarse. `else` corre si no hubo error y `finally` corre siempre.

| Ejercicio | Qué hace |
|---|---|
| 01 | Marca con comentarios los errores de un código y explica por qué ocurren |
| 02 | Corrige esos errores validando los datos, sin usar excepciones |
| 03 | Atrapa los errores con `try` / `except` |
| 04 | Usa un `except` distinto para cada tipo de error |
| 05 | Suma los bloques `else` y `finally` |
| 06 | Pide un número y avisa si lo ingresado no es válido |
| 07 | Igual que el 06, pero deja volver a intentar hasta ingresar un número válido |

### 🧰 Trabajo Práctico Integrador — Sistema de Control de Inventario
Programa de consola que controla el inventario de una ferretería con un menú interactivo. Junta todo lo visto en la materia: listas de diccionarios, funciones repartidas en varios archivos (paquetes), validaciones y manejo de errores con `try` / `except` y `raise`.

| Opción del menú | Qué hace |
|---|---|
| 1 | Carga varias herramientas con su stock inicial |
| 2 | Muestra todo el inventario |
| 3 | Consulta el stock de una herramienta |
| 4 | Lista las herramientas agotadas |
| 5 | Da de alta un producto nuevo |
| 6 | Registra una venta o un ingreso de stock |
| 7 | Sale del programa |

- `sistema_de_inventario/` — código del programa (se ejecuta desde `main.py`). Tiene su propio [README](Trabajo_Practico_Integrador/sistema_de_inventario/README.md) con la estructura y el detalle de cada función.
- `TPI Informe - Programacion 1.pdf` — informe escrito del trabajo.

> Voy a ir sumando nuevas carpetas a medida que avance la cursada.

## ▶️ Cómo correr un ejercicio

Solo hace falta tener **Python 3** instalado. No hay que instalar nada más.

Desde la carpeta principal del repositorio, escribí en la terminal:

```bash
python3 "07_Datos_Complejos/Ejercicio_01.py"
```

Cambiá la ruta por la del ejercicio que quieras probar. Muchos ejercicios te van a pedir que escribas datos.

Para el Trabajo Práctico Integrador hay que entrar a su carpeta, porque `main.py` importa los demás archivos:

```bash
cd Trabajo_Practico_Integrador/sistema_de_inventario
python3 main.py
```

## 👤 Autor

Joaquín Lallana — estudiante de la Tecnicatura Universitaria en Programación (UTN, a distancia)

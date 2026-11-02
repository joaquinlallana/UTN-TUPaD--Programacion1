# Sistema de Control de Inventario

Trabajo Práctico Integrador de **Programación I**, Tecnicatura Universitaria en Programación a Distancia (UTN).

Alumno: **Joaquín Dalmiro Lallana**

Programa de consola, escrito en Python, que controla el inventario de una ferretería mediante un menú interactivo. Permite cargar herramientas con su stock inicial, listarlas, consultar el stock de una herramienta, ver las agotadas, dar de alta productos y registrar ventas e ingresos. Los datos viven en memoria mientras el programa está en ejecución y no se guardan al cerrarlo.

---

## Requisitos

- Python 3 (desarrollado y probado con **Python 3.12.3**).
- No usa librerías externas: solo funciones propias repartidas en varios archivos.

## Cómo ejecutarlo

Desde una terminal, dentro de esta carpeta:

```bash
cd sistema_de_inventario
python3 main.py
```

`main.py` es el único archivo que se ejecuta. Los demás contienen las funciones que `main.py` importa.

---

## Estructura del proyecto

```
sistema_de_inventario/
├── README.md                  ← este archivo
├── main.py                    ← punto de entrada: main() con el menú
├── interfaz/
│   └── menu.py                ← mostrar_menu() y pedir_opcion()
├── operaciones/
│   ├── carga.py               ← opciones 1 y 5 (agregan herramientas)
│   ├── consultas.py           ← opciones 2, 3 y 4 (solo leen el inventario)
│   └── movimientos.py         ← opción 6 (modifica el stock)
└── auxiliares/
    ├── validaciones.py        ← validación de números y nombres
    └── busqueda.py            ← búsqueda de una herramienta por nombre
```

Cada carpeta agrupa archivos relacionados y funciona como un **paquete** de Python (desde Python 3.3 no hace falta un archivo `__init__.py` para importarlas). Las funciones se comparten entre archivos con `from paquete.modulo import funcion`, por ejemplo:

```python
from auxiliares.validaciones import pedir_entero, validar_nombre_nuevo
```

### Funciones de cada archivo

| Archivo | Función | Qué hace |
|---|---|---|
| `main.py` | `main()` | Crea `inventario`, repite el menú en un bucle, llama a la función de cada opción y captura los `ValueError` que llegan desde las opciones. |
| `interfaz/menu.py` | `mostrar_menu()` | Imprime las 7 opciones del menú. |
| | `pedir_opcion()` | Lee la opción elegida. Si no es un número entero, relanza el error con un mensaje en español. |
| `operaciones/carga.py` | `cargar_herramientas(inventario)` | Opción 1. Carga varias herramientas y vuelve a pedir cada dato inválido dentro de la función. |
| | `alta_producto(inventario)` | Opción 5. Agrega una herramienta; si un dato es inválido, el error sale hacia `main()`. |
| `operaciones/consultas.py` | `mostrar_inventario(inventario)` | Opción 2. Lista todas las herramientas con su stock. |
| | `consultar_stock(inventario)` | Opción 3. Busca una herramienta por nombre y muestra su stock. |
| | `reporte_agotados(inventario)` | Opción 4. Muestra solo las herramientas con stock cero. |
| `operaciones/movimientos.py` | `actualizar_stock(inventario)` | Opción 6. Registra una venta o un ingreso. |
| `auxiliares/validaciones.py` | `pedir_entero(mensaje, minimo)` | Pide un número entero. Lanza `ValueError` con un mensaje en español si no es un entero o si es menor que el mínimo. |
| | `validar_nombre(nombre)` | Rechaza un nombre vacío o con solo espacios y lo devuelve sin espacios en los extremos. |
| | `validar_nombre_nuevo(inventario, nombre)` | Además de validar el nombre, rechaza una herramienta que ya está cargada. |
| `auxiliares/busqueda.py` | `buscar_herramienta(inventario, nombre)` | Devuelve la herramienta encontrada (sin distinguir mayúsculas ni espacios extremos) o `None`. |

---

## Estructura de datos

Todo el inventario se guarda en una única **lista de diccionarios** llamada `inventario`. Cada diccionario es una herramienta con dos claves:

```python
[{'herramienta': 'Martillo', 'cantidad': 10}, {'herramienta': 'Pala', 'cantidad': 3}]
```

- `'herramienta'`: el nombre, guardado sin espacios en los extremos y con las mayúsculas que escribió el usuario.
- `'cantidad'`: el stock (unidades disponibles), un número entero.

`inventario` se crea dentro de `main()` y se pasa por parámetro a cada función. No hay variables globales.

---

## Opciones del menú

El menú se vuelve a mostrar después de cada operación. Solo la opción 7 termina el programa.

| Opción | Qué hace |
|---|---|
| **1. Carga de herramientas** | Pregunta cuántas herramientas distintas se van a cargar y, por cada una, pide nombre y stock inicial. Si un dato es inválido, vuelve a pedir solo ese dato. Una herramienta se agrega recién cuando su nombre y su stock son válidos. |
| **2. Visualización del inventario** | Lista todas las herramientas con su stock. |
| **3. Consulta de stock** | Pide un nombre y muestra el stock de esa herramienta, o avisa que no está en el inventario. |
| **4. Reporte de agotados** | Muestra las herramientas con stock cero, o avisa que todas tienen stock. |
| **5. Alta de nuevo producto** | Pide el nombre y, solo si es válido, el stock inicial. Si algo falla, no agrega nada y vuelve al menú. |
| **6. Actualización de stock** | Pide la herramienta, el tipo de movimiento (`1` venta, `2` ingreso) y las unidades. Una venta no puede dejar el stock en negativo. El stock se modifica recién después de validar todo. |
| **7. Salir** | Termina el programa. |

Las opciones 2, 3, 4 y 6 avisan si todavía no hay herramientas cargadas, sin pedir ningún dato.

---

## Validaciones y manejo de errores

El programa usa una sola excepción, `ValueError`, que ya viene con Python.

- **`try/except`**: captura las entradas que no se pueden convertir a entero (por ejemplo `abc` o `3.5`). `int()` lanza `ValueError` en esos casos. Como el mensaje de ese error viene en inglés, `pedir_opcion()` (menú) y `pedir_entero()` (cantidad, stock y unidades) lo capturan y lo vuelven a lanzar con `raise` y un mensaje en español. Así todos los errores que ve el usuario están en español.
- **`raise ValueError(...)`**: lanza un error con un mensaje claro cuando un dato rompe una regla del negocio:
  - nombre vacío, solo espacios o duplicado;
  - stock inicial negativo (el 0 es válido);
  - cantidad de herramientas a cargar o unidades menores que 1;
  - venta mayor que el stock disponible;
  - opción del menú fuera del rango 1 a 7.
- **Condición y mensaje, sin excepción**: inventario vacío, herramienta inexistente y tipo de movimiento inválido.

Dónde se captura cada error:

- **Opción 1**: el error se captura dentro de `cargar_herramientas`, y la función vuelve a pedir el dato que falló. Si falla el stock, se conserva el nombre.
- **Opciones 3, 5 y 6**: las funciones no capturan el error. El `ValueError` sube hasta el `except` de `main()`, que muestra el motivo y vuelve al menú sin haber modificado nada.

Los nombres se comparan sin distinguir mayúsculas ni espacios en los extremos: `Martillo`, `martillo` y `  MARTILLO  ` son la misma herramienta.

---

## Ejemplo de uso

```
Opciones:
1. Carga de herramientas con existencias iniciales
...
7. Salir
Seleccione una opción: 1
Ingrese la cantidad de herramientas distintas a cargar: 2
Ingrese el nombre de la herramienta 1: Martillo
Ingrese el stock inicial de Martillo: 10
Ingrese el nombre de la herramienta 2: Pala
Ingrese el stock inicial de Pala: 0

Seleccione una opción: 4
Las herramientas que se encuentran sin stock son:
>  Pala
```

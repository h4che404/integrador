# Integrador TPI – Gestión de Países

Trabajo integrador de Programación 1 que implementa un sistema de **gestión y análisis de países** utilizando un archivo CSV como fuente de datos.

El programa permite:

- Cargar un dataset de países desde `paises_base.csv`.
- Buscar países por nombre.
- Filtrar por continente, población o superficie.
- Ordenar los países por diferentes campos.
- Calcular estadísticas básicas (mayor/menor población, promedios).
- Guardar los resultados en un nuevo archivo CSV.

---

## Estructura del proyecto

- `integrador_tpi1.py`  
  Script principal en Python. Contiene:
  - Funciones de validación y normalización de datos.
  - Manejo del archivo CSV (lectura y escritura).
  - Lógica principal del menú de opciones.
- `paises_base.csv`  
  Dataset base de países con el siguiente formato de columnas:

  | Columna     | Tipo      | Descripción                                      |
  |------------|-----------|--------------------------------------------------|
  | `nombre`   | texto     | Nombre del país                                  |
  | `poblacion`| entero    | Cantidad de habitantes                           |
  | `superficie`| entero   | Superficie en km²                                |
  | `continente`| texto    | Continente al que pertenece el país              |

  > El archivo incluido en este trabajo contiene 64 países de distintos continentes.

---

## Requisitos

- **Python 3.x** instalado.
- Archivo `paises_base.csv` en el **mismo directorio** que `integrador_tpi1.py`.

---

## Instrucciones de uso

1. **Ubicar los archivos**

   Colocar en la misma carpeta:

   - `integrador_tpi1.py`
   - `paises_base.csv`

2. **Ejecutar el programa**

   Desde la terminal, ubicándose en la carpeta del proyecto:

   ```bash
   python integrador_tpi1.py

3. **📋 Opciones del Menú**

  Al ejecutar el programa, se presentará el siguiente menú:

  ```bash
  MENU DE OPCIONES
  1. Cargar datos de países
  2. Filtrar datos
  3. Ordenar datos
  4. Calcular estadísticas
  5. Mostrar todos los países
  6. Guardar datos filtrados/ordenados
  . Salir


**👥 Participación de los integrantes**

## Completar con los datos reales del grupo.
## Si el trabajo es individual, dejar solo un integrante.

- **[Juan Cruz Elias Martin]** 
- **[Joaquin Mendez Reynoso]**
import csv

# Datos que queremos guardar
datos_ejemplo = [
    ['Nombre', 'Edad', 'Ciudad'],  # Encabezado (header)
    ['Ana', 30, 'Madrid'],
    ['Carlos', 25, 'Barcelona'],
    ['Eva', 45, 'Sevilla']
]

# Abrir el archivo en modo escritura ('w')
# Se usa 'newline=' para evitar filas en blanco entre los datos.
nombre_archivo = 'ejemplo.csv'
try:
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
        # 1. Crear el objeto escritor (writer)
        escritor = csv.writer(archivo_csv)

        # 2. Escribir todas las filas a la vez
        escritor.writerows(datos_ejemplo)

    print(f"El archivo '{nombre_archivo}' ha sido creado y guardado con éxito.")
except Exception as e:
    print(f"Ocurrió un error al escribir el archivo: {e}")
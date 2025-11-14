"""
Integrador TPI - Gestión de Países
"""

import csv
import os

CSV_FILE_DEFAULT = "paises_base.csv"
CSV_HEADERS = ["nombre", "poblacion", "superficie", "continente"]

# =========================
# BLOQUE 1: VALIDACIONES / UTILIDADES
# =========================

# Normalización de texto y parsing de enteros flexible
def normalizar_texto(texto):
    """Devuelve el texto sin espacios extras y en minúsculas."""
    if texto is None:
        return ""
    # Mapa de acentos a caracteres sin acento
    mapa_acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'ñ': 'n', 'Ñ': 'N', 'ü': 'u', 'Ü': 'U'   
    }
    for acentuada, sin_acentuar in mapa_acentos.items():
        texto = texto.replace(acentuada, sin_acentuar)
        
    return str(texto).strip().lower()

# Revisión y parsing de enteros flexibles    
def parse_int_flexible(valor):
    #Convierte el valor en entero.
    #Elimina separadores (., ) y devuelve 0 si no es válido.
    if valor is None:
        return 0
    s = str(valor).strip()
    # Manejo de cadena vacía
    if s == "":
        return 0
    # Eliminación de separadores comunes y verificación de dígitos
    s = s.replace(" ", "").replace(",", "").replace(".", "")
    if s.lstrip("-").isdigit():
        return int(s)
    return 0

# Entradas validadas de usuario solamente letras y opciones
def input_str_solo_letras(mensaje):
    while True:
        entrada = input(mensaje).strip()
        entrada = normalizar_texto(entrada).strip()
        if not entrada:
            print("Error: La entrada no puede estar vacía. Inténtelo de nuevo.")
            continue
        if entrada.isalpha():
            return entrada
        print("Error: Ingrese solo letras (caracteres alfabéticos).")

# Entrada validada de usuario para enteros
def input_int(mensaje, permitir_vacio=False, valor_defecto=None):
    """Pide un número entero y valida"""
    while True:
        entrada = input(mensaje).strip()
        if entrada == "" and permitir_vacio:
            return valor_defecto
        entrada_limpia = entrada.replace(" ", "").replace(",", "").replace(".", "")
        if entrada_limpia.lstrip("-").isdigit():
            return parse_int_flexible(entrada_limpia)
        print("Error: ingrese un número entero válido.")

# Entrada validada de usuario para opciones de texto
def input_opcion(mensaje, opciones, permitir_vacio=False):
    """Pide una opción de texto válida."""
    opciones_normalizadas = {
        normalizar_texto(opcion): opcion 
        for opcion in opciones
    }
    # Bucle para verificar opción válida y coincidencia parcial
    while True:
        entrada = input_str_solo_letras(mensaje).strip()
        if entrada == "" and permitir_vacio:
            return None
        coincidencia_encontrada = None
        for normalizado_opcion, original_opcion in opciones_normalizadas.items():
            if normalizado_opcion.startswith(entrada):
                coincidencia_encontrada = original_opcion
                break 
        if coincidencia_encontrada:
            return coincidencia_encontrada
        else:
            print("Opción inválida o ambigua.")
            print(f"Opciones válidas (acepta coincidencia parcial): {', '.join(opciones)}")
        


# =========================
# BLOQUE 2: PERSISTENCIA (CSV)
# =========================

# Verificación de existencia de archivo
def archivo_existe(ruta):
    """Devuelve True si el archivo existe y es accesible."""
    return os.path.isfile(ruta)

# Creación de CSV de ejemplo por si no existe
def crear_csv_ejemplo(ruta):
    """Crea un CSV de ejemplo si no existe."""
    # Datos de ejemplo 
    muestra = [
        {"nombre": "Argentina", "poblacion": "45376763", "superficie": "2780400", "continente": "América"},
        {"nombre": "Japón", "poblacion": "125800000", "superficie": "377975", "continente": "Asia"},
        {"nombre": "Brasil", "poblacion": "213993437", "superficie": "8515767", "continente": "América"},
        {"nombre": "Alemania", "poblacion": "83149300", "superficie": "357022", "continente": "Europa"},
        {"nombre": "Australia", "poblacion": "25687041", "superficie": "7692024", "continente": "Oceanía"}
    ]
    # Guardar CSV de ejemplo
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
        writer.writeheader()
        for fila in muestra:
            writer.writerow(fila)

# Carga y validación de CSV existente
def cargar_csv(ruta):
    """Carga un CSV y valida que tenga las columnas requeridas."""
    paises = []
    # Verificar existencia del archivo 
    if not archivo_existe(ruta):
        print(f"Archivo no encontrado: {ruta}")
        return paises
    with open(ruta, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        encabezados = [h.strip().lower() for h in reader.fieldnames or []]
        for requerido in CSV_HEADERS:
            if requerido not in encabezados:
                print(f"Falta la columna '{requerido}' en el CSV.")
                return []
        # Lectura y validación de filas
        for fila in reader:
            nombre = (fila.get("nombre") or "").strip()
            pobl = parse_int_flexible(fila.get("poblacion"))
            sup = parse_int_flexible(fila.get("superficie"))
            cont = (fila.get("continente") or "Desconocido").strip()
            if nombre != "":
                paises.append({
                    "nombre": nombre,
                    "poblacion": pobl,
                    "superficie": sup,
                    "continente": cont
                })
    return paises

# Guardado de CSV modificado 
def guardar_csv(ruta, paises):
    """Guarda la lista de países en un CSV nuevo."""
    # Validar que haya datos para guardar 
    if not paises:
        print("No hay datos para guardar.")
        return
    # Guardar en CSV
    with open(ruta, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
        writer.writeheader()
        for p in paises:
            writer.writerow(p)
    print(f"Archivo guardado correctamente en {ruta}")

# =========================
# BLOQUE 3: FUNCIONALIDAD PRINCIPAL
# =========================

# Búsqueda, filtrado, ordenamiento y estadísticas de países
# Búsqueda por nombre (parcial, case insensitive)
def buscar_por_nombre(paises, termino):
    return [p for p in paises if normalizar_texto(termino) in normalizar_texto(p["nombre"])]
# Filtro por continente para lista de países 
def filtrar_por_continente(paises, continente):
    return [p for p in paises if normalizar_texto(continente) in normalizar_texto(p["continente"] )]

# Filtro por rango numérico (población o superficie) 
def filtrar_por_rango(paises, campo, minimo, maximo):
    resultado = []
    # Asegurar que el campo es válido 
    for p in paises:
        valor = p.get(campo, 0)
        if minimo is not None and valor < minimo:
            continue
        if maximo is not None and valor > maximo:
            continue
        resultado.append(p)
    return resultado

# Ordenamiento por campo (nombre, población o superficie) 
def ordenar_paises(paises, campo, descendente=False):
    if campo == "nombre":
        return sorted(paises, key=lambda x: normalizar_texto(x["nombre"]), reverse=descendente)
    return sorted(paises, key=lambda x: x.get(campo, 0), reverse=descendente)

# Cálculo de estadísticas básicas de población y superficie 
def estadisticas(paises):
    if not paises:
        return None
    # Listas auxiliares para cálculos
    pops = [p["poblacion"] for p in paises]
    sups = [p["superficie"] for p in paises]
    # Validar que haya datos numéricos 
    if not pops or not sups:
        return None
    return {
        "mayor": max(paises, key=lambda x: x["poblacion"]),
        "menor": min(paises, key=lambda x: x["poblacion"]),
        "prom_pobl": sum(pops) / len(pops),
        "prom_sup": sum(sups) / len(sups)
    }

# Mostrar lista de países en formato tabular 
def mostrar_paises(paises, maximo=None):
    if not paises:
        print("------------------------------------------")
        print("No hay países para mostrar con ese nombre.")
        return
    print("-"*65)
    print(f"{'Nombre':<20} | {'Población':>12} | {'Superficie':>10} | {'Continente':<12}")
    print("-"*65)
    for i, p in enumerate(paises):
        if maximo and i >= maximo:
            print(f"... y {len(paises)-maximo} más.")
            break
        print(f"{p['nombre']:<20} | {p['poblacion']:>12} | {p['superficie']:>10} | {p['continente']:<12}")

# =========================
# BLOQUE 4: MENÚ PRINCIPAL
# =========================

# Menú principal y flujo de la aplicación 
def mostrar_menu():
    print("""
=== MENÚ PRINCIPAL ===
1) Buscar país
2) Filtrar países
3) Ordenar países
4) Mostrar estadísticas
5) Mostrar todos
0) Salir
======================
""")

def main():
    print("Integrador TPI")
    if not archivo_existe(CSV_FILE_DEFAULT):
        print("No se encontró el archivo base, se creará uno de ejemplo.")
        crear_csv_ejemplo(CSV_FILE_DEFAULT)
    paises = cargar_csv(CSV_FILE_DEFAULT)
    print(f"\n{len(paises)} países cargados correctamente.\n")

    while True:
        mostrar_menu()
        op = input("Seleccione una opción: ").strip()
        if op == "0":
            print("Hasta luego.")
            break
        elif op == "1":
            term = input_str_solo_letras("\nIngrese nombre o parte del nombre: ").strip()
            print("\n")
            mostrar_paises(buscar_por_nombre(paises, term))
        elif op == "2":
            print("\n")
            tipo = input_opcion("Filtrar por (a) continente, (b) población, (c) superficie: ", ["a","b","c"])
            if tipo == "a":
                cont = input_str_solo_letras("\nIngrese el continente: ").strip()
                print("\n")
                mostrar_paises(filtrar_por_continente(paises, cont))
            elif tipo == "b":
                while True:
                    minv = input_int("\nPoblación mínima (ENTER = sin límite): ", True)
                    maxv = input_int("\nPoblación máxima (ENTER = sin límite): ", True)
                    if minv is not None and maxv is not None and minv > maxv:
                        print("\nError: la población mínima no puede ser mayor que la máxima.")
                    elif minv <= 0 or maxv <= 0:
                        print("\nError: los valores deben ser positivos.")
                    else:
                        mostrar_paises(filtrar_por_rango(paises, "poblacion", minv, maxv))
                        break
            elif tipo == "c":
                minv = input_int("Superficie mínima (ENTER = sin límite): ", True)
                maxv = input_int("Superficie máxima (ENTER = sin límite): ", True)
                mostrar_paises(filtrar_por_rango(paises, "superficie", minv, maxv))
        elif op == "3":
            campo = input_opcion("Ordenar por (nombre/poblacion/superficie): ", ["nombre","poblacion","superficie"])
            sentido = input_opcion("Sentido (asc/desc): ", ["asc","desc"])
            mostrar_paises(ordenar_paises(paises, campo, sentido == "desc"))
        elif op == "4":
            est = estadisticas(paises)
            if est is None:
                print("No hay datos suficientes para estadísticas.")
            else:
                print(f"Mayor población: {est['mayor']['nombre']} ({est['mayor']['poblacion']})")
                print(f"Menor población: {est['menor']['nombre']} ({est['menor']['poblacion']})")
                print(f"Promedio de población: {round(est['prom_pobl'],2)}")
                print(f"Promedio de superficie: {round(est['prom_sup'],2)} km²")
        elif op == "5":
            mostrar_paises(paises, 50)
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()

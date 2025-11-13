def normalizar_texto_manual(texto):
    """Convierte el texto a minúsculas y elimina tildes/acentos (manual)."""
    # Asegura que sea string y lo convierte a minúsculas
    texto = str(texto).lower()
    
    # Mapeo manual de acentos
    mapa_acentos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'ñ': 'n', 'ü': 'u'
    }
    
    for acentuada, sin_acentuar in mapa_acentos.items():
        texto = texto.replace(acentuada, sin_acentuar)
        
    return texto

def seleccionar_opcion_flexible_manual(opciones_disponibles):
    """
    Permite al usuario seleccionar una opción de la tupla ingresando 
    una coincidencia parcial (sin librerías).
    
    Args:
        opciones_disponibles (tuple/list): Las opciones válidas (ej: ["nombre", "poblacion"]).
        
    Returns:
        str | None: La opción completa seleccionada o None si no hay coincidencia.
    """
    # 1. Normalizar las opciones disponibles para la búsqueda
    opciones_normalizadas = {
        normalizar_texto_manual(opcion): opcion 
        for opcion in opciones_disponibles
    }
    
    while True:
        # 2. Mostrar opciones al usuario
        print("\n--- Opciones Disponibles ---")
        print(f"[{', '.join(opciones_disponibles)}]")
        
        # 3. Pedir la entrada
        entrada_usuario = input("Ingrese el inicio o la palabra clave de la opción: ").strip()
        
        if not entrada_usuario:
            print("❌ Error: La entrada no puede estar vacía.")
            continue
            
        # 4. Normalizar la entrada del usuario
        entrada_normalizada = normalizar_texto_manual(entrada_usuario)
        
        coincidencia_encontrada = None
        
        # 5. Búsqueda de Coincidencia (startswith)
        for normalizado_opcion, original_opcion in opciones_normalizadas.items():
            # Comprueba si la opción normalizada COMIENZA con la entrada normalizada del usuario
            if normalizado_opcion.startswith(entrada_normalizada):
                # Se encontró la coincidencia, guardar la versión original y salir del bucle for
                coincidencia_encontrada = original_opcion
                break 
                
        # 6. Devolver el resultado
        if coincidencia_encontrada:
            print(f"✅ Opción seleccionada: '{coincidencia_encontrada}'")
            return coincidencia_encontrada
        else:
            print(f"❌ Error: No se encontró ninguna opción que comience con '{entrada_usuario}'. Inténtelo de nuevo.")

## 💡 Ejemplo de Uso


opciones_tupla = ("nombre", "población", "Superficie", "Continente")

opcion_elegida = seleccionar_opcion_flexible_manual(opciones_tupla)

if opcion_elegida:
    print(f"\nFinalizado. El usuario eligió: {opcion_elegida}")
from companies import companies as contexto

def obtener_numero_codificacion(companies):
    return sum([contexto.index(compania) for compania in companies if compania in contexto])

def codificar(dpi, companies):
    numero_codificacion = obtener_numero_codificacion(companies)
    
    # Codificar el DPI usando XOR con el número de codificación
    dpi_codificado = int(dpi) ^ numero_codificacion
    
    # Añadir el número de codificación al final del DPI codificado para usarlo en la decodificación
    return int(str(dpi_codificado) + str(numero_codificacion).zfill(4))

def decodificar(dpi_codificado_con_info):
    # Extraer el número de codificación del final del DPI
    numero_codificacion = int(str(dpi_codificado_con_info)[-4:])
    
    # Extraer el DPI codificado sin la información añadida
    dpi_codificado = int(str(dpi_codificado_con_info)[:-4])
    
    # Decodificar usando XOR
    return dpi_codificado ^ numero_codificacion
from processing.services.procesador import *
from config.settings_manager import process_config

def run_processing():
    """
    Función orquestadora principal del procesamiento de datos de boyas.
    
    Args:
        ruta_a_carpeta: Ruta donde están los archivos CSV descargados
        fecha_inicial: Fecha inicial del rango (formato: "YYYY-MM-DD HH:MM:SS")
        fecha_final: Fecha final del rango (formato: "YYYY-MM-DD HH:MM:SS")
        ruta_guardado: Ruta donde guardar el archivo Excel de salida
        nombre_salida: Nombre del archivo de salida (sin extensión)
    
    Returns:
        DataFrame con los resultados del procesamiento
    """
    
    
    fecha_inicial = process_config.get_starting_date()
    fecha_final = process_config.get_ending_date()
    process_config.crear_carpeta_de_guardado()
    
    # Validar rutas de entrada y salida
    process_config.validar_rutas()
    ruta_de_datos_crudos = process_config.RUTA_DATOS_CRUDOS
    ruta_guardado = process_config.RUTA_GUARDADO
    
    # Buscar archivos CSV
    archivos = buscar_archivos_csv(ruta_de_datos_crudos)
    
    # Crear diccionario de boyas
    dic = crear_diccionario_de_boyas(archivos)
    
    # Llenar datos del diccionario
    dic = llenar_datos_de_diccionario_de_boyas(dic, ruta_de_datos_crudos, fecha_inicial, fecha_final)
    
    # Crear DataFrame de salida
    df_salida = crear_dataframe_de_salida(dic, fecha_inicial, fecha_final)
    
    # 5. Guardar csv de salida
    nombre_de_archivo_de_salida = process_config.crear_nombre_de_archivo_de_salida_excel()
    guardar_excel(df_salida, ruta_guardado, nombre_de_archivo_de_salida)
    
    print(f"OLEAJE ESPERADOS: {df_salida['oleaje_esperados'].sum()}")
    print(f"OLEAJE RECIBIDOS: {df_salida['oleaje_recibidos'].sum()}")
    return df_salida
    
    
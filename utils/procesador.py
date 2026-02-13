"""
Módulo de procesamiento de datos de boyas.
Contiene funciones para cargar, procesar y analizar datos de CSV de boyas.
"""
import os
import pandas as pd
import numpy as np


def crear_ruta_a_archivo(nombre_archivo, ruta_a_carpeta="data"):
    """Crea una ruta completa a un archivo dentro de una carpeta especificada."""
    return os.path.join(ruta_a_carpeta, nombre_archivo)

def cargar_csv(ruta_archivo):
    """Carga un archivo CSV y devuelve un DataFrame de pandas."""
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"El archivo {ruta_archivo} no existe.")
    return pd.read_csv(ruta_archivo)

def estandarizar_nombres_de_columnas(df):
    """Estandariza los nombres de las columnas de un DataFrame."""
    df.columns.values[0] = "fecha"
    return df

def guardar_csv(df, ruta_archivo):
    """Guarda un DataFrame de pandas en un archivo CSV."""
    if not os.path.exists(os.path.dirname(ruta_archivo)):
        os.makedirs(os.path.dirname(ruta_archivo))
    df.to_csv(ruta_archivo, index=False)
    
def buscar_archivos_csv(ruta_a_carpeta):
    """Busca y devuelve una lista de archivos CSV en la carpeta especificada."""
    if not os.path.exists(ruta_a_carpeta):
        raise FileNotFoundError(f"La carpeta {ruta_a_carpeta} no existe.")
    return [f for f in os.listdir(ruta_a_carpeta) if f.endswith('.csv')]

def arreglar_fechas_de_df(df):
    """Convierte la columna 'fecha' de un DataFrame a formato datetime."""
    # 2026-01-01T00:02:00.000z
    df['fecha'] = pd.to_datetime(df["fecha"])
    return df

def filtrar_fechas(df,fecha_inicial, fecha_final):
    """Filtra un DataFrame por un rango de fechas."""
    fecha_inicial = pd.to_datetime(fecha_inicial, format ="%Y-%m-%d %H:%M:%S").replace(second=0, microsecond=0)
    fecha_final = pd.to_datetime(fecha_final, format ="%Y-%m-%d %H:%M:%S").replace(second=0, microsecond=0)
        
    df['fecha'] = pd.to_datetime(df['fecha'])
    return df[(df['fecha'] >= fecha_inicial) & (df['fecha'] <= fecha_final)]

def obtener_nombre_de_boya(ruta_a_archivo):
    """Obtiene el nombre de la boya a partir del nombre del archivo."""
    nombre = ruta_a_archivo.split('_')
    return "".join(nombre[2:3])

def buscar_archivos_csv_de_una_boya(ruta_a_carpeta, nombre_de_boya):
    """Busca y devuelve una lista de archivos CSV de una boya específica en la carpeta."""
    archivos = buscar_archivos_csv(ruta_a_carpeta)
    archivos_boya = []
    for archivo in archivos:
        if nombre_de_boya in archivo:
            archivos_boya.append(archivo)
    return archivos_boya

def crear_diccionario_de_boyas(archivos: list[str]) -> dict:
    """Crea un diccionario de boyas a partir de una lista de archivos."""
    dic = {}
    for archivo in archivos:
        nombre_de_boya = obtener_nombre_de_boya(archivo)
        if nombre_de_boya not in dic:
            dic[nombre_de_boya] = {
                "viento": pd.DataFrame(),
                "oleaje": pd.DataFrame(),
                "corriente": pd.DataFrame(),
                "mct": pd.DataFrame(),
            }
    return dic


def llenar_datos_de_diccionario_de_boyas(dic: dict, ruta_a_carpeta: str, fecha_inicial: str, fecha_final: str):
    for nombre_de_boya in dic:
        archivos_de_boya = buscar_archivos_csv_de_una_boya(ruta_a_carpeta, nombre_de_boya)
        for archivo in archivos_de_boya:
            ruta_a_archivo = crear_ruta_a_archivo(archivo, ruta_a_carpeta)
            df = cargar_csv(ruta_a_archivo)
            df = estandarizar_nombres_de_columnas(df)
            df = arreglar_fechas_de_df(df)
            tipo = obtener_tipo_de_dato(archivo)
            df_filtrado = filtrar_fechas(df, fecha_inicial, fecha_final) 
            dic[nombre_de_boya][tipo] = df_filtrado
    return dic

def obtener_tipo_de_dato(archivo: str) -> str:
    """Obtiene el tipo de dato (viento, oleaje, corriente, mct) a partir del nombre del archivo."""
    if "Viento" in archivo:
        return "viento"
    elif "Oleaje" in archivo or "Ola" in archivo:
        return "oleaje"
    elif "Corriente" in archivo:
        return "corriente"
    elif "Salinidad" in archivo:
        return "mct"
    else:
        raise ValueError(f"No se pudo determinar el tipo de dato para el archivo {archivo}.")
    
    
def crear_dataframe_de_salida(dic: dict, fecha_inicial, fecha_final) -> pd.DataFrame:
    """Crea un DataFrame de salida a partir del diccionario de boyas."""
    tipos = ["viento","oleaje","corriente","mct"]
    df_salida = pd.DataFrame(columns=["boya"])
    for tipo in tipos:
        esperados = []
        recibidos = []
        for boya in dic.keys():
            if len(dic[boya][tipo]) == 0:
                esperados.append(0)
                recibidos.append(0)
                continue
            
            delta_t_min = (dic[boya][tipo]["fecha"].diff().dt.total_seconds() /60).min()
            cantidad_de_datos_esperados = len(pd.date_range(start=fecha_inicial, end=fecha_final, freq=f"{delta_t_min}min"))
            if tipo == "viento":
                var_name = dic[boya][tipo].columns[4]
            else:
                var_name = dic[boya][tipo].columns[1]
            
            dic[boya][tipo].dropna(subset=var_name, inplace=True)
            cantidad_de_datos_recibidos = len(dic[boya][tipo])
            esperados.append(cantidad_de_datos_esperados)
            recibidos.append(cantidad_de_datos_recibidos)
            
        df_salida["boya"] = pd.Series(list(dic.keys()))
        df_salida[f"{tipo}_esperados"] = pd.Series(esperados)
        df_salida[f"{tipo}_recibidos"] = pd.Series(recibidos) 
    
    return df_salida

def guardar_excel(df, ruta_a_carpeta_de_guardado, nombre_de_excel_de_salida):
    """Guarda el DataFrame de salida en un archivo Excel."""    
    ruta_a_archivo = crear_ruta_a_archivo(f"{nombre_de_excel_de_salida}.xlsx", ruta_a_carpeta_de_guardado)
    if not os.path.exists(os.path.dirname(ruta_a_archivo)):
        os.makedirs(os.path.dirname(ruta_a_archivo))
    df.to_excel(ruta_a_archivo, index=False)
    print(f"Archivo guardado en: {ruta_a_archivo}")


def procesar_datos_boyas(ruta_a_carpeta: str, fecha_inicial: str, fecha_final: str, 
                         ruta_guardado: str, nombre_salida: str) -> pd.DataFrame:
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
    print("="*60)
    print("INICIANDO PROCESAMIENTO DE DATOS DE BOYAS")
    print("="*60)
    
    # 1. Buscar archivos CSV
    print(f"\n1. Buscando archivos CSV en: {ruta_a_carpeta}")
    archivos = buscar_archivos_csv(ruta_a_carpeta)
    print(f"   ✓ Encontrados {len(archivos)} archivos CSV")
    
    # 2. Crear diccionario de boyas
    print("\n2. Creando estructura de datos para boyas...")
    dic = crear_diccionario_de_boyas(archivos)
    print(f"   ✓ Boyas identificadas: {', '.join(dic.keys())}")
    
    # 3. Llenar datos del diccionario
    print("\n3. Cargando y filtrando datos por fecha...")
    print(f"   Rango: {fecha_inicial} → {fecha_final}")
    dic = llenar_datos_de_diccionario_de_boyas(dic, ruta_a_carpeta, fecha_inicial, fecha_final)
    print("   ✓ Datos cargados y filtrados")
    
    # 4. Crear DataFrame de salida
    print("\n4. Generando reporte de datos esperados vs recibidos...")
    df_salida = crear_dataframe_de_salida(dic, fecha_inicial, fecha_final)
    print("   ✓ Reporte generado")
    
    # 5. Guardar Excel
    print(f"\n5. Guardando archivo Excel: {nombre_salida}.xlsx")
    guardar_excel(df_salida, ruta_guardado, nombre_salida)
    
    print("\n" + "="*60)
    print("PROCESAMIENTO COMPLETADO EXITOSAMENTE")
    print("="*60 + "\n")
    
    return df_salida
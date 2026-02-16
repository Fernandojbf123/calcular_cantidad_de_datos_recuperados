"""
Configuraciones del módulo de PROCESAMIENTO de datos.

Este archivo contiene solo las configuraciones relacionadas con el 
procesamiento y análisis de archivos CSV de boyas.
"""

# ============== RUTAS DE ARCHIVOS ==============
# Ruta donde están los archivos CSV a procesar
RUTA_DATOS_CRUDOS = "downloads"

# Ruta donde se guardará el archivo Excel de salida
RUTA_GUARDADO = "downloads/"

# ============== CONFIGURACIÓN DE FECHAS ==============
# Las fechas se calculan automáticamente basadas en la fecha actual del sistema

# Mes específico a procesar (1-12). Si es None, usa el mes actual
MES_ESTUDIO = None

# Día inicial del periodo
DIA_INICIAL = 1
HORA_INICIAL = 0
MINUTOS_INICIAL = 0

# Dia final
DIA_FINAL = None # Poner una fecha sino, dejar en None y se calculará automáticamente como el día actual 
HORA_FINAL = 21
MINUTOS_FINAL = 59

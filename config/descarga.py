"""
Configuraciones del módulo de DESCARGA con Selenium.

Este archivo contiene solo las configuraciones relacionadas con la 
descarga automatizada de datos usando Selenium.
"""

# ============== CONFIGURACIONES DE SELENIUM ==============
# Navegador a utilizar: "chrome", "firefox", "edge"
NAVEGADOR = "chrome"

# Modo headless (sin interfaz gráfica) - útil para servidores
HEADLESS_MODE = False

# Tiempo de espera implícito para encontrar elementos (segundos)
IMPLICIT_WAIT = 10

# ============== CONFIGURACIONES DE DESCARGA ==============
# Carpeta donde se guardarán los archivos descargados
CARPETA_DESCARGAS = "downloads"

# Tiempo de espera máximo para que complete una descarga (segundos)
TIMEOUT_DESCARGA = 60

# Intentos de reintento en caso de error
MAX_REINTENTOS = 3

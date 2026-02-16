##### NO TOCAR ESTE ARCHIVO #####

import os
from dotenv import load_dotenv
from .download_settings import *
from .process_settings import *

load_dotenv()
def load_download_settings():
    return {
        "navegador": NAVEGADOR,
        "headless_mode": HEADLESS_MODE,
        "carpeta_descargas": CARPETA_DESCARGAS,
        "implicit_wait": IMPLICIT_WAIT,
        "timeout_descarga": TIMEOUT_DESCARGA,
        "max_reintentos": MAX_REINTENTOS,
        "base_url": os.getenv("URL"),
        "user_login": os.getenv("USER_LOGIN"),
        "user_password": os.getenv("USER_PASSWORD")
    }
    
def load_process_settings():
    return {
        "ruta_datos_crudos": RUTA_DATOS_CRUDOS,
        "ruta_guardado": RUTA_GUARDADO,
    }
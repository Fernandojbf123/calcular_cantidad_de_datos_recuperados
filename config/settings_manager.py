##### NO TOCAR ESTE ARCHIVO #####
import os
import pandas as pd
from datetime import datetime
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
        "mes_estudio": MES_ESTUDIO,
        "dia_inicial": DIA_INICIAL,
        "hora_inicial": HORA_INICIAL,
        "minutos_inicial": MINUTOS_INICIAL,
        "dia_final": DIA_FINAL,
        "hora_final": HORA_FINAL,
        "minutos_final": MINUTOS_FINAL,
    }
    
################### Exclusivo de descarga ###################
class DescargaManager:
    """
    Gestor de configuraciones para el módulo de descarga con Selenium.
    Este archivo carga las configuraciones desde el archivo .env y desde config/config_manager.
    Proporciona métodos para validar y mostrar la configuración actual.
    """
    
    download_settings = load_download_settings()
    
    # ============== CREDENCIALES (desde .env) ==============
    URL = download_settings["base_url"]
    USER_LOGIN = download_settings["user_login"]
    USER_PASSWORD = download_settings["user_password"]
    
    # ============== CONFIGURACIONES DE SELENIUM ==============
    NAVEGADOR = download_settings["navegador"]
    HEADLESS_MODE = download_settings["headless_mode"]
    IMPLICIT_WAIT = download_settings["implicit_wait"]
    
    # ============== CONFIGURACIONES DE DESCARGA ==============
    CARPETA_DESCARGAS = download_settings["carpeta_descargas"]
    TIMEOUT_DESCARGA = download_settings["timeout_descarga"]
    MAX_REINTENTOS = download_settings["max_reintentos"]
    
    # ============== MÉTODOS DE VALIDACIÓN ==============
    @classmethod
    def validar_credenciales(cls) -> bool:
        """Valida que las credenciales estén configuradas."""
        if not cls.USER_LOGIN or not cls.USER_PASSWORD:
            print("⚠️  Advertencia: Credenciales no configuradas en .env")
            return False
        if not cls.URL:
            print("⚠️  Advertencia: URL no configurada en .env")
            return False
        return True
    
    @classmethod
    def crear_carpetas_necesarias(cls):
        """Crea las carpetas necesarias para descarga si no existen."""
        if cls.CARPETA_DESCARGAS and not os.path.exists(cls.CARPETA_DESCARGAS):
            os.makedirs(cls.CARPETA_DESCARGAS)
    
    @classmethod
    def mostrar_configuracion(cls):
        """Muestra la configuración actual del módulo de descarga (sin mostrar credenciales completas)."""
        print("\n" + "="*60)
        print("CONFIGURACIÓN - MÓDULO DE DESCARGA")
        print("="*60)
        print(f"URL Web:              {cls.URL if cls.URL else 'No configurada'}")
        print(f"Usuario:              {cls.USER_LOGIN if cls.USER_LOGIN else 'No configurado'}")
        print(f"Password:             {'*' * len(cls.USER_PASSWORD) if cls.USER_PASSWORD else 'No configurado'}")
        print(f"Navegador:            {cls.NAVEGADOR}")
        print(f"Modo headless:        {cls.HEADLESS_MODE}")
        print(f"Implicit wait:        {cls.IMPLICIT_WAIT}s")
        print(f"Carpeta descargas:    {cls.CARPETA_DESCARGAS}")
        print(f"Timeout descarga:     {cls.TIMEOUT_DESCARGA}s")
        print(f"Máx. reintentos:      {cls.MAX_REINTENTOS}")
        print("="*60 + "\n")


#################### Exclusivo de procesamiento ###################
class ProcessManager:
    """
    Gestor de configuraciones para el módulo de procesamiento de datos.
    Carga las rutas y configuraciones necesarias para el procesamiento.
    Las fechas se calculan dinámicamente basadas en la configuración y fecha actual.
    """
    
    process_settings = load_process_settings()
    RUTA_DATOS_CRUDOS = process_settings["ruta_datos_crudos"]
    RUTA_GUARDADO = process_settings["ruta_guardado"]
    MES_ESTUDIO = process_settings["mes_estudio"]
    
    DIA_INICIAL = process_settings["dia_inicial"]
    HORA_INICIAL = process_settings["hora_inicial"]
    MINUTOS_INICIAL = process_settings["minutos_inicial"]
    
    DIA_FINAL = process_settings["dia_final"]
    HORA_FINAL = process_settings["hora_final"]
    MINUTOS_FINAL = process_settings["minutos_final"]
    
    FECHA_ACTUAL = pd.to_datetime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    @classmethod
    def crear_carpeta_de_guardado(cls):
        """Crea las carpetas necesarias para procesamiento si no existen."""
        if cls.RUTA_GUARDADO and not os.path.exists(cls.RUTA_GUARDADO):
            os.makedirs(cls.RUTA_GUARDADO)

    @classmethod
    def validar_rutas(cls) -> None:
        """Valida que las rutas estén configuradas."""
        if not cls.RUTA_DATOS_CRUDOS or not cls.RUTA_GUARDADO:
            print("⚠️  Advertencia: Rutas no configuradas en process_settings.py")
            raise FileNotFoundError("Rutas no configuradas correctamente.")
        
    @classmethod
    def get_starting_date(cls) -> pd.Timestamp:
        """la fecha de inicio del estudio.
        Usa el mes especificado o el mes actual, comenzando en el día configurado.
        
        Returns:
            pd.Timestamp: Fecha inicial del estudio
        """
        hora = cls.HORA_INICIAL
        minutos = cls.MINUTOS_INICIAL
        dia = cls.DIA_INICIAL
        mes = cls.MES_ESTUDIO if cls.MES_ESTUDIO is not None else cls.FECHA_ACTUAL.month
        año = cls.FECHA_ACTUAL.year
        
        # Crear fecha inicial con el día especificado
        fi = pd.Timestamp(year=año, month=mes, day=dia, 
                         hour=hora, minute=minutos, second=0, microsecond=0)

        return fi
    

    @classmethod
    def get_ending_date(cls) -> pd.Timestamp:
        """
        Calcula la fecha final del estudio.
        Usa la fecha actual del sistema con la hora y minutos configurados.
        
        Returns:
            pd.Timestamp: Fecha final del estudio
        """
        # Usar fecha actual con hora y minutos configurados
        hora = cls.HORA_FINAL
        minutos = cls.MINUTOS_FINAL
        dia = cls.DIA_FINAL if cls.DIA_FINAL is not None else cls.FECHA_ACTUAL.day 
        mes = cls.MES_ESTUDIO if cls.MES_ESTUDIO is not None else cls.FECHA_ACTUAL.month
        año = cls.FECHA_ACTUAL.year
        
        fe = pd.Timestamp(year=año, month=mes, day=dia, 
                         hour=hora, minute=minutos, second=59, microsecond=999999)
        
        return fe
    
    
    @classmethod
    def crear_nombre_de_archivo_de_salida_excel(cls):
        """Crea un nombre de archivo de salida basado en el rango de fechas."""
        fe = cls.get_ending_date()
        nombre_salida = f"reporte_{fe.strftime('%Y%m%d%H')}"
        return nombre_salida
    

############################ Instancias globales de gestores ############################
# Instancia global del gestor de descarga
descarga_config = DescargaManager()

# Instancia global del gestor de procesamiento
process_config = ProcessManager()


"""
Gestor de configuraciones del módulo de DESCARGA.

Este gestor maneja solo las configuraciones relacionadas con la 
descarga automatizada de datos usando Selenium.
"""

import os
from dotenv import load_dotenv
from config import descarga

# Cargar variables de entorno desde .env
load_dotenv()


class DescargaManager:
    """Gestor de configuraciones para el módulo de descarga con Selenium."""
    
    # ============== CREDENCIALES (desde .env) ==============
    WEB_URL = os.getenv("WEB_URL", "")
    USER_LOGIN = os.getenv("USER_LOGIN", "")
    USER_PASSWORD = os.getenv("USER_PASSWORD", "")
    
    # ============== CONFIGURACIONES DE SELENIUM ==============
    NAVEGADOR = descarga.NAVEGADOR
    HEADLESS_MODE = descarga.HEADLESS_MODE
    IMPLICIT_WAIT = descarga.IMPLICIT_WAIT
    
    # ============== CONFIGURACIONES DE DESCARGA ==============
    CARPETA_DESCARGAS = descarga.CARPETA_DESCARGAS
    TIMEOUT_DESCARGA = descarga.TIMEOUT_DESCARGA
    MAX_REINTENTOS = descarga.MAX_REINTENTOS
    
    # ============== MÉTODOS DE VALIDACIÓN ==============
    @classmethod
    def validar_credenciales(cls) -> bool:
        """Valida que las credenciales estén configuradas."""
        if not cls.USER_LOGIN or not cls.USER_PASSWORD:
            print("⚠️  Advertencia: Credenciales no configuradas en .env")
            return False
        if not cls.WEB_URL:
            print("⚠️  Advertencia: WEB_URL no configurada en .env")
            return False
        return True
    
    @classmethod
    def crear_carpetas_necesarias(cls):
        """Crea las carpetas necesarias para descarga si no existen."""
        if cls.CARPETA_DESCARGAS and not os.path.exists(cls.CARPETA_DESCARGAS):
            os.makedirs(cls.CARPETA_DESCARGAS)
            print(f"✓ Carpeta creada: {cls.CARPETA_DESCARGAS}")
    
    @classmethod
    def mostrar_configuracion(cls):
        """Muestra la configuración actual del módulo de descarga (sin mostrar credenciales completas)."""
        print("\n" + "="*60)
        print("CONFIGURACIÓN - MÓDULO DE DESCARGA")
        print("="*60)
        print(f"URL Web:              {cls.WEB_URL if cls.WEB_URL else 'No configurada'}")
        print(f"Usuario:              {'***' if cls.USER_LOGIN else 'No configurado'}")
        print(f"Password:             {'***' if cls.USER_PASSWORD else 'No configurado'}")
        print(f"Navegador:            {cls.NAVEGADOR}")
        print(f"Modo headless:        {cls.HEADLESS_MODE}")
        print(f"Implicit wait:        {cls.IMPLICIT_WAIT}s")
        print(f"Carpeta descargas:    {cls.CARPETA_DESCARGAS}")
        print(f"Timeout descarga:     {cls.TIMEOUT_DESCARGA}s")
        print(f"Máx. reintentos:      {cls.MAX_REINTENTOS}")
        print("="*60 + "\n")


# Instancia global del gestor de descarga
descarga_config = DescargaManager()

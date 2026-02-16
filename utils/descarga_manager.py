"""
Gestor de configuraciones del módulo de DESCARGA.

Este gestor maneja solo las configuraciones relacionadas con la 
descarga automatizada de datos usando Selenium.
"""

import os
from config.config_manager import load_download_settings

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


# Instancia global del gestor de descarga
descarga_config = DescargaManager()

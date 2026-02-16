
"""
Orquestador del módulo de descarga.

Este archivo coordina el flujo del proceso de descarga llamando a los servicios.
No contiene lógica de negocio, solo orquesta la ejecución.
"""
import time
from config.settings_manager import descarga_config
from download.drivers.driver_manager import DriverManager
from download.services import login_service
from download.services import dinamic_dashboard_service
from download.services import download_service

def run_download():
    """
    Orquesta el proceso completo de descarga.
    
    Flujo:
    1. Validar configuración
    2. Crear driver
    3. Login
    4. Navegar a FTP
    5. Descargar datos
    6. Cerrar driver
    """
    # ============== SETUP ==============
    descarga_config.mostrar_configuracion()
    
    # 1. Validar configuración
    if not descarga_config.validar_credenciales():
        return ## Terminar el proceso si las credenciales no están configuradas
    
    descarga_config.crear_carpetas_necesarias()
  
    # 2. Crear driver manager
    driver_manager = DriverManager(
        navegador=descarga_config.NAVEGADOR,
        headless=descarga_config.HEADLESS_MODE,
        carpeta_descargas=descarga_config.CARPETA_DESCARGAS,
        implicit_wait=descarga_config.IMPLICIT_WAIT
    )
    
    try:
        # ============== EJECUCIÓN ==============
        driver = driver_manager.crear_driver()
        
        # 3. Login
        login_service.perform_login(
            driver=driver,
            url=descarga_config.URL,
            username=descarga_config.USER_LOGIN,
            password=descarga_config.USER_PASSWORD
        )
        
        # 4. Navegación al menú FTP
        dinamic_dashboard_service.navigate_to_ftp_section(driver)
        
        # 5. Proceso de descarga
        download_service.download_bmt_bot_altura_ola_data(driver)
        
        # Esperar a que se completen las descargas
        time.sleep(10)
        print("\n✅ Proceso de descarga completado exitosamente")
        
    except Exception as e:
        print(f"\n❌ Error durante la descarga: {str(e)}")
        import traceback
        traceback.print_exc()
    
    # 6. Cerrar driver
    finally:
        # ============== TEARDOWN ==============
        driver_manager.cerrar_driver()
    


from utils.descarga_manager import descarga_config
from utils.driver_manager import DriverManager
from pages.login_page import LoginPage
from pages.dinamic_dashboard_page import DinamicDashboardPage
from pages.download_page import DownloadPage
import time


def main():
    """
    Script standalone para ejecutar solo el módulo de DESCARGA.
    Este script es completamente independiente del módulo de procesamiento.
    Ejecuta la descarga de datos desde la web usando Selenium.
    """

    
    # Mostrar configuración actual
    descarga_config.mostrar_configuracion()
    
    # Validar configuración
    if not descarga_config.validar_credenciales():
        print("❌ Error: Credenciales no configuradas correctamente.")
        print("💡 Edita el archivo .env con tus credenciales reales.\n")
        return
    
    # Crear carpetas necesarias
    descarga_config.crear_carpetas_necesarias()
    
    print("="*60)
    print("🌐 MÓDULO DE DESCARGA")
    print("="*60)
    
    # Crear el driver manager
    driver_manager = DriverManager(
        navegador=descarga_config.NAVEGADOR,
        headless=descarga_config.HEADLESS_MODE,
        carpeta_descargas=descarga_config.CARPETA_DESCARGAS,
        implicit_wait=descarga_config.IMPLICIT_WAIT
    )
    
    try:
        # Crear el driver
        driver = driver_manager.crear_driver()
        
        # Crear página de login
        login_page = LoginPage(driver, descarga_config.URL)
        
        # Realizar login
        login_page.login(
            username=descarga_config.USER_LOGIN,
            password=descarga_config.USER_PASSWORD
        )
        print("✅ Login completado exitosamente")
        
        # Esperar a que cargue la página principal
        time.sleep(2)
        
        # Navegar al menú FTP desde el dashboard
        dashboard_page = DinamicDashboardPage(driver)
        dashboard_page.navigate_to_ftp()
        print("✅ Navegación al menú FTP completada exitosamente")
        
        # Esperar a que cargue la página de descargas
        time.sleep(2)
        
        # Proceso de descarga
        download_page = DownloadPage(driver)
        download_page.download_all_bmt_bot_data()
        
        # Esperar un poco para que se completen las descargas
        print("⏳ Esperando 10 segundos para que se completen las descargas...")
        time.sleep(10)
        
        print("✅ Proceso de descarga completado exitosamente")
        
    except Exception as e:
        print(f"❌ Error durante la descarga: {str(e)}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Cerrar el driver
        driver_manager.cerrar_driver()
    
    print("="*60 + "\n")


if __name__ == "__main__":
    main()

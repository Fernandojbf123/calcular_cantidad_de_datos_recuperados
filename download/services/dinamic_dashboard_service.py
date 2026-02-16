"""
Servicio de navegación del dashboard - Lógica de negocio para el dashboard.
"""

from download.pages.dinamic_dashboard_page import DinamicDashboardPage
import time


def navigate_to_ftp_section(driver):
    """
    Navega desde el dashboard al menú FTP.
    
    Args:
        driver: WebDriver de Selenium
        
    Returns:
        bool: True si la navegación fue exitosa
    """
    dashboard_page = DinamicDashboardPage(driver)
    try:
        dashboard_page.wait_for_dashboard_load()
        dashboard_page.click_ftp_menu()
        # Esperar a que cargue la página FTP
        time.sleep(2)
        return True
    except Exception as e:
        print(f"❌ Error al navegar al menú FTP: {str(e)}")
        return False    

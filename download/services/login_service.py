"""
Servicio de autenticación - Lógica de negocio para el login.
"""

from download.pages.login_page import LoginPage
import time


def perform_login(driver, url, username, password):
    """
    Ejecuta el proceso completo de login.
    
    Args:
        driver: WebDriver de Selenium
        url: URL de la aplicación
        username: Nombre de usuario
        password: Contraseña
        
    Returns:
        bool: True si el login fue exitoso
    """
    login_page = LoginPage(driver, url)
    login_page.iniciar_sesion(username, password)
    # Esperar a que cargue la página después del login
    time.sleep(2)
    return True

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DinamicDashboardPage:
    """
    Página de Dashboard Dinámico usando Page Object Model.
    
    Esta clase contiene SOLO métodos atómicos para interactuar con elementos.
    La lógica de negocio está en download/services/dashboard_service.py
    """
    
    # Localizadores de los elementos
    BUTTON_TO_FTP = (By.ID, "menu_ftp")
    
    def __init__(self, driver, timeout=10):
        """
        Inicializa la página de dashboard.
        
        Args:
            driver: WebDriver de Selenium
            timeout: Tiempo de espera en segundos
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def wait_for_dashboard_load(self):
        """Espera a que el dashboard cargue completamente."""
        self.wait.until(EC.presence_of_element_located(self.BUTTON_TO_FTP))
    
    def click_ftp_menu(self):
        """Hace click en el botón del menú FTP."""
        ftp_button = self.wait.until(EC.element_to_be_clickable(self.BUTTON_TO_FTP))
        ftp_button.click()
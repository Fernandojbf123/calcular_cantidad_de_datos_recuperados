from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DownloadPage:
    """
    Página de Descarga usando Page Object Model.
    
    Esta clase contiene SOLO métodos atómicos para interactuar con elementos.
    La lógica de negocio está en download/services/download_service.py
    """
    
    # Localizadores
    SIDEBAR_ANCHORS = (By.XPATH, "//a[@onclick and contains(@class, 'nav-link') and .//span[@class='sidenav-normal']]")
    SIDEBAR_ANCHOR_TEXT_SPAN = (By.XPATH, ".//span[@class='sidenav-normal']")
    DATA_DOWNLOAD_LINKS = (By.XPATH, "//a[contains(@class, 'download_ftp') and @data-location-id and .//p]")
    
    def __init__(self, driver, timeout=10):
        """
        Inicializa la página de descargas.
        
        Args:
            driver: WebDriver de Selenium
            timeout: Tiempo de espera en segundos
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    def wait_for_page_load(self):
        """Espera a que la página de descargas cargue completamente."""
        self.wait.until(EC.presence_of_element_located(self.SIDEBAR_ANCHORS))
    
    def get_sidebar_items(self):
        """
        Obtiene todos los elementos de la barra lateral.
        
        Returns:
            Lista de WebElements
        """
        return self.driver.find_elements(*self.SIDEBAR_ANCHORS)
    
    def get_item_text(self, element):
        """
        Obtiene el texto de un elemento de la barra lateral.
        
        Args:
            element: WebElement del anchor
            
        Returns:
            str: Texto del elemento o cadena vacía
        """
        try:
            span = element.find_element(*self.SIDEBAR_ANCHOR_TEXT_SPAN)
            return span.text.strip()
        except:
            return ""
    
    def click_sidebar_item(self, element):
        """
        Hace click en un elemento de la barra lateral.
        
        Args:
            element: WebElement a clickear
        """
        # Scroll al elemento antes de hacer click
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
    
    def scroll_main_to_top(self):
        """Hace scroll al inicio del contenedor principal."""
        self.driver.execute_script("document.getElementById('main').scrollTop = 0;")
    
    def get_download_links(self):
        """
        Obtiene todos los enlaces de descarga disponibles.
        
        Returns:
            Lista de WebElements
        """
        return self.driver.find_elements(*self.DATA_DOWNLOAD_LINKS)
    
    def get_download_link_text(self, element):
        """
        Obtiene el texto de un enlace de descarga.
        
        Args:
            element: WebElement del enlace
            
        Returns:
            str: Texto del enlace o cadena vacía
        """
        try:
            p_element = element.find_element(By.TAG_NAME, "p")
            return p_element.text.strip()
        except:
            return ""
    
    def click_download_link(self, element):
        """
        Hace click en un enlace de descarga.
        
        Args:
            element: WebElement del enlace a clickear
        """
        # Scroll al elemento
        element.click()

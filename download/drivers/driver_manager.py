from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import os


class DriverManager:
    """
        Driver Manager para Selenium WebDriver.
        Gestiona la creación, configuración y cierre del driver de Selenium.
    """
    
    def __init__(self, navegador="chrome", headless=False, carpeta_descargas=None, implicit_wait=10):
        """
        Inicializa el gestor del driver.
        
        Args:
            navegador: Tipo de navegador ("chrome", "firefox", "edge")
            headless: Si debe ejecutarse en modo headless
            carpeta_descargas: Ruta absoluta de la carpeta de descargas
            implicit_wait: Tiempo de espera implícito en segundos
        """
        self.navegador = navegador.lower()
        self.headless = headless
        self.carpeta_descargas = os.path.abspath(carpeta_descargas) if carpeta_descargas else None
        self.implicit_wait = implicit_wait
        self.driver = None
    
    def crear_driver(self):
        """
        Crea y configura el WebDriver según las opciones especificadas.
        
        Returns:
            WebDriver configurado
        """
        if self.navegador == "chrome":
            self.driver = self._crear_chrome_driver()
        elif self.navegador == "firefox":
            self.driver = self._crear_firefox_driver()
        elif self.navegador == "edge":
            self.driver = self._crear_edge_driver()
        else:
            raise ValueError(f"Navegador no soportado: {self.navegador}")
        
        # Configurar tiempo de espera implícito
        self.driver.implicitly_wait(self.implicit_wait)
        
        # Maximizar ventana (opcional)
        if not self.headless:
            self.driver.maximize_window()
            
        return self.driver
    
    def _crear_chrome_driver(self):
        """Crea el driver de Chrome con las opciones configuradas."""
        options = ChromeOptions()
        
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        
        # Configurar carpeta de descargas
        if self.carpeta_descargas:
            prefs = {
                "download.default_directory": self.carpeta_descargas,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            }
            options.add_experimental_option("prefs", prefs)
        
        # Opciones adicionales para estabilidad
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=options)
    
    def _crear_firefox_driver(self):
        """Crea el driver de Firefox con las opciones configuradas."""
        options = FirefoxOptions()
        
        if self.headless:
            options.add_argument("--headless")
        
        # Configurar carpeta de descargas
        if self.carpeta_descargas:
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.dir", self.carpeta_descargas)
            options.set_preference("browser.download.useDownloadDir", True)
            options.set_preference("browser.helperApps.neverAsk.saveToDisk", 
                                   "application/octet-stream,application/vnd.ms-excel,text/csv")
        
        service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=service, options=options)
    
    def _crear_edge_driver(self):
        """Crea el driver de Edge con las opciones configuradas."""
        options = EdgeOptions()
        
        if self.headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
        
        # Configurar carpeta de descargas
        if self.carpeta_descargas:
            prefs = {
                "download.default_directory": self.carpeta_descargas,
                "download.prompt_for_download": False,
                "download.directory_upgrade": True,
                "safebrowsing.enabled": True
            }
            options.add_experimental_option("prefs", prefs)
        
        service = EdgeService(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service, options=options)
    
    def cerrar_driver(self):
        """Cierra el driver y limpia recursos."""
        if self.driver:
            self.driver.quit()
            print("✓ Driver cerrado exitosamente")
    
    def __enter__(self):
        """Permite usar el gestor con context manager."""
        return self.crear_driver()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Cierra el driver al salir del context manager."""
        self.cerrar_driver()

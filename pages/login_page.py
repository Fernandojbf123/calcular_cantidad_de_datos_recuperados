from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
        Página de Login usando Page Object Model.
    """

    
    # Localizadores de los elementos de la página
    USER_INPUT = (By.ID, "user")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "authButton")

    def __init__(self, driver, base_url, timeout=10):
        """
        Inicializa la página de login.
        
        Args:
            driver: WebDriver de Selenium
            base_url: URL base de la aplicación
            timeout: Tiempo de espera en segundos
        """
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout)
        
    def open(self):
        """Abre la página de login."""
        self.driver.get(self.base_url)
        
    def set_username(self, username: str) -> None:
        """Escribe el nombre de usuario."""
        user_input_element = self.wait.until(EC.presence_of_element_located(self.USER_INPUT))
        user_input_element.clear()
        user_input_element.send_keys(username)
        
    def set_password(self, password: str) -> None:
        """Escribe la contraseña."""
        password_input_element = self.wait.until(EC.presence_of_element_located(self.PASSWORD_INPUT))
        password_input_element.clear()
        password_input_element.send_keys(password)
        
    def click_login_button(self) -> None:
        """Hace click en el botón de login."""
        login_button_element = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button_element.click()
        
    def login(self, username: str, password: str) -> None:
        """
        Realiza el proceso de login completo.
        
        Args:
            username: Nombre de usuario
            password: Contraseña
        """
        self.open()
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
        

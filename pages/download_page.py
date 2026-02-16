from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DownloadPage:
    """
        Página de Descarga usando Page Object Model.
        Esta clase se encargará de interactuar con la página de descargas después del login.
    """
    
    # Localizadores
    SIDEBAR_ANCHORS = (By.XPATH, "//a[@onclick and contains(@class, 'nav-link') and .//span[@class='sidenav-normal']]")
    SIDEBAR_ANCHOR_TEXT_SPAN = (By.XPATH, ".//span[@class='sidenav-normal']")  # Span con el texto
    DATA_DOWNLOAD_LINKS = (By.XPATH, "//a[contains(@class, 'download_ftp') and @data-location-id and .//p]")  # Enlaces de descarga
    
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
        print("✓ Página de descargas cargada")
    
    def get_sidebar_anchors(self):
        """
        Obtiene todos los elementos anchor de la barra lateral.
        
        Returns:
            Lista de WebElements
        """
        return self.driver.find_elements(*self.SIDEBAR_ANCHORS)
    
    def get_anchor_text(self, anchor_element):
        """
        Obtiene el texto del segundo span dentro de un anchor.
        
        Args:
            anchor_element: WebElement del anchor
            
        Returns:
            Texto del span o string vacío si no se encuentra
        """
        try:
            span = anchor_element.find_element(*self.SIDEBAR_ANCHOR_TEXT_SPAN)
            return span.text.strip()
        except:
            return ""
    
    def find_and_click_bmt_bot_items(self):
        """
        Busca y hace clic en todos los elementos de la barra lateral 
        que contengan 'BMT' o 'BOT' en su texto.
        
        Returns:
            Lista de textos de los elementos clickeados
        """
        print("\n" + "="*60)
        print("BUSCANDO ELEMENTOS BMT/BOT EN BARRA LATERAL")
        print("="*60)
        
        self.wait_for_page_load()
        anchors = self.get_sidebar_anchors()
        clicked_items = []
        
        print(f"📋 Total de elementos en barra lateral: {len(anchors)}")
        
        for index, anchor in enumerate(anchors):
            text = self.get_anchor_text(anchor)
            
            if text and ("BMT" in text.upper() or "BOT" in text.upper()):
                print(f"✓ Encontrado: {text}")
                clicked_items.append(text)
                
                try:
                    # Scroll al elemento antes de hacer click
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", anchor)
                    time.sleep(0.5)
                    
                    # Hacer click
                    anchor.click()
                    print(f"  ✓ Click realizado en: {text}")
                    
                    # Esperar a que aparezcan los datos
                    time.sleep(1)
                    
                    # Buscar "Datos AlturaOlaSignificante"
                    if self.find_and_download_altura_ola():
                        print(f"  ✅ Descarga iniciada desde: {text}")
                    
                except Exception as e:
                    print(f"  ⚠️ Error al hacer click en {text}: {str(e)}")
        
        print("="*60 + "\n")
        return clicked_items
    
    def find_and_download_altura_ola(self):
        """
        Busca el elemento "Datos AlturaOlaSignificante" en los datos 
        que aparecen a la derecha y hace click para descargar.
        
        Returns:
            True si encontró y clickeó el elemento, False en caso contrario
        """
        try:
            # Scroll hacia arriba en el section main para que aparezcan todas las opciones
            self.driver.execute_script("document.getElementById('main').scrollTop = 0;")
            time.sleep(0.5)
            
            # Esperar a que aparezcan los elementos de descarga
            time.sleep(1)
            download_links = self.driver.find_elements(*self.DATA_DOWNLOAD_LINKS)
            
            for link in download_links:
                # Obtener el texto del <p> dentro del anchor
                try:
                    p_element = link.find_element(By.TAG_NAME, "p")
                    text = p_element.text.strip()
                    
                    if "Datos AlturaOlaSignificante" in text or "AlturaOlaSignificante" in text:
                        print(f"    🎯 Encontrado: {text}")
                        
                        # Scroll al elemento
                        self.driver.execute_script("arguments[0].scrollIntoView(true);", link)
                        time.sleep(0.5)
                        
                        # Hacer click para descargar
                        link.click()
                        print(f"    ✓ Click en descarga: {text}")
                        
                        # Esperar a que inicie la descarga
                        time.sleep(2)
                        
                        return True
                except:
                    continue
            
            return False
            
        except Exception as e:
            print(f"    ⚠️ Error al buscar datos: {str(e)}")
            return False
    
    def download_all_bmt_bot_data(self):
        """
        Proceso completo: busca todos los BMT/BOT, hace click en cada uno
        y descarga los datos de AlturaOlaSignificante.
        """
        print("\n" + "="*60)
        print("🌊 INICIANDO DESCARGA DE DATOS")
        print("="*60)
        
        clicked_items = self.find_and_click_bmt_bot_items()
        
        if clicked_items:
            print(f"\n✅ Proceso completado. Se procesaron {len(clicked_items)} elementos:")
            for item in clicked_items:
                print(f"   - {item}")
        else:
            print("\n⚠️ No se encontraron elementos BMT/BOT")
        
        print("="*60 + "\n")
    
    
    
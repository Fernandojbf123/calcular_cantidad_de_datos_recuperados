"""
Servicio de descargas - Lógica de negocio para descargar archivos.
"""
import os
import time
from download.pages.download_page import DownloadPage
from config.settings_manager import descarga_config



def download_bmt_bot_altura_ola_data(driver):
    """
    Descarga archivos de AlturaOlaSignificante de todas las boyas BMT/BOT.
    
    Esta función contiene la lógica de negocio:
    - Filtra elementos que contengan 'BMT' o 'BOT'
    - Para cada uno, busca el archivo 'Datos AlturaOlaSignificante'
    - Descarga el archivo encontrado
    
    Args:
        driver: WebDriver de Selenium
        
    Returns:
        list: Lista de elementos procesados
    """
    download_page = DownloadPage(driver)
    download_page.wait_for_page_load()
    
    # Obtener todos los elementos de la barra lateral
    sidebar_items = download_page.get_sidebar_items()    
    processed_items = []
    
    files_in_folder = _get_csv_files_in_folder()
    
    # LÓGICA DE NEGOCIO: Filtrar y procesar solo BMT/BOT
    for item in sidebar_items:
        item_text = download_page.get_item_text(item)
        
        # Criterio de negocio: solo procesar BMT o BOT
        if item_text and ("BMT" in item_text.upper() or "BOT" in item_text.upper()):
            processed_items.append(item_text)
            
            try:
                # Hacer click en el elemento de la barra lateral
                download_page.click_sidebar_item(item)
                time.sleep(1)
                
                # Buscar y descargar el archivo específico
                _download_altura_ola_file(download_page,files_in_folder)
                
            except Exception as e:
                print(f"  ⚠️ Error al procesar {item_text}: {str(e)}")
    
    return processed_items


def _download_altura_ola_file(download_page, files_in_folder):
    """
    Función auxiliar para buscar y descargar el archivo de AlturaOlaSignificante.
    
    Args:
        download_page: Instancia de DownloadPage
        files_in_folder: Lista de archivos CSV en la carpeta de descargas
        
    Returns:
        str: Mensaje indicando el estado de la descarga
    """
    msg = "No se consiguió descargar el archivo de AlturaOlaSignificante"
    # Scroll al inicio para que aparezcan todas las opciones
    download_page.scroll_main_to_top()
    time.sleep(0.5)
    
    # Esperar a que aparezcan los enlaces de descarga
    time.sleep(1)
    
    # Obtener todos los enlaces de descarga
    download_links = download_page.get_download_links()
    
    # LÓGICA DE NEGOCIO: Buscar archivo específico "AlturaOlaSignificante"
    for link in download_links:
        link_text = download_page.get_download_link_text(link)
        
        current_file = link_text.replace(' ',"_")
        #datos_AlturaOlaSignificante_BMT3-09-T80_TOTAL
        
        # Criterio de negocio: buscar AlturaOlaSignificante
        # Eliminar archivo existente antes de descargar
        _remove_existing_file(current_file,files_in_folder)
        
        # Hacer click para descargar solo si es de los archivos que se buscan
        if "AlturaOlaSignificante".lower() in link_text.lower():
            download_page.click_download_link(link)
            # Esperar a que inicie la descarga
            time.sleep(2)
            msg = "Descargando archivo de AlturaOlaSignificante..."
            return msg
    
    return msg


def _remove_existing_file(file,files_in_folder=None):
    """
    Elimina archivos existentes con el mismo nombre (incluyendo versiones con (1), (2), etc.).
    
    Args:
        file: Nombre del archivo a eliminar
    """
    try:
        # Extraer el nombre del archivo del texto del enlace
        if file.lower() in files_in_folder:
        # Construir la ruta completa del archivo
            filename = "datos_" +file.split("Datos_")[-1].strip().replace('.csv',"_TOTAL.csv")
            # Obtener la carpeta de descargas
            download_folder = descarga_config.CARPETA_DESCARGAS
            file_path = os.path.join(download_folder, filename)
        
            # Eliminar el archivo si existe
            if os.path.exists(file_path):
                os.remove(file_path)
        
    except Exception as e:
        print(f"    ⚠️  Error al eliminar archivo existente: {str(e)}")


def _get_csv_files_in_folder():
    """
    Función auxiliar para listar archivos CSV en la carpeta de descargas.
    Útil para depuración y ver qué archivos hay antes de iniciar el proceso.
    """
    files = None
    download_folder = descarga_config.CARPETA_DESCARGAS
    if os.path.exists(download_folder):
        files = [f.lower() for f in os.listdir(download_folder) if f.endswith('.csv')]
    return files

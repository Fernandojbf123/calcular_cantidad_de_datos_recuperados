import download.main_download
import processing.main_processing

def main():
    """
    Script principal para ejecutar todo el proceso de descarga y procesamiento.
    Primero ejecuta la descarga de datos desde la web usando Selenium, y luego
    procesa los archivos CSV descargados para generar reportes Excel.
    """
    
    print("="*60)
    print("🚀 INICIANDO PROCESO COMPLETO")
    print("="*60)
    
    # Ejecutar módulo de descarga
    print("\n🔹 EJECUTANDO MÓDULO DE DESCARGA")
    download.main_download.main()
    
    # Ejecutar módulo de procesamiento
    print("\n🔹 EJECUTANDO MÓDULO DE PROCESAMIENTO")
    processing.main_processing.main()
    
    print("\n✅ PROCESO COMPLETO FINALIZADO")
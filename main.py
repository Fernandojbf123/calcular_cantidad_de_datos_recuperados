import sys
from pathlib import Path

# Agregar la raíz del proyecto al path para que los imports funcionen
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

import download.orquestador as download
import processing.orquestador as processing

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
    download.run_download()
    
    # Ejecutar módulo de procesamiento
    print("\n🔹 EJECUTANDO MÓDULO DE PROCESAMIENTO")
    processing.run_processing()
    
    print("\n✅ PROCESO COMPLETO FINALIZADO")
    
if __name__ == "__main__":
    main()
import sys
from pathlib import Path

# Agregar la raíz del proyecto al path para que los imports funcionen
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from download.orquestador import run_download

def main():
    """
    Script standalone para ejecutar solo el módulo de DESCARGA.
    Este script es completamente independiente del módulo de procesamiento.
    Ejecuta la descarga de datos desde la web usando Selenium.
    """
    run_download()

if __name__ == "__main__":
    run_download()

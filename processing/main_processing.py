import sys
from pathlib import Path

# Agregar la raíz del proyecto al path para que los imports funcionen
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from processing.orquestador import run_processing

def main():
    """
    Script standalone para ejecutar solo el módulo de PROCESAMIENTO.
    Este script es completamente independiente del módulo de descarga.
    Procesa archivos CSV ya existentes y genera reportes Excel.
    """
    run_processing()


if __name__ == "__main__":
    run_processing()

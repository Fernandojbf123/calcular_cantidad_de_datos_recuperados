

from utils.procesador import buscar_archivos_csv, crear_dataframe_de_salida, procesar_datos_boyas
from utils import procesamiento_config
from utils.procesamiento_manager import *


def main():
    """
    Script standalone para ejecutar solo el módulo de PROCESAMIENTO.
    Este script es completamente independiente del módulo de descarga.
    Procesa archivos CSV ya existentes y genera reportes Excel.
    """
    ############## NO TOCAR ##############
    procesar_datos_boyas(ruta_a_carpeta: , fecha_inicial: , fecha_final:, 
                         ruta_guardado, nombre_salida:)


if __name__ == "__main__":
    main()

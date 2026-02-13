"""
Paquete de utilidades para el proyecto.
Contiene los gestores de configuración y procesadores de cada módulo.
"""

from .procesador import procesar_datos_boyas
from .procesamiento_manager import ProcesamientoManager, procesamiento_config
from .descarga_manager import DescargaManager, descarga_config

__all__ = [
    'procesar_datos_boyas',
    'ProcesamientoManager', 
    'procesamiento_config',
    'DescargaManager',
    'descarga_config'
]

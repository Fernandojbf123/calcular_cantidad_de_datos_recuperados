"""
Paquete de configuraciones del proyecto.

IMPORTANTE: Las configuraciones están organizadas por módulo:
- procesamiento.py: Configuraciones del módulo de procesamiento de datos
- descarga.py: Configuraciones del módulo de descarga con Selenium

Los gestores que orquestan todo están en:
- utils/procesamiento_manager.py: Gestor del módulo de procesamiento
- utils/descarga_manager.py: Gestor del módulo de descarga
"""

# Re-exportar gestores para compatibilidad
from utils.procesamiento_manager import ProcesamientoManager, procesamiento_config
from utils.descarga_manager import DescargaManager, descarga_config

# Alias para retrocompatibilidad
config = procesamiento_config  # Por defecto, apunta al módulo de procesamiento

__all__ = [
    'ProcesamientoManager', 
    'procesamiento_config',
    'DescargaManager',
    'descarga_config',
    'config'  # Alias retrocompatible
]

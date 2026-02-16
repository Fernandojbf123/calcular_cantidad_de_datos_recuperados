# """
# Gestor de configuraciones del módulo de PROCESAMIENTO.

# Este gestor maneja solo las configuraciones relacionadas con el 
# procesamiento y análisis de datos de boyas.
# """

# import os
# from datetime import datetime
# from config import procesamiento


# class ProcesamientoManager:
#     """Gestor de configuraciones para el módulo de procesamiento de datos."""
    
#     # ============== CONFIGURACIONES ESTÁTICAS ==============
#     RUTA_DATOS_CRUDOS = procesamiento.RUTA_DATOS_CRUDOS
#     RUTA_GUARDADO = procesamiento.RUTA_GUARDADO
    
#     # ============== CONFIGURACIONES DINÁMICAS ==============
#     @staticmethod
#     def _obtener_fecha_inicial():
#         """Obtiene el primer día del mes actual a las 00:00:00."""
#         hoy = datetime.now()
#         return hoy.replace(day=1, hour=0, minute=0, second=0, microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
    
#     @staticmethod
#     def _obtener_fecha_final():
#         """Obtiene la fecha actual a las 21:59:59."""
#         hoy = datetime.now()
#         return hoy.replace(hour=21, minute=59, second=59, microsecond=0).strftime("%Y-%m-%d %H:%M:%S")
    
#     @staticmethod
#     def _obtener_nombre_salida(fecha_inicial, fecha_final):
#         """Genera el nombre de archivo basado en las fechas inicial y final."""
#         fecha_ini = datetime.strptime(fecha_inicial, "%Y-%m-%d %H:%M:%S")
#         fecha_fin = datetime.strptime(fecha_final, "%Y-%m-%d %H:%M:%S")
#         return f"{fecha_ini.strftime('%Y%m%d%H')}_{fecha_fin.strftime('%Y%m%d%H')}"
    
#     # Fechas calculadas dinámicamente
#     FECHA_INICIAL = _obtener_fecha_inicial.__func__()
#     FECHA_FINAL = _obtener_fecha_final.__func__()
#     NOMBRE_EXCEL_SALIDA = _obtener_nombre_salida.__func__(FECHA_INICIAL, FECHA_FINAL)
    
#     # ============== MÉTODOS DE VALIDACIÓN ==============
#     @classmethod
#     def validar_rutas(cls) -> bool:
#         """Valida que las rutas de procesamiento existan."""
#         if cls.RUTA_DATOS_CRUDOS and not os.path.exists(cls.RUTA_DATOS_CRUDOS):
#             print(f"⚠️  Advertencia: La ruta {cls.RUTA_DATOS_CRUDOS} no existe.")
#             return False
#         return True
    
#     @classmethod
#     def crear_carpetas_necesarias(cls):
#         """Crea las carpetas necesarias para procesamiento si no existen."""
#         if cls.RUTA_GUARDADO and not os.path.exists(cls.RUTA_GUARDADO):
#             os.makedirs(cls.RUTA_GUARDADO)
#             print(f"✓ Carpeta creada: {cls.RUTA_GUARDADO}")
    
#     @classmethod
#     def mostrar_configuracion(cls):
#         """Muestra la configuración actual del módulo de procesamiento."""
#         print("\n" + "="*60)
#         print("CONFIGURACIÓN - MÓDULO DE PROCESAMIENTO")
#         print("="*60)
#         print(f"Ruta datos crudos:    {cls.RUTA_DATOS_CRUDOS}")
#         print(f"Ruta guardado:        {cls.RUTA_GUARDADO}")
#         print(f"Fecha inicial:        {cls.FECHA_INICIAL}")
#         print(f"Fecha final:          {cls.FECHA_FINAL}")
#         print(f"Nombre salida:        {cls.NOMBRE_EXCEL_SALIDA}.xlsx")
#         print("="*60 + "\n")


# # Instancia global del gestor de procesamiento
# procesamiento_config = ProcesamientoManager()

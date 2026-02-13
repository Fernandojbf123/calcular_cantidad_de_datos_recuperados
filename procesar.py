"""
Script standalone para ejecutar solo el módulo de PROCESAMIENTO.

Este script es completamente independiente del módulo de descarga.
Procesa archivos CSV ya existentes y genera reportes Excel.
"""

from utils.procesador import procesar_datos_boyas
from utils import procesamiento_config


def main():
    """Función principal que ejecuta solo el módulo de procesamiento."""
    
    # Mostrar configuración actual
    procesamiento_config.mostrar_configuracion()
    
    # Validar configuración
    if not procesamiento_config.validar_rutas():
        print("⚠️  Algunas rutas no están configuradas correctamente.")
        print("💡 Edita el archivo config/procesamiento.py para ajustar las rutas.\n")
    
    # Crear carpetas necesarias
    procesamiento_config.crear_carpetas_necesarias()
    
    try:
        # Ejecutar procesamiento
        df_resultado = procesar_datos_boyas(
            ruta_a_carpeta=procesamiento_config.RUTA_DATOS_CRUDOS,
            fecha_inicial=procesamiento_config.FECHA_INICIAL,
            fecha_final=procesamiento_config.FECHA_FINAL,
            ruta_guardado=procesamiento_config.RUTA_GUARDADO,
            nombre_salida=procesamiento_config.NOMBRE_EXCEL_SALIDA
        )
        
        # Mostrar resumen
        print("\n📊 RESUMEN DEL REPORTE:")
        print(df_resultado.to_string(index=False))
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Verifica que la ruta de la carpeta sea correcta.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        raise


if __name__ == "__main__":
    main()

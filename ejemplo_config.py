"""
Script de ejemplo/demo para mostrar las configuraciones dinámicas.
Ejecuta este archivo para ver las fechas calculadas automáticamente.
"""

from utils import procesamiento_config, descarga_config

def mostrar_ejemplo():
    """Muestra un ejemplo de cómo funcionan las configuraciones de cada módulo."""
    
    print("\n" + "="*70)
    print(" 📊 CONFIGURACIONES DE MÓDULOS INDEPENDIENTES")
    print("="*70)
    
    print("\n" + "─"*70)
    print("📊 MÓDULO DE PROCESAMIENTO")
    print("─"*70)
    procesamiento_config.mostrar_configuracion()
    
    print("\n" + "─"*70)
    print("🌐 MÓDULO DE DESCARGA")
    print("─"*70)
    descarga_config.mostrar_configuracion()
    
    print("\n💡 VENTAJAS DE ESTA ARQUITECTURA:")
    print("   ✅ Cada módulo es completamente independiente")
    print("   ✅ Puedes usar solo uno sin necesitar el otro")
    print("   ✅ Configuraciones separadas por responsabilidad")
    print("   ✅ Fácil de mantener y escalar")
    
    print("\n💡 PARA MODIFICAR:")
    print("   📊 Procesamiento → config/procesamiento.py")
    print("   🌐 Descarga → config/descarga.py y .env")
    print("   🔧 Lógica de fechas → utils/procesamiento_manager.py")
    
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    mostrar_ejemplo()

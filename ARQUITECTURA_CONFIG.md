"""
ARQUITECTURA DE CONFIGURACIONES
================================

Este documento explica cómo están organizadas las configuraciones del proyecto.

┌─────────────────────────────────────────────────────────────┐
│  PRINCIPIO: MÓDULOS COMPLETAMENTE INDEPENDIENTES             │
└─────────────────────────────────────────────────────────────┘

Cada módulo tiene su propio gestor de configuraciones independiente:

📊 MÓDULO DE PROCESAMIENTO
   ├─ config/procesamiento.py       → Configuraciones
   └─ utils/procesamiento_manager.py → Gestor

🌐 MÓDULO DE DESCARGA
   ├─ config/descarga.py             → Configuraciones
   └─ utils/descarga_manager.py      → Gestor

🔒 COMPARTIDO
   └─ .env                           → Credenciales sensibles


┌─────────────────────────────────────────────────────────────┐
│  FLUJO DE CONFIGURACIONES                                    │
└─────────────────────────────────────────────────────────────┘

MÓDULO DE PROCESAMIENTO:
1. Usuario edita: config/procesamiento.py
2. Gestor procesa: utils/procesamiento_manager.py
   ├─ Lee procesamiento.py
   ├─ Calcula fechas dinámicamente
   ├─ Genera nombres de archivos
   └─ Valida rutas
3. Aplicación usa: from utils import procesamiento_config

MÓDULO DE DESCARGA:
1. Usuario edita: config/descarga.py y .env
2. Gestor procesa: utils/descarga_manager.py
   ├─ Lee descarga.py
   ├─ Lee credenciales de .env
   ├─ Valida credenciales
   └─ Prepara Selenium
3. Aplicación usa: from utils import descarga_config


┌─────────────────────────────────────────────────────────────┐
│  ¿QUÉ VA EN CADA ARCHIVO?                                   │
└─────────────────────────────────────────────────────────────┘

📊 config/procesamiento.py
   ├─ RUTA_DATOS_CRUDOS
   ├─ RUTA_GUARDADO
   └─ Solo configs de procesamiento de datos
   
🔧 utils/procesamiento_manager.py
   ├─ Lee procesamiento.py
   ├─ Calcula FECHA_INICIAL (automático)
   ├─ Calcula FECHA_FINAL (automático)
   ├─ Genera NOMBRE_EXCEL_SALIDA (automático)
   └─ Métodos: validar_rutas(), crear_carpetas_necesarias()

🌐 config/descarga.py
   ├─ NAVEGADOR
   ├─ HEADLESS_MODE
   ├─ CARPETA_DESCARGAS
   ├─ TIMEOUT_DESCARGA
   └─ Solo configs de descarga con Selenium

🔧 utils/descarga_manager.py
   ├─ Lee descarga.py
   ├─ Lee credenciales de .env (WEB_URL, USER_LOGIN, USER_PASSWORD)
   └─ Métodos: validar_credenciales(), crear_carpetas_necesarias()

🔒 .env
   ├─ WEB_URL (usada por descarga)
   ├─ USER_LOGIN (usada por descarga)
   └─ USER_PASSWORD (usada por descarga)
   ⚠️  NUNCA subir a Git


┌─────────────────────────────────────────────────────────────┐
│  EJEMPLO DE USO                                              │
└─────────────────────────────────────────────────────────────┘

# OPCIÓN 1: Importar desde utils (recomendado)
from utils import procesamiento_config, descarga_config

# Usar módulo de procesamiento:
print(procesamiento_config.RUTA_DATOS_CRUDOS)
print(procesamiento_config.FECHA_INICIAL)      # Calculado automáticamente
print(procesamiento_config.NOMBRE_EXCEL_SALIDA) # Calculado automáticamente
procesamiento_config.validar_rutas()
procesamiento_config.mostrar_configuracion()

# Usar módulo de descarga:
print(descarga_config.WEB_URL)                 # De .env
print(descarga_config.NAVEGADOR)               # De descarga.py
print(descarga_config.CARPETA_DESCARGAS)
descarga_config.validar_credenciales()
descarga_config.mostrar_configuracion()

# OPCIÓN 2: Importar desde config (retrocompatible)
from config import procesamiento_config, descarga_config


┌─────────────────────────────────────────────────────────────┐
│  BENEFICIOS DE ESTA ARQUITECTURA                            │
└─────────────────────────────────────────────────────────────┘

✅ Módulos completamente independientes
✅ Puedes usar solo procesamiento sin descarga (y viceversa)
✅ Cada módulo tiene su propio gestor especializado
✅ Fácil de mantener: editas solo lo que necesitas
✅ Escalable: agregar más módulos es trivial
✅ Testing: testeas cada módulo por separado
✅ Credenciales protegidas en .env
✅ Fechas siempre actualizadas automáticamente


┌─────────────────────────────────────────────────────────────┐
│  ESTRUCTURA DE ARCHIVOS                                      │
└─────────────────────────────────────────────────────────────┘

proyecto/
├── config/
│   ├── procesamiento.py         # Configs estáticas de procesamiento
│   ├── descarga.py              # Configs estáticas de descarga
│   └── __init__.py              # Re-exporta gestores
├── utils/
│   ├── procesamiento_manager.py # Gestor de procesamiento
│   ├── descarga_manager.py      # Gestor de descarga
│   ├── procesador.py            # Lógica de procesamiento
│   └── __init__.py              # Exporta todo
└── .env                         # Credenciales compartidas


┌─────────────────────────────────────────────────────────────┐
│  ¿CUÁNDO EDITAR CADA ARCHIVO?                               │
└─────────────────────────────────────────────────────────────┘

📊 config/procesamiento.py
   └─ Cambiar rutas de archivos CSV o Excel

🌐 config/descarga.py
   └─ Cambiar navegador, timeouts, o configs de Selenium

🔒 .env
   └─ Cambiar credenciales o URL del sitio web

🔧 utils/procesamiento_manager.py
   └─ Modificar lógica de fechas automáticas o validaciones

🔧 utils/descarga_manager.py
   └─ Modificar validaciones de credenciales o Selenium


┌─────────────────────────────────────────────────────────────┐
│  PREGUNTAS FRECUENTES                                        │
└─────────────────────────────────────────────────────────────┘

Q: ¿Puedo usar solo el módulo de procesamiento?
A: Sí, es completamente independiente. Solo importa procesamiento_config.

Q: ¿Puedo usar solo el módulo de descarga?
A: Sí, es completamente independiente. Solo importa descarga_config.

Q: ¿Por qué hay dos gestores separados?
A: Porque son módulos independientes. Cada uno maneja sus propias configs.

Q: ¿Dónde cambio las rutas de mis archivos?
A: En config/procesamiento.py

Q: ¿Dónde configuro Selenium?
A: En config/descarga.py

Q: ¿Dónde pongo mis credenciales?
A: En .env (compartido entre módulos que lo necesiten)

Q: ¿Cómo cambio la lógica de las fechas?
A: Edita los métodos estáticos en utils/procesamiento_manager.py

Q: ¿Por qué no hay un config_manager.py general?
A: Porque queremos módulos independientes. No necesitas un gestor
   central cuando cada módulo puede gestionar sus propias configs.

Q: Si agrego un tercer módulo, ¿qué debo crear?
A: 1. config/nuevo_modulo.py (configuraciones)
   2. utils/nuevo_modulo_manager.py (gestor)
   3. Exportar en utils/__init__.py
"""

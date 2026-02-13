# Determinar Porcentajes

Este proyecto contiene un código en Python que automatiza la descarga y procesamiento de datos de boyas oceanográficas. El programa calcula la cantidad de datos esperada y la cantidad de datos recibidos, permitiendo así verificar la integridad y completitud de los datos procesados.

## ✨ Características

- **Descarga automatizada:** Descarga datos desde una página web usando Selenium (con autenticación)
- **Procesamiento inteligente:** Lee automáticamente todos los archivos `.csv` y los organiza por nombre de boya
- **Análisis de completitud:** Compara datos esperados vs datos recibidos para cada variable
- **Exportación a Excel:** Genera reportes en formato Excel con los resultados del análisis
- **Configuración flexible:** Todas las configuraciones centralizadas y fáciles de modificar

## 📁 Estructura del Proyecto

```
determinar_porcentajes/
├── main.py                          # Orquestador principal
├── config/                          # Configuraciones por módulo
│   ├── procesamiento.py            # ⚙️ Configs de procesamiento
│   ├── descarga.py                 # 🌐 Configs de descarga
│   └── __init__.py
├── utils/                           # Utilidades y gestores
│   ├── procesamiento_manager.py    # 🔧 Gestor de procesamiento
│   ├── descarga_manager.py         # 🔧 Gestor de descarga
│   ├── procesador.py               # 📊 Lógica de procesamiento
│   └── __init__.py
├── pages/                           # Page Object Model (Selenium)
│   └── (por implementar)
├── downloads/                       # Archivos descargados
├── .env                             # 🔒 Credenciales (NO compartir)
├── .env.example                    # Plantilla de credenciales
├── ARQUITECTURA_CONFIG.md          # 📖 Documentación detallada
└── requirements.txt                # Dependencias
```

> 💡 **Ver [ARQUITECTURA_CONFIG.md](ARQUITECTURA_CONFIG.md)** para entender cómo funcionan las configuraciones.

## 🚀 Instalación


Se recomienda utilizar un ambiente virtual para evitar conflictos con otras dependencias de Python. Siga los siguientes pasos:

1. **Cree el ambiente virtual:**

   En Windows:
   ```powershell
   python -m venv venv
   ```
   En macOS/Linux:
   ```bash
   python3 -m venv venv
   ```

2. **Active el ambiente virtual:**

   En Windows:
   ```powershell
   .\venv\Scripts\activate
   ```
   En macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. **Instale las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuración

### 1. Configurar credenciales (archivo .env)

```bash
# Copia el archivo de ejemplo
copy .env.example .env

# Edita .env con tus credenciales reales
notepad .env
```

**Importante:** El archivo `.env` contiene credenciales sensibles y NO debe ser compartido ni subido a Git.

### 2. Configurar parámetros del proyecto

**Para el módulo de procesamiento:**

Edita [config/procesamiento.py](config/procesamiento.py) para ajustar:
- Rutas donde están los archivos CSV
- Rutas donde guardar los resultados Excel

**Para el módulo de descarga:**

Edita [config/descarga.py](config/descarga.py) para ajustar:
- Navegador a usar (Chrome, Firefox, Edge)
- Modo headless
- Timeouts y reintentos

**Nota:** Las fechas se calculan automáticamente:
- **Fecha inicial:** Primer día del mes actual a las 00:00:00
- **Fecha final:** Día actual a las 21:59:59
- **Nombre del archivo:** Se genera automáticamente basado en las fechas

Si necesitas fechas personalizadas, puedes modificar las funciones en `utils/procesamiento_manager.py`.

## 💻 Uso

### Ejecutar el proceso completo (descarga + procesamiento)

```bash
python main.py
```

### Ejecutar solo el módulo de procesamiento

```bash
python procesar.py
```

Este comando ejecutará únicamente:
- Procesamiento de archivos CSV existentes
- Generación del reporte Excel

### Ejecutar solo el módulo de descarga

```bash
python descargar.py
```

Este comando ejecutará únicamente:
- Descarga de datos desde la web (cuando esté implementado)

### Usar desde Jupyter Notebook

**Para procesamiento:**
```python
from utils import procesamiento_config
from utils.procesador import procesar_datos_boyas

df = procesar_datos_boyas(
    ruta_a_carpeta=procesamiento_config.RUTA_DATOS_CRUDOS,
    fecha_inicial=procesamiento_config.FECHA_INICIAL,
    fecha_final=procesamiento_config.FECHA_FINAL,
    ruta_guardado=procesamiento_config.RUTA_GUARDADO,
    nombre_salida=procesamiento_config.NOMBRE_EXCEL_SALIDA
)
```

**Para descarga:**
```python
from utils import descarga_config
# TODO: Implementar lógica de descarga
```

## 📊 Funcionalidades

### Procesamiento de Datos

El módulo procesa automáticamente:
- **Viento:** Datos de velocidad y dirección del viento
- **Oleaje:** Altura, periodo y dirección de las olas
- **Corriente:** Velocidad y dirección de corrientes marinas
- **MCT:** Datos de salinidad y temperatura

### Análisis de Completitud

Para cada variable, el sistema calcula:
- Cantidad de datos esperados (basado en el intervalo temporal)
- Cantidad de datos recibidos (datos válidos no nulos)
- Porcentaje de completitud

## 🔒 Seguridad

- ✅ Credenciales protegidas en archivo `.env`
- ✅ `.env` incluido en `.gitignore`
- ✅ Plantilla `.env.example` para referencia
- ⚠️ **NUNCA** subas el archivo `.env` a repositorios públicos

## 📝 Requisitos

- Python 3.14.2

Asegúrese de tener instalada la versión 3.14.2 de Python para garantizar la compatibilidad del código.

## Uso

Ejecute el código principal siguiendo las instrucciones del archivo `main.ipynb` o utilizando los scripts proporcionados.

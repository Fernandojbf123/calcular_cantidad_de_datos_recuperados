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
├── main.py                          # Orquestador principal (descarga + procesamiento)
├── download/                        # 🌐 Módulo de descarga
│   ├── main_download.py            # Entry point de descarga
│   ├── orquestador.py              # Orquestador de descarga
│   ├── pages/                      # Page Object Model (Selenium)
│   │   ├── login_page.py           # Página de login
│   │   ├── dinamic_dashboard_page.py # Página de dashboard
│   │   └── download_page.py        # Página de descarga
│   ├── services/                   # Lógica de negocio de descarga
│   │   ├── login_service.py
│   │   ├── dinamic_dashboard_service.py
│   │   └── download_service.py
│   └── drivers/                    # Gestión de WebDriver
│       └── driver_manager.py
├── processing/                      # 📊 Módulo de procesamiento
│   ├── main_processing.py          # Entry point de procesamiento
│   ├── orquestador.py              # Orquestador de procesamiento
│   └── services/
│       └── procesador.py           # Lógica de procesamiento
├── config/                          # ⚙️ Configuraciones
│   ├── download_settings.py        # Configs de descarga
│   ├── process_settings.py         # Configs de procesamiento
│   ├── settings_manager.py         # Gestores (DescargaManager, ProcessManager)
│   └── __init__.py
├── utils/                           # Utilidades compartidas
│   ├── descarga_manager.py         # (Deprecated - ver config/settings_manager.py)
│   ├── procesamiento_manager.py    # (Deprecated - ver config/settings_manager.py)
│   └── procesador.py               # Funciones de procesamiento
├── downloads/                       # 📁 Archivos descargados
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

Edita [config/process_settings.py](config/process_settings.py) para ajustar:
- `RUTA_DATOS_CRUDOS` - Ruta donde están los archivos CSV
- `RUTA_GUARDADO` - Ruta donde guardar los resultados Excel
- `MES_ESTUDIO` - Mes específico a procesar (1-12) o None para mes actual
- `DIA_INICIAL` - Día inicial del periodo (default: 1)
- `HORA_FINAL` - Hora final del periodo (default: 21)
- `MINUTOS_FINAL` - Minutos finales del periodo (default: 59)

**Para el módulo de descarga:**

Edita [config/download_settings.py](config/download_settings.py) para ajustar:
- `NAVEGADOR` - Navegador a usar ("chrome", "firefox", "edge")
- `HEADLESS_MODE` - Ejecutar sin ventana visible (True/False)
- `CARPETA_DESCARGAS` - Carpeta donde guardar archivos descargados
- `TIMEOUT_DESCARGA` - Tiempo máximo de espera
- `MAX_REINTENTOS` - Número de reintentos en caso de error

**Nota:** Las fechas se calculan automáticamente:
- **Fecha inicial:** Basada en MES_ESTUDIO y DIA_INICIAL (default: primer día del mes actual a las 00:00:00)
- **Fecha final:** Día actual con la hora configurada (default: día actual a las 21:59:59)
- **Nombre del archivo:** Se genera automáticamente basado en las fechas

La lógica de fechas está en `config/settings_manager.py` (clase ProcessManager).

## 💻 Uso

### Ejecutar el proceso completo (descarga + procesamiento)

```bash
python main.py
```

### Ejecutar solo el módulo de procesamiento

```bash
python processing/main_processing.py
```

Este comando ejecutará únicamente:
- Procesamiento de archivos CSV existentes
- Generación del reporte Excel

### Ejecutar solo el módulo de descarga

```bash
python download/main_download.py
```

Este comando ejecutará únicamente:
- Descarga automatizada de datos desde la web usando Selenium
- Navegación y login en el sistema
- Descarga de archivos de boyas BMT y BOT

### Usar desde Jupyter Notebook

**Para procesamiento:**
```python
from processing.orquestador import run_processing

# Ejecutar procesamiento completo
df = run_processing()
```

**Para usar el gestor de configuración:**
```python
from config.settings_manager import ProcessManager

# Ver configuración actual
ProcessManager.mostrar_configuracion()

# Obtener fechas calculadas
fecha_inicio = ProcessManager.get_starting_date()
fecha_fin = ProcessManager.get_ending_date()
print(f"Procesando desde {fecha_inicio} hasta {fecha_fin}")
```

**Para descarga:**
```python
from download.orquestador import run_download

# Ejecutar descarga completa
run_download()
```

**Para usar el gestor de descarga:**
```python
from config.settings_manager import DescargaManager

# Ver configuración actual
DescargaManager.mostrar_configuracion()

# Validar credenciales
if DescargaManager.validar_credenciales():
    print("✅ Credenciales configuradas correctamente")
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
- Selenium WebDriver
- Pandas 3.0.0
- Chrome/Firefox/Edge (para el módulo de descarga)

Asegúrese de tener instalada la versión 3.14.2 de Python para garantizar la compatibilidad del código. Todas las dependencias están listadas en `requirements.txt`.

# Determinar Porcentajes

Este proyecto contiene un código en Python que carga datos desde un archivo en formato CSV. El programa calcula la cantidad de datos esperada y la cantidad de datos recibidos, permitiendo así verificar la integridad y completitud de los datos procesados.

Además, este archivo busca y lee automáticamente todos los archivos `.csv` que se encuentren en la ruta de destino y los ordena por nombre de boya. Si solo se desean cargar datos de dos boyas, entonces en la carpeta solo deben estar los archivos `.csv` correspondientes a esas dos boyas. Las variables que no estén disponibles para esas boyas se colocarán en cero automáticamente.

## Descripción

- **Carga de datos:** El código lee archivos CSV para procesar la información contenida.
- **Cálculo de datos esperados y recibidos:** Se determina cuántos datos deberían estar presentes y cuántos realmente se han recibido, facilitando la validación de los datos.

## Instalación


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

## Requisitos

- Python 3.14.2

Asegúrese de tener instalada la versión 3.14.2 de Python para garantizar la compatibilidad del código.

## Uso

Ejecute el código principal siguiendo las instrucciones del archivo `main.ipynb` o utilizando los scripts proporcionados.

# 🧠 Easy OCR Reader

Una herramienta simple para aplicar OCR (Reconocimiento Óptico de Caracteres) sobre imágenes usando [EasyOCR](https://github.com/JaidedAI/EasyOCR). Ideal para extraer texto desde cualquier imagen local.

## 🔧 Requisitos

- Python 3.8 o superior
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- OpenCV
- Matplotlib

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## ⚡ Instalación rápida
1. Clona este repositorio:
   ```bash
   git clone https://github.com/TheGatoSamurai/Easy-OCR-Reader
   cd Easy-OCR-Reader
   ```
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   .venv/Scripts/activate  # En Windows
   source .venv/bin/activate  # En Linux/Mac
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## 🖼️ Uso

Ejecuta el script principal para procesar todas las imágenes en la carpeta `images`:

```bash
python main.py
```

Puedes agregar tus imágenes en la carpeta `images/` (formatos soportados: .jpg, .jpeg, .png).

## 📋 Ejemplo de salida

```
Procesando imagen: images/auto1.jpg
Resultados OCR:
Texto: ABC123, Confianza: 98.76%
Texto: 2025, Confianza: 87.45%
...
```

## 🪟 Nota para usuarios de Windows

Si ves el error:
```
Microsoft Visual C++ Redistributable is not installed, this may lead to the DLL load failure.
```
Descarga e instala el [Microsoft Visual C++ Redistributable](https://aka.ms/vs/16/release/vc_redist.x64.exe) y reinicia tu PC.

## 🛠️ Solución de problemas

- **No se encuentra el módulo torch o c10.dll:**
  - Instala el Visual C++ Redistributable como se indica arriba.
  - Reinstala los paquetes:
    ```bash
    pip install --force-reinstall torch easyocr
    ```
- **No se detectan imágenes:**
  - Verifica que tus archivos estén en la carpeta `images/` y tengan extensión .jpg, .jpeg o .png.

## 📚 Recursos

- [EasyOCR Docs](https://github.com/JaidedAI/EasyOCR)
- [OpenCV Docs](https://docs.opencv.org/)
- [Matplotlib Docs](https://matplotlib.org/)

## ✨ Autor

- [Soy Gerald, conocido en línea como thegatosamurai 🐱🥷](https://github.com/TheGatoSamurai)

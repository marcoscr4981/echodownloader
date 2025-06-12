# EchoDownloader

## Tabla de contenidos

- [01 Descripción](#01-descripción)
- [02 Instalación](#02-instalación)
- [03 Uso](#03-uso)
- [04 Estructura del proyecto](#04-estructura-del-proyecto)
- [05 Autor](#05-autor)
- [06 Licencia](#06-licencia)

## 01 Descripción

**EchoDownloader** es una herramienta de línea de comandos escrita en Python que permite descargar el audio de uno o varios vídeos de YouTube en formato `.mp3`, utilizando la potente librería `yt_dlp`. Ideal para crear tu biblioteca offline de música o podcasts.

- **Versión:** v1.0  
- **Última revisión:** 12/06/2025

### Características

- Descarga en formato MP3 con calidad de 192 kbps.
- Permite introducir una URL directamente o pasar un archivo con múltiples URLs.
- Interfaz de consola limpia, con mensajes informativos y de error personalizados.
- Gestión de errores clara y controlada.
- Compatible con Linux, macOS y Windows.

### Requisitos

- Python 3.10 o superior
- FFmpeg (instalado y disponible en la línea de comandos)
- Recomendado: entorno virtual con `venv`

[Subir](#)

## 02 Instalación

```bash
git clone https://github.com/marcoscr4981/echodownloader.git
cd echodownloader
pip install -r requirements.txt
```

> Recuerda tener instalado `ffmpeg`.

[Subir](#)

## 03 Uso

### Descargar desde una sola URL

```bash
python -m echodownloader -u "https://www.youtube.com/watch?v=XXXXX"
```

### Descargar desde un archivo `.txt``

```bash
python -m echodownloader -f urls.txt
```

- El archivo debe contener una URL por línea.
- Puedes incluir un retraso entre descargas con `-d`:
  ```bash
  python -m echodownloader -f urls.txt -d 3
  ```

[Subir](#)

## 04 Estructura del proyecto

```text
echodownloader/
├── cli.py                # Gestión de línea de comandos
├── core.py               # Lógica principal de descarga
├── __main__.py           # Punto de entrada principal
├── config.py             # Información del proyecto
├── model/
│   ├── parser.py         # ArgumentParser personalizado
│   └── echomedia.py      # Modelo de datos del vídeo
├── utils/
│   ├── files.py          # Lectura/validación de URLs
│   └── yt_tools.py       # Integración con yt_dlp
├── view/
│   └── display.py        # Mensajes y salida por consola
└── exceptions/
    └── exceptions.py     # Excepciones personalizadas
```

[Subir](#)

## 05 Autor

- **Nombre:**  Marcos Cuadrado Rey
- **Email:**  [marcoscr4981@gmail.com](mailto:marcoscr4981@gmail.com)
- **GitHub:**  [https://github.com/marcoscr4981](https://github.com/marcoscr4981)

[Subir](#)

## 06 Licencia

- **Licencia:** MIT

[Subir](#)

---

> Última actualización: 12 de Junio de 2025
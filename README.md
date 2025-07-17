# EchoDownloader

## Tabla de contenidos

- [01 Descripción](#01-descripción)
- [02 Instalación](#02-instalación)
- [03 Uso](#03-uso)
- [04 Estructura del proyecto](#04-estructura-del-proyecto)
- [05 Autor](#05-autor)
- [06 Licencia](#06-licencia)

## 01 Descripción

**EchoDownloader** es una herramienta de línea de comandos escrita en Python que permite descargar el audio de uno o varios vídeos de YouTube en formato `.mp3`, utilizando la librería `yt_dlp`. Ideal para crear tu biblioteca offline de música o podcasts.

- **Versión:** v1.1 
- **Última revisión:** 17/07/2025

### Actualizaciones

- Muestra los diferentes mensajes por consola con colores.
- Parsea las diferentes URLs de YouTube.
- Contador de descargas, tanto correctas como erróneas.
- Mejoras en el archivo README.md

### Características

- Descarga en formato MP3 con calidad de 192 kbps.
- Permite introducir una URL directamente o pasar un archivo con múltiples URLs.
- Interfaz de consola limpia, con mensajes informativos y de error personalizados.
- Gestión de errores clara y controlada.
- Compatible con Linux, Mac OS y Windows.

### Requisitos

- Python 3.10 o superior
- FFmpeg (instalado y disponible en la línea de comandos)
- Recomendado: entorno virtual con `venv`

### Librerías externas

- **colored:** Añade color y formato al texto en la consola.
- **yt_dlp:** Librería para la descarga de videos y audio de diversos sitios web, como YouTube y Vimeo.

[Subir](#)

## 02 Instalación

```bash
git clone https://github.com/marcoscr4981/echodownloader.git
cd echodownloader
# Para crear el entorno virtual: python -m venv <nombre_entorno>
pip install -r requirements.txt
```

> Recuerda tener instalado `ffmpeg`.

[Subir](#)

## 03 Uso

Si se utiliza un entorno virtual, acuérdate de activarlo:

```bash
# Sistemas Windows
.\<nombre_entorno>\Scripts\activate

# Sistemas Linux/Mac OS
source <nombre_entorno>/bin/activate
```

> Para desactivar el entorno virtual:
> ```bash
> deactivate
>```

### Descargar desde una sola URL

```bash
python -m echodownloader -u "https://www.youtube.com/watch?v=XXXXX"
```

> Al pasar una URL como argumento, siempre enciérrala entre comillas `"` para evitar errores del sistema operativo o del intérprete de comandos.

### Descargar desde un archivo `.txt``

```bash
python -m echodownloader -f urls.txt
```

- El archivo debe contener una URL por línea.
- Puedes incluir un retraso entre descargas con el parámetro `-d`:
  ```bash
  python -m echodownloader -f urls.txt -d 3
  ```

### Ver la ayuda de la aplicación

```bash
python -m echodownloader -h
```

### Ver la versión de la aplicación

```bash
python -m echodownloader -v
```

[Subir](#)

## 04 Estructura del proyecto

```text
EchoDownloader
├──echodownloader/
│     ├── cli.py                # Gestión de línea de comandos
│     ├── core.py               # Lógica principal de descarga
│     ├── __main__.py           # Punto de entrada principal
│     ├── config.py             # Información del proyecto
│     ├── model/
│     │   ├── parser.py         # ArgumentParser personalizado
│     │   └── echomedia.py      # Modelo de datos del vídeo
│     ├── utils/
│     │   ├── files.py          # Lectura/validación de URLs
│     │   ├── screen_colors.py  # Tipos de colores a utilizar en la consola
│     │   ├── youtube_parse.py  # Parsea las distitntas URLS de YouTube
│     │   └── yt_tools.py       # Integración con yt_dlp
│     ├── view/
│     │   └── display.py        # Mensajes y salida por consola
│     └── exceptions/
│         └── exceptions.py     # Excepciones personalizadas
│
├── LICENSE.txt                 # Licencia del proyecto (MIT)
├── README.txt                  # Instrucciones del proyecto
└── requirements.txt            # Archivo de librerias que se han de instalar
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

> Última actualización: 16 de Julio de 2025
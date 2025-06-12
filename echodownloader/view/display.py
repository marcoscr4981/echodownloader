"""Módulo encargado de mostrar mensajes informativos, de error y progreso
en la interfaz de línea de comandos de la aplicación.
"""
import os
import os.path
from typing import Optional

from ..config import PROJECT_NAME, VERSION_PROJECT
from ..model.echomedia import EchoMedia

def barnner() -> None:
    """Limpia la consola y muestra el banner del proyecto con su versión."""
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{PROJECT_NAME} {VERSION_PROJECT}\n")


def clear_line() -> None:
    """Elimina la línea actual de la terminal (para actualizar información en pantalla)."""
    print("\033[2K", end="\r")


def show_fetching_info(echomedia:EchoMedia) -> None:
    """Muestra un mensaje indicando que se está obteniendo la información del video.

    Args:
        media (EchoMedia): Objeto con la URL del video.
    """
    print(f"[i] [Obteniendo información] {echomedia.url}", end='\r')


def show_downloading(echomedia:EchoMedia) -> None:
    """Muestra un mensaje de progreso mientras se descarga el audio del video.

    Args:
        media (EchoMedia): Objeto con la URL y ruta de descarga del audio.
    """
    clear_line()

    if echomedia.download_path is not None:
        print(f"[i] [Descargando] {echomedia.url} ({os.path.basename(echomedia.download_path)}.mp3)", end='\r')


def show_download_complete(echomedia:EchoMedia) -> None:
    """Muestra un mensaje indicando que la descarga se ha completado correctamente.

    Args:
        media (EchoMedia): Objeto con la URL y ruta del archivo descargado.
    """
    clear_line()

    if echomedia.download_path is not None:
        print(f"[*] [Completado] {echomedia.url} ({os.path.basename(echomedia.download_path)}.mp3)")


def show_error(msg:str, echomedia:Optional[EchoMedia] = None) -> None:
    """
    Muestra un mensaje de error personalizado. Si se proporciona un objeto media, se añade la URL asociada.

    Args:
        message (str): Descripción del error.
        media (Optional[EchoMedia]): Objeto con la URL del video (opcional).
    """
    print("\033[2K", end="\r")

    if echomedia is not None:
        print(f"[!] [Error] {msg} ({echomedia.url})")
    else:
        print(f"\n[!] [Error] {msg}")
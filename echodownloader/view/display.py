"""Módulo encargado de mostrar mensajes informativos, de error y progreso
en la interfaz de línea de comandos de la aplicación.
"""
import os
import os.path
from typing import Optional

from ..config import PROJECT_NAME, VERSION_PROJECT
from ..model.echomedia import EchoMedia
from ..utils.screen_colors import COMPLETED_COLOR, ERROR_COLOR, INFO_COLOR, RESET_COLOR, RUNNING_COLOR

def barnner() -> None:
    """Limpia la consola y muestra el banner del proyecto con su versión."""
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"{RUNNING_COLOR}{PROJECT_NAME} {VERSION_PROJECT}\n{RESET_COLOR}")


def clear_line() -> None:
    """Elimina la línea actual de la terminal (para actualizar información en pantalla)."""
    print("\033[2K", end="\r")


def show_fetching_info(echomedia:EchoMedia) -> None:
    """Muestra un mensaje indicando que se está obteniendo la información del video.

    Args:
        media (EchoMedia): Objeto con la URL del video.
    """
    print(f"{INFO_COLOR}[i] [Obteniendo información] {echomedia.url}{RESET_COLOR}", end='\r')


def show_downloading(echomedia:EchoMedia) -> None:
    """Muestra un mensaje de progreso mientras se descarga el audio del video.

    Args:
        media (EchoMedia): Objeto con la URL y ruta de descarga del audio.
    """
    clear_line()

    if echomedia.download_path is not None:
        print(f"{INFO_COLOR}[i] [Descargando] {echomedia.url} ({os.path.basename(echomedia.download_path)}.mp3){RESET_COLOR}", end='\r')


def show_download_complete(echomedia:EchoMedia) -> None:
    """Muestra un mensaje indicando que la descarga se ha completado correctamente.

    Args:
        media (EchoMedia): Objeto con la URL y ruta del archivo descargado.
    """
    clear_line()

    if echomedia.download_path is not None:
        print(f"{COMPLETED_COLOR}[*] [Completado] {echomedia.url} ({os.path.basename(echomedia.download_path)}.mp3){RESET_COLOR}")


def show_error(msg:str, echomedia:Optional[EchoMedia] = None) -> None:
    """Muestra un mensaje de error personalizado. Si se proporciona un objeto media, se añade la URL asociada.

    Args:
        message (str): Descripción del error.
        media (Optional[EchoMedia]): Objeto con la URL del video (opcional).
    """
    print("\033[2K", end="\r")

    if echomedia is not None:
        print(f"{ERROR_COLOR}[!] [Error] {msg} ({echomedia.url}){RESET_COLOR}")
    else:
        print(f"\n{ERROR_COLOR}[!] [Error] {msg}{RESET_COLOR}")


def show_summary(sumary:dict) -> None:
    """Muestra el resumen de las descargas múltiples con su resultado (descargas correctas o incorrectas).

    Args:
        sumary (dict): Diccionario con los resultados de las descargas ('downloads', 'completed', 'incorrect').
    """
    ident = " ".rjust(5)

    print(f"\n{INFO_COLOR}[*] Descargas:{RESET_COLOR} {sumary['downloads']}{ident}{COMPLETED_COLOR}Completadas:{RESET_COLOR} {sumary['completed']}{ident}{ERROR_COLOR}Erróneas:{RESET_COLOR} {sumary['incorrect']}")
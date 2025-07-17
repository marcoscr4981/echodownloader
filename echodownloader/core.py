"""Módulo que gestiona la lógica principal de la aplicación para la descarga de audios desde YouTube."""
import sys
import time

from .exceptions import EmptyDataException, YouTubeException
from .model.echomedia import EchoMedia
from .utils.files import read_urls_from_file, generate_unique_file_path
from .utils.youtube_parse import parse_url
from .utils.yt_tools import download_mp3, fetch_video_title
from .view.display import *


def download_youtube_url(url:str, youtube_file:bool = False) -> None:
    """Descarga el audio en formato MP3 de un video de YouTube dado su URL.

    Args:
        url (str): URL del video de YouTube.
        show_banner (bool): Si se debe mostrar el banner del programa.

    Raises:
        YouTubeException: Si ocurre un error al obtener información o al descargar.
    """
    if url is None:
        print(f"\n[!] No se ha proporcionado como argumento la URL.\n")
        sys.exit(1)

    if youtube_file:
        barnner()
    
    try:
        url = parse_url(url)

        media = EchoMedia(url)

        show_fetching_info(media)
        title = fetch_video_title(media)

        media.download_path = generate_unique_file_path(title, '.mp3')
        show_downloading(media)
        
        download_mp3(media)
        show_download_complete(media)
    except YouTubeException as ex:
        if youtube_file:
            raise YouTubeException(str(ex))
        else:
            show_error(str(ex), media)
    

def download_youtube_file(file_path:str, delay:float = 5) -> None:
    """Descarga múltiples audios desde una lista de URLs contenida en un archivo de texto.

    Args:
        file_path (str): Ruta al archivo de texto con URLs (una por línea).
        delay (float): Tiempo de espera entre descargas (en segundos).

    Raises:
        EmptyDataException: Si no se proporciona una ruta válida.
        YouTubeException: Si ocurre un error durante la descarga de algún video.
    """
    if file_path is None:
        print(f"\n[!] No se ha proporcionado la ruta al archivo como argumento.\n")
        sys.exit(1)

    barnner()

    sumary = {
        'downloads': 0,
        'completed': 0,
        'incorrect': 0
    }

    try:
        url_list = read_urls_from_file(file_path)
    except EmptyDataException as ex:
        show_error(str(ex))
    except Exception:
        show_error("Se ha producido un error al acceder al archivo proporcionado")
        print("\n")
        sys.exit(1)

    for url in url_list:
        try:
            download_youtube_url(url, youtube_file=True)
            sumary['completed'] += 1
            time.sleep(delay)
        except (EmptyDataException, YouTubeException) as ex:
            show_error(str(ex))
            sumary['incorrect'] += 1
        except Exception:
            show_error(f"Se ha producido un error al acceder a la URL {url}")
            sumary['incorrect'] += 1

    sumary['downloads'] = sumary['completed'] + sumary['incorrect']

    show_summary(sumary)
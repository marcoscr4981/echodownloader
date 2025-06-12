"""Módulo de herramientas para interacción con YouTube mediante 'yt_dlp'."""
from yt_dlp import YoutubeDL

from ..model.echomedia import EchoMedia
from ..exceptions import YouTubeException

ERROR_INVALID_URL = "La URL es inválida o no está accesible."
ERROR_NO_TITLE = "No se pudo obtener el título del video."
ERROR_NO_PATH = "No se ha definido la ruta de descarga."

class SilentLogger:
    """Logger que suprime la salida estándar de yt_dlp."""
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass


def fetch_video_title(echomedia:EchoMedia) -> str:
    """Obtiene el título del video de YouTube a partir de su URL.

    Args:
        media (EchoMedia): Objeto que contiene la URL del video.

    Returns:
        str: Título del video.

    Raises:
        YouTubeException: Si no se puede acceder al video o no se encuentra el título.
    """
    ydl_opts = {
        'quiet': True,
        'logger': SilentLogger(),
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(echomedia.url, download=False)

            if info is None or 'title' not in info:
                raise YouTubeException(ERROR_NO_TITLE)
            
            return info['title']
        except Exception as ex:
            raise YouTubeException(ERROR_INVALID_URL)
        

def download_mp3(echomedia:EchoMedia) -> None:
    """Descarga el audio del video de YouTube en formato MP3.

    Args:
        media (EchoMedia): Objeto que contiene la URL del video y la ruta de descarga.

    Raises:
        YouTubeException: Si ocurre un error durante la descarga o falta la ruta.
    """
    if not echomedia.download_path:
        raise YouTubeException(ERROR_NO_PATH)
    
    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'noplaylist': True,
        'outtmpl': echomedia.download_path,
        'quiet': True,
        'no_warnings': True,
        'progress_hooks': [],
        'logger': SilentLogger(),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([echomedia.url])
        except Exception as ex:
            raise YouTubeException(ERROR_INVALID_URL)
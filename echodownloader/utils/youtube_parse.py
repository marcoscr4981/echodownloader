"""Módulo que parsea las diferentes URLs de YouTube."""
from urllib.parse import urlparse, parse_qs

from ..exceptions import YouTubeException

def parse_url(url:str) -> str:
    """Parsea los distintos tipos de URLs de YouTube.

    Args:
        url (str): URL a parsear.

    Returns:
        str: URL parseada.

    Raises:
        YouTubeException: Si el dominio de la URL aportada no lo reconoce o no se puede extraer el ID del video.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url

    parsed = urlparse(url)

    domain = parsed.netloc.replace('www.', '')

    if domain in ('youtube.com', 'm.youtube.com'):
        query_params = parse_qs(parsed.query)
        video_id = query_params.get('v', [None])[0]
    elif domain == 'youtu.be':
        video_id = parsed.path.lstrip('/')
    else:
        raise YouTubeException(f"Dominio de YouTube no reconocido: {parsed.netloc}")
    
    if not video_id:
        raise YouTubeException("No se pudo extraer el ID del video de la URL")
    
    return f"https://www.youtube.com/watch?v={video_id}"
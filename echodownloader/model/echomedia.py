"""Módulo que define la clase EchoMedia para representar un medio de YouTube a descargar."""
from typing import Optional

class EchoMedia:
    """Representa un medio de YouTube con su URL y la ruta de descarga asociada."""

    def __init__(self, url:str) -> None:
        """Inicializa una instancia de EchoMedia con la URL dada.

        Args:
            url (str): URL del video de YouTube.
        """
        self._url = url
        self._download_path:Optional[str] = None


    @property
    def url(self) -> str:
        """Devuelve la URL del video.

        Returns:
            str: URL del video de YouTube.
        """
        return self._url
    

    @url.setter
    def url(self, url:str) -> None:
        """Establece una nueva URL para el video y resetea la ruta de descarga.

        Args:
            url (str): Nueva URL del video de YouTube.
        """
        self._url = url
        self._download_path = None


    @property
    def download_path(self) -> Optional[str]:
        """Devuelve la ruta local donde se guardará el archivo descargado.

        Returns:
            Optional[str]: Ruta local del archivo descargado o None si no está definida.
        """
        return self._download_path
    

    @download_path.setter
    def download_path(self, download_path:str) -> None:
        """Establece la ruta local donde se guardará el archivo descargado.

        Args:
            download_path (str): Ruta local del archivo.
        """
        self._download_path = download_path
        
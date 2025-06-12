"""Módulo donde se definen las excepciones personalizadas para la aplicación."""
from typing import Optional


class EmptyDataException(Exception):
    """Excepción lanzada cuando no se proporciona un dato obligatorio.

    Attributes:
        message (str): Mensaje que se mostrará al usuario.
    """
    def __init__(self, message:Optional[str] = "El campo está vacío") -> None:
        super().__init__(message)


class YouTubeException(Exception):
    """Excepción lanzada al producirse un error al acceder a YouTube.

    Attributes:
        message (str): Mensaje que se mostrará al usuario.
    """
    def __init__(self, message:Optional[str] = "Se ha producido un error al conectar con YouTube") -> None:
        super().__init__(message)
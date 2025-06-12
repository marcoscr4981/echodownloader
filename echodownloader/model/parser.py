"""Parser personalizado basado en argparse, con mensajes de ayuda, introducción y errores definidos por el usuario."""
import argparse
from ..config import *


class Parser(argparse.ArgumentParser):
    """Extiende argparse.ArgumentParser para mostrar mensajes personalizados de ayuda y error."""

    def print_help(self) -> None:
        """Imprime el mensaje de introducción seguido de las opciones de ayuda."""
        self.intro()
        self.options()


    def intro(self) -> None:
        """Muestra un mensaje introductorio con detalles del proyecto."""
        print(f"[{PROJECT_NAME}]")
        print(f"\nVersión: {VERSION_PROJECT} ({PROJECT_DATE})")
        print(f"Autor: {AUTHOR_NAME} ({WEB})\n")


    def options(self) -> None:
        """Muestra los argumentos disponibles y su descripción."""
        ident = " ".rjust(5)

        print("Descarga el audio de un video de YouTube en formato mp3.\n")
        print(f"{ident}-u / --url <url_youtube>")
        print(f"{ident}-f / --file <archivo_urls> [-d / --delay <segundos>] (El archivo debe contener una URL por línea)")
        print(f"{ident}-v / --version")
        print(f"{ident}-h / --help\n")
        print("Librería utilizada: yt_dlp\n")


    def error(self, message: str) -> None:
        """Muestra un mensaje de error personalizado cuando se proporciona un argumento no válido.

        Args:
            message (str): Mensaje de error generado por argparse.
        """
        custom_message = (
            "\n[!] Argumento no válido\n"
            f"{' '.rjust(4)}Detalle: {message}\n"
            f"{' '.rjust(4)}Para más ayuda: python3 echodownloader --help\n\n"
        )
        self.exit(2, custom_message)

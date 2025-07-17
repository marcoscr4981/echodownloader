"""Parser personalizado basado en argparse, con mensajes de ayuda, introducción y errores definidos por el usuario."""
import argparse

from ..config import *
from ..utils.screen_colors import INFO_COLOR, RESET_COLOR, RUNNING_COLOR

class Parser(argparse.ArgumentParser):
    """Extiende argparse.ArgumentParser para mostrar mensajes personalizados de ayuda y error."""

    def print_help(self) -> None:
        """Imprime el mensaje de introducción seguido de las opciones de ayuda."""
        self.intro()
        self.options()


    def intro(self) -> None:
        """Muestra un mensaje introductorio con detalles del proyecto."""
        print(f"\n{RUNNING_COLOR}[{PROJECT_NAME}]{RESET_COLOR}")
        print(f"\n{INFO_COLOR}Versión:{RESET_COLOR} {VERSION_PROJECT} ({PROJECT_DATE})")
        print(f"{INFO_COLOR}Autor:{RESET_COLOR} {AUTHOR_NAME} ({WEB})\n")


    def options(self) -> None:
        """Muestra los argumentos disponibles y su descripción."""
        ident = " ".rjust(5)

        print(f"{INFO_COLOR}Descarga el audio de un video de YouTube en formato MP3\n{RESET_COLOR}")
        print(f"{ident}{INFO_COLOR}-u, --url <url_youtube>{RESET_COLOR}           URL del video de YouTube (entrecomillada)")
        print(f"{ident}{INFO_COLOR}-f, --file <archivo_urls>{RESET_COLOR}         Archivo de texto con una URL por línea")
        print(f"{ident*2}{INFO_COLOR}-d, --delay <segundos>{RESET_COLOR}          (Opcional) Espera entre descargas, solo con -f/--file")
        print(f"{ident}{INFO_COLOR}-v, --version{RESET_COLOR}                     Muestra la versión de la aplicación")
        print(f"{ident}{INFO_COLOR}-h, --help{RESET_COLOR}                        Muestra esta ayuda\n")


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

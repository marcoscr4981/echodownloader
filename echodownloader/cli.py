"""Módulo que gestiona la línea de comandos de la aplicación. Configura los argumentos,
valida la entrada del usuario y dirige el flujo del programa hacia la lógica principal.
"""
from argparse import ArgumentParser, Namespace

from .config import PROJECT_NAME, VERSION_PROJECT
from .core import  download_youtube_file, download_youtube_url
from .model.parser import Parser


def config_argparse() -> ArgumentParser:
    """Configura y devuelve el parser de argumentos de la CLI.

    Returns:
        ArgumentParser: Parser con los argumentos disponibles para el usuario.
    """
    parser = Parser()
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-u', '--url', type=str, help='URL de un video de YouTube')
    group.add_argument('-f', '--file', type=str, help='Archivo con una lista de URLs')
    parser.add_argument('-d', '--delay', type=float, help='Tiempo de espera entre descargas (en segundos)')
    parser.add_argument('-v', '--version', action='version', version=f"{PROJECT_NAME} {VERSION_PROJECT}", help=f"Versión de {PROJECT_NAME}")

    return parser


def check_args(args:Namespace) -> None:
    """Procesa los argumentos proporcionados y ejecuta la acción correspondiente.

    Args:
        args (Namespace): Argumentos parseados desde la línea de comandos.
    """
    if args.url:
        download_youtube_url(args.url)
    elif args.file:
        if args.delay:
            download_youtube_file(args.file, args.delay)
        else:
            download_youtube_file(args.file)
            
    print()


def main() -> None:
    """Punto de entrada principal de la aplicación CLI."""
    parser = config_argparse()
    args = parser.parse_args()
    check_args(args)

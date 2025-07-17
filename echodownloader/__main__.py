#!/usr/bin/env python3
"""EchoDownloader

Descarga el audio de videos de YouTube en mp3.
Utiliza la librería 'yt-dlp' para la descarga.

Autor: Marcos Cuadrado Rey
Versión: v1.1
Licencia: MIT
"""
import signal
import sys
from types import FrameType
from typing import Optional

from .cli import main

def def_handler(sig:int, frame:Optional[FrameType]) -> None:
    """Función que maneja la señal SIGINT (Ctrl + C), permitiendo una terminación ordenada del programa.

    Args:
        sig (int): Señal recibida (en este caso, SIGINT).
        frame (Optional[FrameType]): Marco de pila en el momento de la interrupción.
    """
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, def_handler)
    main()
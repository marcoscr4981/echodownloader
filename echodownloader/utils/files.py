"""Módulo que gestiona las funcionalidades con archivos."""
import os
import random
import re
import unicodedata

from ..exceptions.exceptions import EmptyDataException

def read_urls_from_file(file_path:str) -> list:
    """Lee un archivo de texto con URLs de YouTube, una por línea.

    Args:
        file_path (str): Ruta del archivo a leer.

    Returns:
        List[str]: Lista con las URLs extraídas.

    Raises:
        EmptyDataException: Si la ruta no se proporciona o el archivo no existe.
    """
    if file_path is None:
        raise EmptyDataException("No se ha proporcionado la ruta del archivo.")
    
    if not os.path.exists(file_path):
        raise EmptyDataException(f"El archivo {file_path} no existe.")

    with open(file_path, 'r', encoding='utf-8') as file:
        urls = [line.strip() for line in file if line.strip()]

    return urls


def generate_unique_file_path(name:str, extension:str) -> str:
    """Genera una ruta única para guardar un archivo evitando colisiones.

    Args:
        name (str): Nombre base del archivo.
        extension (str): Extensión (incluyendo el punto), por ejemplo '.mp3'.

    Returns:
        str: Ruta absoluta del archivo sin extensión (yt_dlp la añade luego).
    """
    sanitized_name = sanitize_filename(name)
    base_path = os.getcwd()

    while True:
        full_path = os.path.join(base_path, sanitized_name + extension)

        if not os.path.exists(full_path):
            return os.path.join(base_path, sanitized_name)
        
        sanitized_name = f"{sanitized_name}_{random.randint(0, 999999)}"


def sanitize_filename(filename: str, max_length: int = 100) -> str:
    """Limpia un texto para usarlo como nombre de archivo válido.

    Args:
        filename (str): Texto original (por ejemplo, el título del video).
        max_length (int): Longitud máxima permitida.

    Returns:
        str: Texto limpio y seguro como nombre de archivo.
    """
    # Normaliza caracteres Unicode a ASCII cuando sea posible
    filename = unicodedata.normalize("NFKD", filename).encode("ascii", "ignore").decode("ascii")

    # Elimina caracteres no permitidos en nombres de archivo
    filename = re.sub(r'[<>:"/\\|?*\n\r\t]', '', filename)

    # Reemplaza múltiples espacios por uno solo
    filename = re.sub(r'\s+', ' ', filename).strip()

    # Trunca si es demasiado largo
    if len(filename) > max_length:
        filename = filename[:max_length].rstrip()

    return filename

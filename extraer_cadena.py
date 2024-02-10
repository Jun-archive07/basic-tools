import re

def extraer_cadena(parrafo):
    """
    Extrae la primera cadena entre comillas dobles en un párrafo dado.

    Args:
        parrafo (str): El párrafo en el que se buscará la cadena.

    Returns:
        str: La primera cadena encontrada entre comillas dobles.
             Si no se encuentra ninguna cadena, se devuelve una cadena vacía.
    """
    cadena = re.findall(r'"([^"\\]*(?:\\.[^"\\]*)*)"', parrafo)
    return cadena[0] if cadena else ''
import re

def filtrar_marcas(texto, lista):
    """
    Reemplaza los caracteres especiales por un marcador en el texto.

    Args:
        texto (str): El texto en el cual se quieren reemplazar los caracteres especiales.
        lista (list): Una lista con los caracteres especiales que se quieren reemplazar.

    Returns:
        str: El texto con los caracteres especiales reemplazados por el marcador.
    """
    texto_reemplazado = texto
    for item in lista:
        etiqueta = item
        texto_reemplazado = texto_reemplazado.replace(f"{etiqueta}", "{K}")
    return texto_reemplazado
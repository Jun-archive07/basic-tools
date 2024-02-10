import re

def restaurar_marcas(texto, lista):
    """
    Inserta los caracteres especiales en el texto procesado.

    Args:
        texto (str): El texto procesado en el cual se quieren insertar los caracteres especiales.
        lista (list): Una lista con los caracteres especiales que se quieren insertar.

    Returns:
        str: El texto con los caracteres especiales insertados.
    """
    texto_insertado = texto
    for item in lista:
        etiqueta = item
        texto_insertado = texto_insertado.replace("{K}", f"{etiqueta}", 1)
    return texto_insertado
import re

def extraer_marcas(texto):
    """
    Extrae los caracteres especiales "{}" de un texto y los guarda en una lista.

    Args:
        texto (str): El texto del cual se quieren extraer los caracteres especiales.

    Returns:
        list: Una lista con los caracteres especiales encontrados en el texto.
    """
    patron = r"\{[^{}]+\}"
    lista = []
    for match in re.finditer(patron, texto):
        etiqueta = match.group(0)
        lista.append(etiqueta)
    return lista
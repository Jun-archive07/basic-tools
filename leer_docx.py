# pip install python-docx

from docx import Document

def leer_docx(ruta):
    """
    Esta función recibe una ruta a un archivo docx y devuelve el texto del documento.

    Args:
        ruta: Ruta al archivo docx.

    Returns:
        Texto del documento.
    """
    # Se crea un objeto Document a partir del archivo docx.
    doc = Document(ruta)
    # Se crea una variable para almacenar el texto del documento.
    texto = ""
    # Se itera sobre los párrafos del documento.
    for paragraph in doc.paragraphs:
        # Si el párrafo está vacío, se añade un salto de línea a la variable texto.
        if paragraph.text == "":
            texto += "\n"
        # Si el párrafo no está vacío, se añade el texto del párrafo a la variable texto.
        else:
            texto += paragraph.text + "\n"
    # Se devuelve el texto del documento.
    return texto
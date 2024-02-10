# pip install pandas openpyxl

import re
import pandas as pd

def text_replace(long_string, xlsx_path, case_sensitive):
    """
     Reemplaza palabras en una cadena larga según una asignación proporcionada en un archivo de Excel.
    
     Argumentos:
         long_string (str): La cadena larga en la que se realizarán los reemplazos.
         xlsx_path (str): la ruta al archivo de Excel que contiene la palabra mapeo.
         case_SENSITIVE (bool): determina si los reemplazos deben distinguir entre mayúsculas y minúsculas o no.
        
     Devoluciones:
         str: La cadena larga después de realizar los reemplazos.
    """
    # Leer el archivo de Excel y guardar la primera columna y la segunda columna en dos listas separadas.
    df = pd.read_excel(xlsx_path) #usa header=None para agregar la primera fila a la lista 
    old_words = df.iloc[:, 0].tolist()
    new_words = df.iloc[:, 1].tolist()
    # Ordenar las listas de palabras antiguas y nuevas en orden descendente de longitud y ajustarlas sincrónicamente.
    old_words, new_words = zip(*sorted(zip(old_words, new_words), key=lambda x: len(x[0]), reverse=True))
    # Iterar sobre las dos listas y reemplazar las cadenas de texto.    
    for i in range(len(old_words)):
        # Si no se distingue entre mayúsculas y minúsculas, convertir tanto la cadena de texto como la palabra a reemplazar a minúsculas.
        if not case_sensitive:
            lower_string = long_string.lower()
            lower_old_word = old_words[i].lower()
            # Usar expresiones regulares para realizar el reemplazo, asegurándose de mantener el formato original de la cadena de texto.
            long_string = re.sub(r"\b" + lower_old_word + r"\b", new_words[i], long_string, flags=re.IGNORECASE)
        # Si se distingue entre mayúsculas y minúsculas, realizar directamente el reemplazo utilizando expresiones regulares.
        else:
            long_string = re.sub(r"\b" + old_words[i] + r"\b", new_words[i], long_string)
    # Devolver la cadena de texto después de realizar los reemplazos.
    return long_string
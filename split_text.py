def split_text(text):
    """
    Divide un texto en fragmentos más cortos de longitud máxima de 1024 caracteres.

    Args:
        text (str): El texto a dividir.

    Returns:
        list: Una lista de fragmentos de texto cortos.
    """
    sentence_list = text.split("\n")

    # Inicializa una lista de fragmentos de texto cortos
    short_text_list = []
    # Inicializa el fragmento de texto actual
    short_text = ""
    # Recorre la lista de oraciones
    for s in sentence_list:
        # Si la longitud del fragmento de texto actual más la longitud de la nueva oración no supera los 1024 caracteres,
        # se agrega la nueva oración al fragmento de texto actual
        if len(short_text + s) <= 1024:
            short_text += s + '\n'
        # Si la longitud del fragmento de texto actual más la longitud de la nueva oración supera los 1024 caracteres,
        # se agrega el fragmento de texto actual a la lista de fragmentos de texto y se reinicia el fragmento de texto actual con la nueva oración
        else:
            short_text_list.append(short_text)
            short_text = s + '\n'
    # Agrega el último fragmento de texto a la lista de fragmentos de texto
    short_text_list.append(short_text)
    return short_text_list
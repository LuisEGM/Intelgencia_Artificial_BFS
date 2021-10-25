def sonIguales(lista_a: list, lista_b: list):
    """
    Parameters
    ----------
    lista_a, lista_b: list
        Nombre del archivo con la organizacion del tablero a leer
    Returns
    -------
    boolean:
        True si las listas son iguales y Flase en caso contrario
    """
    if len(lista_a) == len(lista_b):
        for i, x in zip(lista_a, lista_b):
            if i != x:
                return False
        return True
    else:
        return False
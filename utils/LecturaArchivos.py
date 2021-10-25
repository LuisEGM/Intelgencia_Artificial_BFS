def leerTablero(tablero_a_leer):
    """ 
    Parameters
    ----------
    tablero_a_leer: string
        Nombre del archivo con la organizacion del tablero a leer
    Returns
    -------
    list_tablero: list
        Una lista de los elementos del tablero leido
    """
    fichero = open(tablero_a_leer, "r");
    cadena_tablero = ""

    for linea in fichero:
        cadena_tablero += linea
    fichero.close();

    cadena_tablero = cadena_tablero.replace("\n", ",")
    cadena_tablero = cadena_tablero.replace(";", "")
    return cadena_tablero.split(",")

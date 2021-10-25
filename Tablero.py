import utils.EMovimientos as m
import utils.DiccionarioDeMovimientos as dm

def obtenerEstadosPosibles(estado_actual: list):
    """
    Parameters
    ----------
    estado_actual: list
        Estado actual del tablero
    Returns
    -------
    estados_posibles: list
        Una lista de los estados con los movimientos ejecutados
    """
    posicionDelCero = estado_actual.index('0')
    movimientosPosibles = dm.diccionario.get(posicionDelCero)
    listaDeEstadosPosibles = []

    for movimiento in movimientosPosibles:
        listaDeEstadosPosibles.append(moverElCero(posicionDelCero, movimiento, estado_actual))

    return listaDeEstadosPosibles

def moverElCero(posicionDelCero, movimiento: dict, estado_actual: list):
    """
    Parameters
    ----------
    posicionDelCero: number
        La posicion donde se encuentra el 0
    movimineto: dict
        El diccionario del detalle del movimiento y la casilla donde termina
    estado_actual: list
        El estado del tablero
    Returns
    -------
    estado_temporal: list
        El estado del cuadro con el movimiento ejecutado
    """
    estado_temporal = estado_actual.copy()
    estado_temporal[posicionDelCero], estado_temporal[movimiento.get('ubicacion')] = estado_temporal[movimiento.get('ubicacion')], estado_temporal[posicionDelCero]
    return estado_temporal
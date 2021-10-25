import utils.LecturaArchivos as la
import utils.ImprimirTablero as it
import utils.Compararlistas as cl
import Tablero as tab
from collections import deque

def main():
    """
    Preparacion
    """
    cola = deque()
    tablero_inicial = la.leerTablero("./assets/tablero_inicial.txt")
    tablero_final = la.leerTablero("./assets/tablero_final.txt")
    
    print(">>>>>>> TABLERO INICIAL <<<<<<<")
    it.imprimir(tablero_inicial)
    print(">>>>>>>>>>>>>>><<<<<<<<<<<<<<<<")

    # Funcion de comparacion de tableros
    # cl.sonIguales(lista_inicial, lista_final)

    # estadosPosibles = tab.obtenerEstadosPosibles(tablero_inicial)
    # print("\n================================")
    # for estado in estadosPosibles:
    #     it.imprimir(estado)
    #     print("\n================================")

main()

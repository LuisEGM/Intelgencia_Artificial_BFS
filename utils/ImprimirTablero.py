def imprimir(tablero: list):
    """
    Parameters
    ----------
    tablero: list
        Lista a imprimir
    """
    for i in range(len(tablero)):
        if i >= 0 and i < 4:
            print("{:^2}".format(tablero[i]), end=' ')
        if i == 3:
             print()
        if i >= 4 and i < 8:
            print("{:^2}".format(tablero[i]), end=' ')
        if i == 7:
             print()
        if i >= 8 and i < 12:
            print("{:^2}".format(tablero[i]), end=' ')
        if i == 11:
             print()
        if i >= 12 and i < 16:
            print("{:^2}".format(tablero[i]), end=' ')
        if i == 15:
            print()
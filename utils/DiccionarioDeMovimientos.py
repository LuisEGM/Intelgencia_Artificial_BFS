import utils.EMovimientos as em

diccionario = {
    # Posiciones con 2 posibles movimientos
    0: [
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 1
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 4
        }
    ],

    3: [
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 2
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 7
        }
    ],

    12: [
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 8
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 13
        }
    ],

    15: [
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 11
        },
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 14
        }
    ],


    # Posiciones con 3 posibles em.Movimientos
    1: [
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 0
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 2
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 5
        }
    ],
    
    2: [
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 1
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 3
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 6
        }
    ],
    
    4: [
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 0
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 8
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 5
        }
    ],

    8: [
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 4
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 12
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 9
        }
    ],

    7: [
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 3
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 11
        },
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 6
        }
    ],

    11: [
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 7
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 15
        },
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 10
        }
    ],

    13: [
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 12
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 14
        },
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 9
        }
    ],

    14: [
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 13
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 15
        },
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 10
        }
    ],

    # Posiciones con 4 posibles em.Movimientos
    5: [
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 1
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 6
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 9
        },
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 4
        }
    ],

    6: [
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 2
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 7
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 10
        },
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 5
        }
    ],

    9: [
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 5
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 10
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 13
        },
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 8
        }
    ],

    10: [
        {
            'movimiento': em.Movimientos.ARRIBA,
            'ubicacion': 6
        },
        {
            'movimiento': em.Movimientos.DERECHA,
            'ubicacion': 11
        },
        {
            'movimiento': em.Movimientos.ABAJO,
            'ubicacion': 14
        },
        {
            'movimiento': em.Movimientos.IZQUIERDA,
            'ubicacion': 9
        }
    ]
}
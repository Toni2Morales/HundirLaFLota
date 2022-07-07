import numpy as np
import time
from IPython.display import clear_output
from clases import *
def atacar(self, y, x):
    from prueba import Jugador1
    from prueba import Maquina
    jug_atac = None
    acierto = 0
    if self.nombre == Jugador1.nombre:
        jug_atac = Maquina
    elif self.nombre == Maquina.nombre:
        jug_atac = Jugador1
    if jug_atac.tablero_prop.valor[y,x] == "  ":
        self.tablero_adver.valor[y,x] = "\U0001F4A6"
        if self.nombre == Jugador1.nombre:
            print("¡Has atacado en [", y, "," ,x, "]!")
            print("¡Agua!")
        elif self.nombre == Maquina.nombre:
            print("¡Te atacaron en [", y, "," ,x, "]!")
            print("¡Agua!")
    elif jug_atac.tablero_prop.valor[y,x] == "O ":
        jug_atac.tablero_prop.valor[y,x] = "\U0001F4A2"
        self.tablero_adver.valor[y,x] = "\U0001F4A2"
        acierto = 1
        tocado_y_hundido = 0
        for bar in jug_atac.barcos:
            comparador = 0
            for posicion in bar.posicion:
                if jug_atac.tablero_prop.valor[tuple(posicion)] == "\U0001F4A2":
                        comparador += 1        
                if comparador == bar.eslora:
                    print("¡Tocado y Hundido!")
                    tocado_y_hundido = 1
                    for posicion in bar.posicion:
                        jug_atac.tablero_prop.valor[tuple(posicion)] = "\U0001F4A5"
                        self.tablero_adver.valor[tuple(posicion)] = "\U0001F4A5"
                        jug_atac.n_barcos -= 1
        if tocado_y_hundido == 0:
            if self.nombre == Jugador1.nombre:
                        print("¡Has atacado en [", y, "," ,x, "]!")
                        print("!Tocado¡")
            elif self.nombre == Maquina.nombre:
                        print("¡Te atacaron en [", y, "," ,x, "]!")
                        print("!Tocado¡")
    print("Tablero de Jugador2")
    Maquina.tablero_prop.mostrar()
    print("Tu Tablero:")
    Jugador1.tablero_prop.mostrar()
    print("Tus ataques:")
    Jugador1.tablero_adver.mostrar()
    clear_output(wait=True)
    return acierto
def acierto(self):
    from prueba import Jugador1
    from prueba import Maquina
    print("estamos en acierto")
    if (Jugador1.n_barcos != 0) and (Maquina.n_barcos != 0):
        if self.nombre == Jugador1.nombre:
            if atacar(Jugador1,int(input("Introduce la coordenada Y para atacar")),int(input("Introduce la coordenada X para atacar"))) == 1:
                acierto((self))
        if self.nombre == Maquina.nombre:
            if atacar(Maquina, np.random.randint(10), np.random.randint(10)) == 1:
                acierto((self))
# from prueba import Jugador1
# from prueba import Maquina
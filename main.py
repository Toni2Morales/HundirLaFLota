from clases import *
import numpy as np
import time
import os
def conometro(longitud):
    start = time.gmtime().tm_sec
    rev = [3,2,1,0]
    l = list(range(1,longitud+1))
    print("Presiona 'q' para saltar")
    while len(l) != 0:
        if keyboard.is_pressed("q"):
            break
        end = time.gmtime().tm_sec - start
        if end in l:
            print(rev[end-1])
            l.remove(end)
    os.system("cls")
def atacar(self, y, x):
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
    os.system("cls")
    return acierto
def acierto(self):
    if (Jugador1.n_barcos != 0) and (Maquina.n_barcos != 0):
        if self.nombre == Jugador1.nombre:
            print("turno de Jugador1")
            print("Tablero de Jugador2")
            Maquina.tablero_prop.mostrar()
            print("Tu Tablero:")
            Jugador1.tablero_prop.mostrar()
            print("Tus ataques:")
            Jugador1.tablero_adver.mostrar()
            if atacar(Jugador1,int(input("Introduce la coordenada Y para atacar: ")),int(input("Introduce la coordenada X para atacar: "))) == 1:
                os.system("cls")
                acierto((self))
        if self.nombre == Maquina.nombre:
            print("turno de Jugador2")
            print("Tablero de Jugador2")
            Maquina.tablero_prop.mostrar()
            print("Tu Tablero:")
            Jugador1.tablero_prop.mostrar()
            print("Tus ataques:")
            Jugador1.tablero_adver.mostrar()
            conometro(3)
            if atacar(Maquina, np.random.randint(10), np.random.randint(10)) == 1:
                acierto((self))
Jugador1 = jugador("Jugador1")
Jugador1.anadir_barcos()
while len(Jugador1.barcos) != 10:
    print("Introduce unas coordenadas correctas")
    Jugador1.anadir_barcos()
Maquina = jugador("Jugador2")
while len(Maquina.barcos) != 10:
    Maquina.anadir_barcos()
time.sleep(0.1)
conometro(4)
os.system("cls")
while (Jugador1.n_barcos != 0) and (Maquina.n_barcos != 0):
    turnos = (1,2)
    for i in turnos:
        if i == 1:
            if (Jugador1.n_barcos != 0) and (Maquina.n_barcos != 0):
                acierto(Jugador1)
                conometro(4)
                os.system("cls")
        elif i == 2:
            if (Jugador1.n_barcos != 0) and (Maquina.n_barcos != 0):
                conometro(4)
                acierto(Maquina)
                conometro(3)
time.sleep(0.01)
if Jugador1.n_barcos == 0:
    print("\U0001F38A" + "¡" + Maquina.nombre + " ha ganado!" + "\U0001F38A")
    print("\U0001F44E" + "¡" + Jugador1.nombre + " ha perdido!" + "\U0001F44E")
elif Maquina.n_barcos == 0:
    print("\U0001F38A" + "¡" + Jugador1.nombre + " ha ganado!" + "\U0001F38A")
    print("\U0001F44E" + "¡" + Maquina.nombre + " ha perdido!" + "\U0001F44E")
print("Tableros:")
print("Tablero de " + Jugador1.nombre)
Jugador1.tablero_prop.mostrar()
print("Ataques de " + Jugador1.nombre)
Jugador1.tablero_adver.mostrar()
print("Tablero de " + Maquina.nombre)
Maquina.tablero_prop.mostrar()
print("Ataques de " + Maquina.nombre)
Maquina.tablero_adver.mostrar()
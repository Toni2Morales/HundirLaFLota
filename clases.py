import numpy as np
import os
import time
import keyboard
class tablero:
    def __init__(self):
        self.valor = np.full([10,10], fill_value = "  ")
    def mostrar(self):
        print(self.valor)
    def limpiar(self):
        self.valor = np.full([10,10], fill_value = "  ")
class barco:
    def comprobacion(self):
        if any([(0 > self.posicion[-1][0]),(self.posicion[-1][0] >= 10),(0 > self.posicion[-1][1]),(self.posicion[-1][1] >= 10), (self.posicion[-1] in (i for x in self.dueño_barco.barcos for i in x.posicion))]):
            self.posicion.append(["No", "No"])
            return 0
    def __init__(self, eslora, posicion, orientacion, jugador):
        self.eslora = eslora
        self.posicion = posicion
        self.orientacion = orientacion
        self.dueño_barco = jugador
        while len(self.posicion) != self.eslora:
            if self.orientacion == "N":
                for i in range(self.eslora-1):
                    if self.comprobacion() == 0:
                        return
                    self.posicion.append([self.posicion[-1][0] - 1, self.posicion[-1][1]])
            elif self.orientacion == "S":       
                for i in range(self.eslora-1):
                    if self.comprobacion() == 0:
                        return
                    self.posicion.append([self.posicion[-1][0] + 1, self.posicion[-1][1]])
            elif self.orientacion == "O":    
                for i in range(self.eslora-1):
                    if self.comprobacion() == 0:
                        return
                    self.posicion.append([self.posicion[-1][0], self.posicion[-1][1] - 1])
            elif self.orientacion == "E":
                for i in range(self.eslora-1):
                    if self.comprobacion() == 0:
                        return
                    self.posicion.append([self.posicion[-1][0], self.posicion[-1][1] + 1])
        self.comprobacion()                       
class jugador:
    def __init__(self, nombre,):
        self.error_barco = False
        self.nombre = nombre
        self.n_barcos = 20
        self.tablero_prop = tablero()
        self.tablero_adver = tablero()
        self.barcos =[]
    def anadir_barcos(self):
        if self.nombre == "Jugador1":
            for i in range(10):
                self.lista_eslora = [4,3,3,2,2,2,1,1,1,1]
                self.barcos.append(barco(self.lista_eslora[i], [[int(input("Introduce la coordenada Y del barco: ")),int(input("Introduce la coordenada X del barco: "))]], input("Introduce la orientación del barco['N', 'S', 'E', 'O']: ").upper(), self))
                if ["No", "No"] in (i for x in self.barcos for i in x.posicion):
                    self.barcos.clear()
                    self.tablero_prop.limpiar()
                    return
                self.colocar_barcos()
                print("Barco", i + 1)
                self.tablero_prop.mostrar()
                start = time.gmtime().tm_sec
                rev = [3,2,1,0]
                l = [1,2,3,4]
                print("presione 'q' para saltar")
                while len(l) != 0:
                    if keyboard.is_pressed("q"):
                        break
                    end = time.gmtime().tm_sec - start
                    if end in l:
                        print(rev[end-1])
                        l.remove(end)
                os.system("cls")
        elif self.nombre == "Jugador2":
            for i in range (10):
                self.lista_eslora = [4,3,3,2,2,2,1,1,1,1]
                self.dict_orientaciones = {1:"N", 2: "S", 3:"E", 4:"O"}
                self.barcos.append(barco(self.lista_eslora[i],[[np.random.randint(0,10), np.random.randint(0,10)]], self.dict_orientaciones[np.random.randint(1,5)], self))
                if ["No", "No"] in (i for x in self.barcos for i in x.posicion):
                    self.barcos.clear()
                    self.tablero_prop.limpiar()
                    return
                self.colocar_barcos()
                # os.system("cls")
    def colocar_barcos(self):
        for bar in self.barcos:
            for posicion  in bar.posicion:
                self.tablero_prop.valor[posicion[0]][posicion[1]] = "O "
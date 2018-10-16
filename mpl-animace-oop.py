#!/usr/bin/env python3
# Soubor:  hra_zivota.py
# Datum:   16.10.2018 10:00
# Úloha:
# Popis:
############################################################################
from random import randint
from pylab import show, imshow, figure
from matplotlib import animation


class Planet:
    def __init__(self, width=64, height=64):
        self.width = width
        self.height = height
        self.data = []
        for i in range(height):
            radek = []
            for j in range(width):
                radek.append(randint(0, 1))
            self.data.append(radek)
        # fig = figure()  # odkaz na obrázek do proměnné fig
        self.fig = figure()
        # graf = imshow(data)  # a odkaz na graf do proměnné graf
        self.graf = imshow(self.data)
        # animace se provede v obrázku fig a co 500ms se spustí metoda step
        self.anim = animation.FuncAnimation(self.fig, self.step, interval=500)

    def getdata(self):
        return self.data

    def setdata(self, data):
        self.data = data

    def step(self, count):
        # vytvořím nová náhodná data
        data = [[randint(0, 1) for i in range(self.width)]
                for j in range(self.height)]
        self.graf.set_array(data)  # provedu update dat v grafu


# nadefinoval jsem jak vypadá planeta, tak si tři různé planetky udělám
earth = Planet()
mars = Planet(32, 32)
venus = Planet(64, 32)

show()

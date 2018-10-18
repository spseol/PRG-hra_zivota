#!/usr/bin/env python3
# Soubor:  hra_zivota.py
# Datum:   16.10.2018 10:00
# Úloha:
# Popis:
############################################################################
from random import randint
from matplotlib import pyplot as plt
from matplotlib import animation


class Planet:
    def __init__(self, title, width=64, height=64):
        self.width = width
        self.height = height
        self.data = []
        for i in range(height):
            radek = []
            for j in range(width):
                radek.append(randint(0, 1))
            self.data.append(radek)
        # fig = figure()  # odkaz na obrázek do proměnné fig
        self.fig = plt.figure()
        self.title = plt.title(title)
        # graf = imshow(data)  # a odkaz na graf do proměnné graf
        self.graf = plt.imshow(self.data)
        # animace se provede v obrázku fig a co 500ms se spustí metoda step
        self.anim = animation.FuncAnimation(self.fig, self.step,
                                            frames=10, interval=500)

    def getdata(self):
        return self.data

    def setdata(self, data):
        self.data = data

    def step(self, count):
        # vytvořím nová náhodná data
        data = [[randint(0, 1) for i in range(self.width)]
                for j in range(self.height)]
        self.graf.set_data(data)  # provedu update dat v grafu


# nadefinoval jsem jak vypadá planeta, tak si tři různé planetky udělám
earth = Planet('Země')
mars = Planet('Marz', 32, 32)
venus = Planet('Venuše', 64, 32)

venus.anim.save('zivot.mp4', fps=2)

plt.show()

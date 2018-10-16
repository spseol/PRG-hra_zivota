#!/usr/bin/env python3
# Soubor:  hra_zivota.py
# Datum:   16.10.2018 10:00
# Úloha:
# Popis:
############################################################################
from random import randint
from pylab import show, draw, imshow, figure
from matplotlib import animation


data = []
for i in range(32):
    radek = []
    for j in range(32):
        radek.append(randint(0, 1))
    data.append(radek)


def tick(count):
    data = [[randint(0, 1) for i in range(32)] for j in range(32)]
    plocha.set_array(data)
    draw()


fig = figure()
plocha = imshow(data)

ani = animation.FuncAnimation(fig, tick, interval=500)
show()


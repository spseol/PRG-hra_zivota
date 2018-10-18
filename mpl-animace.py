#!/usr/bin/env python3
# Soubor:  hra_zivota.py
# Datum:   16.10.2018 10:00
# Úloha:
# Popis:
############################################################################
from random import randint
from pylab import show, imshow, figure
from matplotlib import animation

HEIGHT = 32
WIDTH = 32

# vytvořím náhodné pole nul a jedniček
data = []
for i in range(HEIGHT):
    radek = []
    for j in range(WIDTH):
        radek.append(randint(0, 1))
    data.append(radek)
# toto je sto stejné jak několik předchozích rádků jen to má úsporný zápis
data = [[randint(0, 1) for i in range(WIDTH)] for j in range(HEIGHT)]


def krok(count):
    # vytvořím nová náhodná data
    data = [[randint(0, 1) for i in range(WIDTH)] for j in range(HEIGHT)]
    graf.set_data(data)  # provedu update dat v grafu


fig = figure()  # odkaz na obrázek do proměnné fig
graf = imshow(data)  # a odkaz na graf do proměnné graf

# animace se provede v obrázku fig a každých 500ms se spustí funkce krok
ani = animation.FuncAnimation(fig, krok, interval=500)
# všechno se to spustí a ukáže
show()

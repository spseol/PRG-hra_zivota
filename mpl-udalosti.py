#!/usr/bin/env python3
# Soubor:  hra_zivota.py
# Datum:   16.10.2018 10:00
# Úloha:
# Popis:
############################################################################
from random import randint
from pylab import show, imshow, figure, draw

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


def onclick(event):
    print('%s click: button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          ('double' if event.dblclick else 'single', event.button,
           event.x, event.y, event.xdata, event.ydata))
    # vytvořím nová náhodná data
    data = [[randint(0, 1) for i in range(WIDTH)] for j in range(HEIGHT)]
    graf.set_data(data)  # provedu update dat v grafu
    draw()  # připomeneme plátnu, že data se změnila a májí se znovy vykreslit


fig = figure()  # odkaz na obrázek do proměnné fig
graf = imshow(data)  # a odkaz na graf do proměnné graf

# animace se provede v obrázku fig a každých 500ms se spustí funkce krok
conn_id = fig.canvas.mpl_connect('button_press_event', onclick)
# všechno se to spustí a ukáže
show()

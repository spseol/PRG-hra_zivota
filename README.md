# PRG -- Hra života

[![Join the chat at gitter.im/spseol/Python](https://badges.gitter.im/spseol/PRG-No.svg)](https://gitter.im/spseol/Python?utm_source=share-link&utm_medium=link&utm_campaign=share-link)


Pomocí knihovny [MatPlotLib](https://matplotlib.org/)
vytvořte [Hru života](//cs.wikipedia.org/wiki/Hra_%C5%BEivota).

* V této úloze potřebujete zobrazovat matici logických hodnot. K tomu použijeme
  funkci [`imshow`](//matplotlib.org/api/_as_gen/matplotlib.pyplot.imshow.html)
  (viz např.
  [PRG-jednoduche_obrazky](//github.com/spseol/PRG-jednoduche_obrazky)).
* Data je potřeba ale také měnit. K tomu použijeme metodu `.set_data`, kterou má
  každý vytvořený graf.
* Problém ale je, že k vykreslení grafu dojde až při zavolání funkce `show`.
  V této funkci se program bude nacházet tak dlouho, dokud nezavřeme všechna
  zatím vytvořená okna.
* Změnu dat v grafu, který už je zobrazen zajistíme buď pomocí 
  [animací](//matplotlib.org/search.html?q=animation) nebo pomocí 
  [obsluhy událostí](//matplotlib.org/users/event_handling.html).

## Animace

[mpl-animace.py](mpl-animace.py)

Třída `animation` zajistí, že funkce pro překreslení dat se bude volat vždy
po uplynutí určitého časového intervalu.

## Události

[mpl-udalosti.py](mpl-udalosti.py)

V okně obrázku se sledují události a pokud nastane ta, kterou sledujeme 
(kliknutí myší), spustí se kód pro překreslení obrázku.

## OOP

Pro zajímavost/poučení ještě přidávám jak bude vypadat kód, pokud použijeme 
objektově orientované programování.

[mpl-animace-oop.py](mpl-animace-oop.py)


![Hra života](zivot.gif)

------------------------------------------------------------------------------

* https://cs.wikipedia.org/wiki/Hra_života
* https://matplotlib.org/api/animation_api.html
* https://matplotlib.org/users/event_handling.html
* https://matplotlib.org/api/_as_gen/matplotlib.pyplot.draw.html

# jean.danae.main.py
from _spy.vitollino.main import Sala, STYLE, Cena, Codigo as Code, INVENTARIO, Elemento, NS,Texto
from browser import html

STYLE["width"] = 850
STYLE["height"] = "650px"
MAPA = "https://i.imgur.com/d9YNdTu.png"

def inventario():
    mapa = Cena(img=MAPA)
    mapa(INVENTARIO)
    
    mapa.vai()
inventario()
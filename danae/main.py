# jean.danae.main.py
from _spy.vitollino.main import Sala, STYLE, Cena, Codigo as Code, INVENTARIO, Elemento, NS,Texto
from browser import html

STYLE["width"] = 850
STYLE["height"] = "650px"
MAPA = "https://i.imgur.com/d9YNdTu.png"
R_OESTE = "https://i.imgur.com/XJXjA9r.jpg"

def inventario():
    mapa = Elemento(img=MAPA,tit= "Mapa",style=dict(left=50, top=160, width=200, height=200))
    
    INVENTARIO.bota(mapa)
    r_oeste =Cena(img=R_OESTE)
    mapa.entra(r_oeste)
    
    
    
    
    
    r_oeste.vai()
inventario()
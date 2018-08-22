from _spy.vitollino.main import Cena

MAPA = "https://i.imgur.com/d9YNdTu.png"

STYLE["width"] = 812
STYLE["height"] = "559px"

def criarcenas():
    mapa = Cena(img=MAPA)
    
    mapa.vai()
criarcenas()
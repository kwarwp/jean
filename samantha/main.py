from _spy.vitollino.main import Cena, Texto, STYLE, PSTYLE, EIMGSTY, Cena
from alexa.main import  Element
from _spy.vitollino.main import INVENTARIO
from browser import html, doc


STYLE["width"] = 800
STYLE["height"] = "600px"

BACKG = "https://imgur.com/a/UdDTlZW"
Q1 = "https://imgur.com/a/t1XM4vJ"
Q2 = "https://imgur.com/a/kMgC4FZ"
Q3 = "https://imgur.com/a/3FPynY3"
Q4 = "https://imgur.com/a/g4NqoHD"
Q5 = "https://imgur.com/a/4mwAKzS"

def natureza():
    fundo = Cena(FUNDO)
    colmeia = Elemento(COLMEIA, tit = "colmeia", drag= False,
        x = 10, y = 40, w = 200 , h = 300, drop= "abelha",
        cena= fundo)
    def reposiciona_abelha(sid, x, y):
        sid.style.left = x
        sid.style.top = y
    abelha = Elemento(ABELHA, tit = "abelha", drag=True,
        x = 10, y = 40, w = 80, h = 90, drop="",
        cena=fundo)
    colmeia.doit_drop = reposiciona_abelha
    fundo.vai()

natureza()    

        


    

   
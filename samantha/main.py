from _spy.vitollino.main import Cena, Texto, STYLE, PSTYLE, EIMGSTY, Cena
from alexa.main import Elemento as Element
from _spy.vitollino.main import INVENTARIO
from browser import html, doc


STYLE["width"] = 800
STYLE["height"] = "600px"

FUNDO = "https://imagens.simplo7.net/static/2497/sku/thumb_tricoline-100-algodao-lisa-tricoline-100-algodao-lisa-branca-1474467553683.jpg"
BACKG = "https://imgur.com/a/UdDTlZW"
Q1 = "https://imgur.com/a/t1XM4vJ"
Q2 = "https://imgur.com/a/kMgC4FZ"
Q3 = "https://imgur.com/a/3FPynY3"
Q4 = "https://imgur.com/a/g4NqoHD"
Q5 = "https://imgur.com/a/4mwAKzS"

def natureza():
    fundo = Cena(FUNDO)
    background = Element(BACKG, tit = "backg", drag= False,
        x = 10, y = 40, w = 200 , h = 300, drop= "q1,q2,q3,q4,q5",
        cena= fundo)
    def reposiciona_quadros(sid, x, y):
        sid.style.left = x
        sid.style.top = y
    q1 = Element(Q1, tit = "quadro", drag=True,
        x = 10, y = 40, w = 80, h = 90, drop="",
        cena=fundo)
    background.doit_drop = reposiciona_quadros
    fundo.vai()

natureza()    

        


    

   
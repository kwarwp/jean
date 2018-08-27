from _spy.vitollino.main import Cena, Texto, STYLE, PSTYLE, EIMGSTY, Cena
from alexa.main import  Element
from _spy.vitollino.main import INVENTARIO
from browser import html, doc


STYLE["width"] = 800
STYLE["height"] = "600px"

COLMEIA = 'https://i.ytimg.com/vi/TUlH5-1qs8I/hqdefault.jpg'
ABELHA = 'http://www.baldoni.com.br/images/abelha.png'
FUNDO = "https://imagens.simplo7.net/static/2497/sku/thumb_tricoline-100-algodao-lisa-tricoline-100-algodao-lisa-branca-1474467553683.jpg"
NDCT = {}
FIX_COUNT = {}

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

        


    

   
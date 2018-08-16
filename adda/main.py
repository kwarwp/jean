# jean.adda.main.py
MAPA = "https://i.imgur.com/d9YNdTu.png"

from _spy.vitollino.main import Sala, STYLE, Codigo, Labirinto

STYLE["width"] = 850
STYLE["height"] = "650px"


class Museu:

    def __init__(self):  
        
        MAPA.vai()

                  
        ]
        STYLE = dict(width=400,heigth="250px",left=500,top=100)
        [Codigo(cena = a,topo = b ,codigo= c, style= STYLE) for a, b , c in MENSAGENS]
if __name__ == '__main__':
    #Mapa()
    Museu()
    
class Mapa:
    def __init__(self, c=NADA, n=NADA, l=NADA, s=NADA, o=NADA):
        self.salas = [sala for sala in [c, n, l, s, o]]
        self.centro, self.norte, self.leste, self.sul, self.oeste = self.salas
        for indice, sala in enumerate(self.salas[1:]):
            self.centro.cenas[indice].portal(N=sala.cenas[indice])
            indice_oposto = (indice + 2) % 4
            sala.cenas[indice_oposto].portal(N=self.centro.cenas[indice_oposto])
    
    def __criar_conexao_salas(m):
        pass #não sei como reutilizar a função mapa :(
    Museu()
                           
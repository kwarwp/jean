# jean.adda.main.py
MAPA = "https://i.imgur.com/d9YNdTu.png"

from _spy.vitollino.main import Sala, STYLE, Cena, Labirinto

STYLE["width"] = 850
STYLE["height"] = "650px"


class Mapa:
    def __init__(self):
        self.cena_mapa = Cena(img = MAPA)
        
        self.cena_mapa.meio = Cena(vai=self.vai_importar)
        self.cena_mapa.vai()

def vai(self, *_):
    self.cena_mapa.vai()
    
    
    
    def vai_importar(self, *_):
    from Jean.Kellee.main import Museu
    Museu()
    
def vai_CenaTutorialInterativo():
    cenaImporta = CenaTutorialInterativo()
    cenaImporta.vai()

if __name__ == "__main__":
	vai_CenaTutorialInterativo()
                           
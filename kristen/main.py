# jean.kristen.main.py

from browser import timer
from _spy.vitollino.main import Cena
 
SALAS = dict (R_OESTE = "https://i.imgur.com/XJXjA9r.jpg",
CA_OESTE = "https://i.imgur.com/ozE3Qhg.jpg",
C3_SUL = "https://i.imgur.com/gIvRKAJ.jpg",
C4_SUL = "https://i.imgur.com/xnD8ZtB.jpg",
C5_SUL = "https://i.imgur.com/jTAz1ND.jpg",
C6_SUL = "https://i.imgur.com/MBVBvDM.jpg",
CB_LESTE = "https://i.imgur.com/iSGp4fP.jpg",
CC_SUL = "https://i.imgur.com/M61ZyN8.jpg",
CD_SUL = "https://i.imgur.com/LakLTda.jpg",
CE_SUL = "https://i.imgur.com/uhY89Y6.jpg",
C7_SUL = "https://i.imgur.com/AXT4Zcl.jpg",
C8_OESTE = "https://i.imgur.com/R3FtDb2.jpg",
)

def generator():
    def iterator():
        for n, sala in SALAS.items():
            Cena(sala).vai()
            yield
            
    timer.set_interval(iterator, 200)
    
generator()

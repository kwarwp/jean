R_OESTE = "https://i.imgur.com/XJXjA9r.jpg"
R_LESTE = "https://i.imgur.com/rHzbmtM.jpg"
R_NORTE = "https://i.imgur.com/IPa06hM.jpg"
C1_LESTE = "https://i.imgur.com/YYuRyQR.jpg"
C1_OESTE = "https://i.imgur.com/ryMwKc8.jpg"
C1_NORTE = "https://i.imgur.com/uTIO2tN.jpg"
C1_SUL = "https://i.imgur.com/1fMjUFO.jpg"
C2_NORTE = "https://i.imgur.com/FlwvTzi.jpg"
C2_LESTE = "https://i.imgur.com/9uub4QD.jpg"
C2_OESTE = "https://i.imgur.com/vJZ7pKJ.jpg"
CA_NORTE = "https://i.imgur.com/hxZUIOf.jpg"
CA_LESTE = "https://i.imgur.com/MCEVdWU.jpg"
CA_OESTE = "https://i.imgur.com/ozE3Qhg.jpg"
C3_NORTE = "https://i.imgur.com/rRzsYT8.jpg"
C3_LESTE = "https://i.imgur.com/uy7BGaZ.jpg"
C3_OESTE = "https://i.imgur.com/ZxC1zBd.jpg"
C4_NORTE = "https://i.imgur.com/ZX7ksna.jpg"
C4_LESTE = "https://i.imgur.com/31TCLek.jpg"
C4_OESTE = "https://i.imgur.com/xw3dplb.jpg"
C5_NORTE = "https://i.imgur.com/BoFO4Dw.jpg"
C5_OESTE = "https://i.imgur.com/13RbfOr.jpg"
C5_LESTE =  "https://i.imgur.com/VSU2JRi.jpg"
C6_NORTE = "https://i.imgur.com/fQjnFkR.jpg"
C6_LESTE = "https://i.imgur.com/aqAllvM.jpg"
C6_OESTE = "https://i.imgur.com/GonsqOz.jpg"
C7_NORTE = "https://i.imgur.com/GwKkapl.jpg"
C7_LESTE = "https://i.imgur.com/AXT4Zcl.jpg"
C7_LESTE= "https://i.imgur.com/PAk5ZH1.jpg"
C9_SUL = "https://i.imgur.com/2kCYcjs.jpg"
C9_NORTE = "https://i.imgur.com/0DAX1Yq.jpg"
C9_LESTE = "https://i.imgur.com/Clwe0iK.jpg"
C9_OESTE = "https://i.imgur.com/cOVZAln.jpg"
C9_SUL = "https://i.imgur.com/pIRvnJS.jpg"
from _spy.vitollino.main import Sala, STYLE

STYLE["width"] = 850
STYLE["height"] = "650px"

class Museu:
    def __init__(self):
        R_SUL = R_OESTE
        C_SUL = C1_OESTE
        C2_SUL = C2_OESTE
        C3_SUL = C3_OESTE
        C4_SUL = C4_OESTE
        C5_SUL = C5_OESTE
        C6_SUL = C6_OESTE
        C7_SUL = C7_LESTE
        CA_SUL = CA_LESTE
        sala_0 = Sala(R_NORTE, R_LESTE,R_SUL, R_OESTE)
        sala_1 = Sala(C1_NORTE, C1_LESTE, C_SUL, C1_OESTE)
        sala_2 = Sala(C2_NORTE, C2_LESTE, C2_SUL, C2_OESTE)
        sala_3 = Sala(C3_NORTE, C3_LESTE, C3_SUL , C3_OESTE)
        sala_4 = Sala(C4_NORTE,C4_LESTE, C4_SUL, C4_OESTE)
        sala_5 = Sala(C5_NORTE, C5_LESTE, C5_SUL, C5_OESTE) 
        sala_6 = Sala(C6_NORTE, C6_LESTE, C6_SUL, C6_OESTE)
        sala_7 = Sala(C7_NORTE, C7_LESTE, C7_SUL , C7_LESTE)
        sala_9 = Sala(C9_NORTE,C9_LESTE,C9_OESTE, C9_SUL)
        sala_A = Sala(CA_NORTE,CA_LESTE,CA_OESTE, CA_SUL)
        # TEM DOIS SUL DA C9 QUE NÁ VERDADE ERA PARA SER C8
        sala_0.norte.meio = sala_1.norte
        sala_1.norte.meio = sala_2.norte
        sala_2.norte.meio = sala_3.norte
        #sala_0.norte.vai = sala_1.norte.vai()
        sala_0.norte.vai()
        
        
        
if __name__ == '__main__':
     Museu()
                           
# jean.angie.main.py
C0_NORTE = "https://i.imgur.com/IPa06hM.jpg"
C0_LESTE = "https://i.imgur.com/rHzbmtM.jpg"
C0_SUL = "https://i.imgur.com/NnVA765.jpg"
C0_OESTE = "https://i.imgur.com/XJXjA9r.jpg"
C1_NORTE = "https://i.imgur.com/YYuRyQR.jpg"
C1_LESTE = "https://i.imgur.com/1fMjUFO.jpg"
C1_SUL = "https://i.imgur.com/hF4Cmjp.jpg"
C1_OESTE = "https://i.imgur.com/NQc4pT8.jpg"
C2_NORTE = "https://i.imgur.com/FlwvTzi.jpg"
C2_LESTE = "https://i.imgur.com/9uub4QD.jpg"
C2_SUL = "https://i.imgur.com/QpC4DBa.jpg"
C2_OESTE = "https://i.imgur.com/vJZ7pKJ.jpg"
CA_NORTE = "https://i.imgur.com/hxZUIOf.jpg"
CA_LESTE = "https://i.imgur.com/MCEVdWU.jpg"
CA_SUL = "https://i.imgur.com/3gBbfTF.jpg"
CA_OESTE = "https://i.imgur.com/ozE3Qhg.jpg"
C3_NORTE = "https://i.imgur.com/rRzsYT8.jpg"
C3_LESTE = "https://i.imgur.com/uy7BGaZ.jpg"
C3_SUL = "https://i.imgur.com/gIvRKAJ.jpg"
C3_OESTE = "https://i.imgur.com/ZxC1zBd.jpg"
C4_NORTE = "https://i.imgur.com/ZX7ksna.jpg"
C4_LESTE = "https://i.imgur.com/31TCLek.jpg"
C4_SUL = "https://i.imgur.com/xnD8ZtB.jpg"
C4_OESTE = "https://i.imgur.com/xw3dplb.jpg"
C5_NORTE = "https://i.imgur.com/BoFO4Dw.jpg"
C5_LESTE =  "https://i.imgur.com/VSU2JRi.jpg"
C5_SUL = "https://i.imgur.com/jTAz1ND.jpg"
C5_OESTE = "https://i.imgur.com/13RbfOr.jpg"
C6_NORTE = "https://i.imgur.com/fQjnFkR.jpg"
C6_LESTE = "https://i.imgur.com/Y68GKPX.jpg"
C6_SUL = "https://i.imgur.com/MBVBvDM.jpg"
C6_OESTE = "https://i.imgur.com/GonsqOz.jpg"
CB_NORTE = "https://i.imgur.com/8lDTJl7.jpg"
CB_LESTE = "https://i.imgur.com/iSGp4fP.jpg"
CB_SUL = "https://i.imgur.com/Q0PR8Hy.jpg"
CB_OESTE = "https://i.imgur.com/MGsIsD7.jpg"
CC_NORTE = "https://i.imgur.com/AWmKBuA.jpg"
CC_LESTE = "https://i.imgur.com/1Yd1evR.jpg"
CC_SUL = "https://i.imgur.com/M61ZyN8.jpg"
CC_OESTE = "https://i.imgur.com/Pjtw047.jpg"
CD_NORTE = "https://i.imgur.com/dyADxoS.jpg"
CD_LESTE = "https://i.imgur.com/UEMJ0Sh.jpg"
CD_SUL = "https://i.imgur.com/LakLTda.jpg"
CD_OESTE = "https://i.imgur.com/VThND2I.jpg"
CE_NORTE = "https://i.imgur.com/JDxWPIs.jpg"
CE_LESTE = "https://i.imgur.com/RD79yQk.jpg"
CE_SUL = "https://i.imgur.com/uhY89Y6.jpg"
CE_OESTE = "https://i.imgur.com/Hw5EbJS.jpg"
C7_NORTE = "https://i.imgur.com/vD68tan.jpg"
C7_LESTE = "https://i.imgur.com/ahgVNcp.jpg"
C7_SUL = "https://i.imgur.com/AXT4Zcl.jpg"
C7_OESTE = "https://i.imgur.com/NkHNi13.jpg"
C8_NORTE = "https://i.imgur.com/4SOFpTG.jpg"
C8_LESTE = "https://i.imgur.com/HWQCqxK.jpg"
C8_SUL = "https://i.imgur.com/7q7iaN1.jpg"
C8_OESTE = "https://i.imgur.com/R3FtDb2.jpg"
C9_NORTE = "https://i.imgur.com/0DAX1Yq.jpg"
C9_LESTE = "https://i.imgur.com/Clwe0iK.jpg"
C9_SUL = "https://i.imgur.com/pIRvnJS.jpg"
C9_OESTE = "https://i.imgur.com/cOVZAln.jpg"
from _spy.vitollino.main import Cena, STYLE, Codigo
from _spy.vpython.main import *
from browser import doc
from math import pi
STYLE["width"] = 850
STYLE["height"] = "650px"
IMG_LIST = [C0_NORTE, C0_LESTE, C0_SUL, C0_OESTE]

doc['pydiv'].html = ''
_gs = Glow('pydiv')
scene = canvas()

class Sala3D:
    def __init__(self, img_list):
        for direcao, parede in enumerate(img_list):
            parede_ = box(pos=(-2, 0, 0), size=(0.2, 2, 2), texture=dict(file=parede, place=["right"]))
            
            parede_.rotate(angle=direcao*pi/2.0,pos=(0, 0, 0), axis=vec(0,0,1))

class Museu:
    def __init__(self):  
        pass
    
Sala3D(IMG_LIST)


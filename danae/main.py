# jean.danae.main.py
from _spy.vitollino.main import Sala, STYLE, Cena, Codigo as Code, INVENTARIO, Elemento, NS,Texto
from browser import html

STYLE["width"] = 850
STYLE["height"] = "650px"
MAPA = "https://i.imgur.com/d9YNdTu.png"
R_OESTE = "https://i.imgur.com/XJXjA9r.jpg"
CIRCULOB = "https://images.emojiterra.com/twitter/512px/26aa.png"
R_OESTE = "https://i.imgur.com/XJXjA9r.jpg"
R_LESTE = "https://i.imgur.com/rHzbmtM.jpg"
R_NORTE = "https://i.imgur.com/IPa06hM.jpg"
R_SUL = "https://i.imgur.com/NnVA765.jpg"
C1_NORTE = "https://i.imgur.com/YYuRyQR.jpg"
C1_SUL = "https://i.imgur.com/hF4Cmjp.jpg"
C1_OESTE = "https://i.imgur.com/NQc4pT8.jpg"
C1_LESTE = "https://i.imgur.com/1fMjUFO.jpg"
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
C3_OESTE = "https://i.imgur.com/ZxC1zBd.jpg"
C3_SUL = "https://i.imgur.com/gIvRKAJ.jpg"
C4_NORTE = "https://i.imgur.com/ZX7ksna.jpg"
C4_LESTE = "https://i.imgur.com/31TCLek.jpg"
C4_OESTE = "https://i.imgur.com/xw3dplb.jpg"
C4_SUL = "https://i.imgur.com/xnD8ZtB.jpg"
C5_NORTE = "https://i.imgur.com/BoFO4Dw.jpg"
C5_OESTE = "https://i.imgur.com/13RbfOr.jpg"
C5_LESTE =  "https://i.imgur.com/VSU2JRi.jpg"
C5_SUL = "https://i.imgur.com/jTAz1ND.jpg"
C6_NORTE = "https://i.imgur.com/fQjnFkR.jpg"
C6_LESTE = "https://i.imgur.com/Y68GKPX.jpg"
C6_OESTE = "https://i.imgur.com/GonsqOz.jpg"
C6_SUL = "https://i.imgur.com/MBVBvDM.jpg"
CB_NORTE = "https://i.imgur.com/8lDTJl7.jpg"
CB_OESTE = "https://i.imgur.com/MGsIsD7.jpg"
CB_SUL = "https://i.imgur.com/Q0PR8Hy.jpg"
CB_LESTE = "https://i.imgur.com/iSGp4fP.jpg"
CC_NORTE = "https://i.imgur.com/AWmKBuA.jpg"
CC_LESTE = "https://i.imgur.com/1Yd1evR.jpg"
CC_OESTE = "https://i.imgur.com/Pjtw047.jpg"
CC_SUL = "https://i.imgur.com/M61ZyN8.jpg"
CD_LESTE = "https://i.imgur.com/UEMJ0Sh.jpg"
CD_NORTE = "https://i.imgur.com/dyADxoS.jpg"
CD_OESTE = "https://i.imgur.com/VThND2I.jpg"
CD_SUL = "https://i.imgur.com/LakLTda.jpg"
CE_NORTE = "https://i.imgur.com/JDxWPIs.jpg"
CE_LESTE = "https://i.imgur.com/RD79yQk.jpg"
CE_OESTE = "https://i.imgur.com/Hw5EbJS.jpg"
CE_SUL = "https://i.imgur.com/uhY89Y6.jpg"
C7_NORTE = "https://i.imgur.com/vD68tan.jpg"
C7_LESTE = "https://i.imgur.com/ahgVNcp.jpg"
C7_OESTE = "https://i.imgur.com/NkHNi13.jpg"
C7_SUL = "https://i.imgur.com/AXT4Zcl.jpg"
C8_NORTE = "https://i.imgur.com/4SOFpTG.jpg"
C8_SUL = "https://i.imgur.com/7q7iaN1.jpg"
C8_LESTE = "https://i.imgur.com/HWQCqxK.jpg"
C8_OESTE = "https://i.imgur.com/R3FtDb2.jpg"
C9_NORTE = "https://i.imgur.com/0DAX1Yq.jpg"
C9_LESTE = "https://i.imgur.com/Clwe0iK.jpg"
C9_OESTE = "https://i.imgur.com/cOVZAln.jpg"
C9_SUL = "https://i.imgur.com/pIRvnJS.jpg"

def inventario():
    mapa = Elemento(img=MAPA,tit= "Mapa",style=dict(left=50, top=160, width=200, height="200px"))
    r_oeste =Cena(img=R_OESTE)
    mapa.entra(r_oeste)
    INVENTARIO.inicia()
    INVENTARIO.bota(mapa)
    cmapa= Cena(img=MAPA)
    mapa.vai = cmapa.vai
    dx, dy = 850//6, 650//2
    marcadores= [Elemento (img= CIRCULOB,style=dict(left=dx*(x%6), top=dy*(x//6), width=dx, height="325px")) for x in range (12)]
    for marcador in marcadores :
        marcador.entra(cmapa)
    
    
    
    
    
    r_oeste.vai()
inventario()
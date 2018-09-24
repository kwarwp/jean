# jean.meredith.main.py
from _spy.vitollino.main import Cena
link_para_imagem_1 = "https://i.imgur.com/IPa06hM.jpg" 
cena_1=Cena(link_para_imagem_1)
cena_1.vai()
from _spy.vitollino.main import Cena
link_para_imagem_1 = "https://i.imgur.com/IPa06hM.jpg"
link_para_imagem_2 = "https://i.imgur.com/rHzbmtM.jpg"
cena_1=Cena(link_para_imagem_1)
cena_2=Cena(link_para_imagem_2)
cena_1.direita = cena_2
cena_1.vai()
S0_NORTE = "https://i.imgur.com/XJXjA9r.jpg"
S0_SUL = "https://i.imgur.com/rHzbmtM.jpg"
S0_LESTE = "https://i.imgur.com/IPa06hM.jpg"
S0_OESTE = "https://i.imgur.com/NnVA765.jpg"
S12_SUL = "https://i.imgur.com/YYuRyQR.jpg"
S12_NORTE = "https://i.imgur.com/hF4Cmjp.jpg"
S12_LESTE = "https://i.imgur.com/NQc4pT8.jpg"
S12_OESTE = "https://i.imgur.com/1fMjUFO.jpg"
S11_LESTE = "https://i.imgur.com/FlwvTzi.jpg"
S11_SUL = "https://i.imgur.com/9uub4QD.jpg"
S11_OESTE = "https://i.imgur.com/QpC4DBa.jpg"
S11_NORTE = "https://i.imgur.com/vJZ7pKJ.jpg"
S10_LESTE = "https://i.imgur.com/hxZUIOf.jpg"
S10_SUL = "https://i.imgur.com/MCEVdWU.jpg"
S10_OESTE = "https://i.imgur.com/3gBbfTF.jpg"
S10_NORTE = "https://i.imgur.com/ozE3Qhg.jpg"
S9_LESTE = "https://i.imgur.com/rRzsYT8.jpg"
S9_SUL = "https://i.imgur.com/uy7BGaZ.jpg"
S9_NORTE = "https://i.imgur.com/ZxC1zBd.jpg"
S9_OESTE = "https://i.imgur.com/gIvRKAJ.jpg"
S8_LESTE = "https://i.imgur.com/ZX7ksna.jpg"
S8_SUL = "https://i.imgur.com/31TCLek.jpg"
S8_NORTE = "https://i.imgur.com/xw3dplb.jpg"
S8_OESTE = "https://i.imgur.com/xnD8ZtB.jpg"
S7_NORTE = "https://i.imgur.com/BoFO4Dw.jpg"
S7_OESTE = "https://i.imgur.com/13RbfOr.jpg"
S7_LESTE =  "https://i.imgur.com/VSU2JRi.jpg"
S7_SUL = "https://i.imgur.com/jTAz1ND.jpg"
S7A_LESTE = "https://i.imgur.com/fQjnFkR.jpg"
S7A_SUL = "https://i.imgur.com/Y68GKPX.jpg"
S7A_NORTE = "https://i.imgur.com/GonsqOz.jpg"
S7A_OESTE = "https://i.imgur.com/MBVBvDM.jpg"
S7B_SUL = "https://i.imgur.com/8lDTJl7.jpg"
S7B_LESTE = "https://i.imgur.com/MGsIsD7.jpg"
S7B_NORTE = "https://i.imgur.com/Q0PR8Hy.jpg"
S7B_OESTE = "https://i.imgur.com/iSGp4fP.jpg"
S6_OESTE = "https://i.imgur.com/AWmKBuA.jpg"
S6_NORTE = "https://i.imgur.com/1Yd1evR.jpg"
S6_SUL = "https://i.imgur.com/Pjtw047.jpg"
S6_LESTE = "https://i.imgur.com/M61ZyN8.jpg"
S5_NORTE = "https://i.imgur.com/UEMJ0Sh.jpg"
S5_OESTE = "https://i.imgur.com/dyADxoS.jpg"
S5_SUL = "https://i.imgur.com/VThND2I.jpg"
S5_LESTE = "https://i.imgur.com/LakLTda.jpg"
S4_OESTE = "https://i.imgur.com/JDxWPIs.jpg"
S4_NORTE = "https://i.imgur.com/RD79yQk.jpg"
S4_SUL = "https://i.imgur.com/Hw5EbJS.jpg"
S4_LESTE = "https://i.imgur.com/uhY89Y6.jpg"
S3_SUL = "https://i.imgur.com/vD68tan.jpg"
S3_OESTE = "https://i.imgur.com/ahgVNcp.jpg"
S3_LESTE = "https://i.imgur.com/NkHNi13.jpg"
S3_NORTE = "https://i.imgur.com/AXT4Zcl.jpg"
S2_OESTE = "https://i.imgur.com/4SOFpTG.jpg"
S2_LESTE = "https://i.imgur.com/7q7iaN1.jpg"
S2_NORTE = "https://i.imgur.com/HWQCqxK.jpg"
S2_SUL = "https://i.imgur.com/R3FtDb2.jpg"
S1_NORTE = "https://i.imgur.com/0DAX1Yq.jpg"
S1_LESTE = "https://i.imgur.com/Clwe0iK.jpg"
S1_OESTE = "https://i.imgur.com/cOVZAln.jpg"
S1_SUL = "https://i.imgur.com/pIRvnJS.jpg"
                  

from _spy.vitollino.main import Sala, Labirinto
def Museu():
        sala_0 = Sala(S0_NORTE, S0_LESTE, S0_SUL, S0_OESTE)
        sala_1 = Sala(S1_NORTE, S1_LESTE, S1_SUL, S1_OESTE)
        sala_2 = Sala(S2_NORTE, S2_LESTE, S2_SUL, S2_OESTE)
        sala_3 = Sala(S3_NORTE, S3_LESTE, S3_SUL , S3_OESTE)
        sala_4 = Sala(S4_NORTE, S4_LESTE, S4_SUL, S4_OESTE)
        sala_5 = Sala(S5_NORTE, S5_LESTE, S5_SUL, S5_OESTE) 
        sala_6 = Sala(S6_NORTE, S6_LESTE, S6_SUL, S6_OESTE)
        sala_7 = Sala(S7_NORTE, S7_LESTE, S7_SUL , S7_OESTE)
        sala_7A = Sala(S7A_NORTE, S7A_LESTE, S7A_SUL, S7A_OESTE)
        sala_7B = Sala(S7B_NORTE, S7B_LESTE, S7B_SUL,S7B_OESTE)
        sala_8 = Sala(S8_NORTE, S8_LESTE, S8_SUL, S8_OESTE)
        sala_9 = Sala(S9_NORTE, S9_LESTE, S9_SUL, S9_OESTE)
        sala_10 = Sala(S10_NORTE, S10_LESTE, S10_SUL, S10_OESTE)
        sala_S11 = Sala(S11_NORTE, S11_LESTE, S11_SUL, S11_OESTE)
        sala_S12 = Sala(S12_NORTE, S12_LESTE, S12_SUL, S12_OESTE)
        
        Labirinto(sala_0, None, sala_1, sala_12, None)
        Labirinto(sala_2, sala_1, sala_3, None, None)
        Labirinto(sala_4, None, sala_5, sala_3, None)
        Labirinto(sala_6, None, sala_7, None, sala_5)
        Labirinto(sala_7A, None, None, sala_7B, sala_7)
        Labirinto(sala_8, sala_7, None, None, sala_9)
        Labirinto(sala_10, None, sala_9, None, sala_11)
        Labirinto(sala_11, None, sala_10, None, sala_12)


        

        sala_0.leste.vai()
if __name__ == '__main__':

    Museu()
    
       
        
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
DINO = "http://imagem.ongame.com.br/pb/blog/stingrr.png"
from _spy.vitollino.main import Sala, STYLE, Codigo, Elemento, Texto

STYLE["width"] = 850
STYLE["height"] = "650px"

class Museu:
    def __init__(self):        
        C_SUL = C1_SUL
        C2_SUL = C1_LESTE
        sala_0 = Sala(R_NORTE, R_LESTE, R_SUL, R_OESTE)
        sala_1 = Sala(C1_NORTE, C1_LESTE, C_SUL, C1_OESTE)
        sala_2 = Sala(C2_NORTE, C2_LESTE, C2_SUL, C2_OESTE)
        sala_3 = Sala(C3_NORTE, C3_LESTE, C3_SUL , C3_OESTE)
        sala_4 = Sala(C4_NORTE,C4_LESTE, C4_SUL, C4_OESTE)
        sala_5 = Sala(C5_NORTE, C5_LESTE, C5_SUL, C5_OESTE) 
        sala_6 = Sala(C6_NORTE, C6_LESTE, C6_SUL, C6_OESTE)
        sala_7 = Sala(C7_NORTE, C7_LESTE, C7_SUL , C7_OESTE)
        sala_8 = Sala(C8_NORTE, C8_LESTE, C8_SUL, C8_OESTE)
        sala_9 = Sala(C9_NORTE,C9_LESTE, C9_SUL,C9_OESTE)
        sala_A = Sala(CA_NORTE,CA_LESTE,CA_SUL, CA_OESTE)
        sala_B = Sala(CB_NORTE, CB_LESTE, CB_SUL, CB_OESTE)
        sala_C = Sala(CC_NORTE, CC_LESTE, CC_SUL, CC_OESTE)
        sala_D = Sala(CD_NORTE, CD_LESTE, CD_SUL, CD_OESTE)
        sala_E = Sala(CE_NORTE, CE_LESTE,CE_SUL, CE_OESTE)
        # TEM DOIS SUL DA C9 QUE NA VERDADE ERA PARA SER C8
        sala_0.norte.meio = sala_9.leste
        sala_0.leste.meio = sala_1.norte
        sala_1.oeste.meio = sala_2.norte
        sala_1.sul.meio = sala_0.oeste
        sala_2.norte.meio = sala_A.norte
        sala_A.norte.meio = sala_3.norte
        sala_A.sul.meio = sala_1.leste
        sala_3.norte.meio = sala_4.norte
        sala_3.sul.meio = sala_A.sul
        sala_4.oeste.meio = sala_5.norte
        sala_4.sul.meio = sala_3.sul
        sala_5.leste.meio = sala_6.norte
        sala_5.oeste.meio = sala_C.norte 
        sala_5.sul.meio = sala_4.leste
        sala_6.sul.meio = sala_5.oeste
        sala_C.norte.meio = sala_D.norte
        sala_C.sul.meio = sala_5.leste
        sala_D.norte.meio = sala_7.norte
        sala_D.sul.meio = sala_C.sul
        sala_D.norte.meio = sala_E.norte
        sala_6.leste.meio = sala_B.norte
        sala_B.sul.meio = sala_6.oeste
        sala_7.leste.meio = sala_8.norte
        sala_7.sul.meio = sala_E.leste
        sala_8.leste.meio = sala_9.norte
        sala_8.sul.meio = sala_7.oeste
        sala_9.sul.meio = sala_8.sul
        sala_9.oeste.meio = sala_0.sul
        sala_9.sul.meio = sala_8.oeste
        sala_E.oeste.meio = sala_7.norte
        sala_E.sul.meio = sala_D.sul
        
        dino = Elemento(img=DINO, tit="Dino", style=dict(left=50, top=160, width=200, height=200))
        dino.entra(sala_2.leste)
        dinotexto = Texto(sala_2.leste, "e ai,colega, tudo tranks?")
        dino.vai = dinotexto.vai

        
        #sala_0.norte.vai = sala_1.norte.vai()
        sala_0.norte.vai()
       # cod = Codigo(cena=sala_0.norte ,topo= "ola", codigo = "if True:print('oi')",style = dict(width=400,heigth="250px",left=500,top=100))
       # cod = Codigo(cena=sala_1.norte, topo = "hello",codigo = "if True:print('ooi')",style = dict(width=400,heigth="250px",left=500,top=100))
       # cod = Codigo(cena=sala_1.leste, topo = "Bonju",codigo = "if True:print('ooi')",style = dict(width=400,heigth="250px",left=500,top=100))
       # cod = Codigo(cena=sala_1.oeste, topo = "Buenos dias",codigo = "if True:print('ooi')",style = dict(width=400,heigth="250px",left=500,top=100))
       # cod =Codigo(cena=sala_1.sul, topo = "como vai?",codigo = "if True:print('ooi')",style = dict(width=400,heigth="250px",left=500,top=100))
        
        MENSAGENS=[
                  [sala_0.norte ,"tendi",  "tamu junto"],
                  [sala_1.norte ,"Hello",  "if True:print('ooi')"],
                  [sala_1.leste ,"bonju",  "if True:print(':)')"],
                  [sala_1.oeste ,"Buenos dias",  "if True:print('oi')"],
                  [sala_1.sul ,"como vai?",  "if True:print('oi')"],
                  [sala_2.norte ,"Bora lá?",  "if True:print('oi')"],
                  [sala_2.leste,"vamos?",  "if True:print('oi')"],
                  [sala_2.oeste ,"lest go",  "if True:print('oi')"],
                  [sala_2.sul ,"vamonos",  "if True:print('oi')"],
                  [sala_3.norte ,"como estas?",  "if True:print('oi')"],
                  [sala_3.leste ,"e o dia?",  "if True:print('oi')"],
                  [sala_3.oeste ,"ta calor?",  "if True:print('oi')"],
                  [sala_3.sul ,"quanto graus está agora?",  "if True:print('oi')"],
                  [sala_4.norte ,"hey",  "if True:print('oi')"],
                  [sala_4.leste ,"parabéns",  "if True:print('oi')"],
                  [sala_4.oeste ,"você chegou até aqui!",  "if True:print('oi')"],
                  [sala_4.sul ,"tenha muito orgulho de vc",  "if True:print('oi')"],
                  [sala_5.norte ,"temos que comemorara pequenas vitórias",  "if True:print('oi')"],
                  [sala_5.leste ,"está indo muito bem",  "if True:print('oi')"],
                  [sala_5.oeste ,"tudo que fizer coloque amor",  "if True:print('oi')"],
                  [sala_5.sul ,"se ame",  "if True:print('oi')"],
                  [sala_6.norte ,"se cuide",  "if True:print('oi')"],
                  [sala_6.leste ,"hoje o dia esta lindo",  "if True:print('oi')"],
                  [sala_6.oeste ,"deixe a chuva lavar a alma",  "if True:print('oi')"],
                  [sala_6.sul ,"hasta la vista",  "if True:print('oi')"],
                  [sala_7.norte ," you say goodbye",  "if True:print('oi')"],
                  [sala_7.leste ,"and say Hello",  "if True:print('oi')"],
                  [sala_7.oeste ,"acredite em vc",  "if True:print('oi')"],
                  [sala_7.sul ,"vc é capaz",  "if True:print('oi')"],
                  [sala_8.norte ,"don't worry",  "if True:print('oi')"],
                  [sala_8.leste ,"vc é capaz",  "if True:print('oi')"],
                  [sala_8.oeste ," be free",  "if True:print('oi')"],
                  [sala_8.sul,"está quase acabando",  "if True:print('oi')"],
                  [sala_9.norte,"você esta vencendo seus medos",  "if True:print('oi')"],
                  [sala_9.leste ,"está se superando",  "if True:print('oi')"],
                  [sala_9.oeste ,"respire",  "if True:print('oi')"],
                  [sala_9.sul ,"comemore, pois vc venceu",  "if True:print('oi')"],
                  [sala_A.norte ,"tudo vai bem",  "if True:print('oi')"],
                  [sala_A.leste ,"não desista",  "if True:print('oi')"],
                  [sala_A.oeste ,"não é tão complicado",  "if True:print('oi')"],
                  [sala_A.sul ,"avai sim",  "if True:print('oi')"],
                  [sala_B.norte ,"tudo vai bem",  "if True:print('oi')"],
                  [sala_B.leste ,"não desista",  "if True:print('oi')"],
                  [sala_B.oeste ,"não é tão complicado",  "if True:print('oi')"],
                  [sala_B.sul ,"avai sim",  "if True:print('oi')"],
                  [sala_C.norte ,"tudo vai bem",  "if True:print('oi')"],
                  [sala_C.leste ,"não desista",  "if True:print('oi')"],
                  [sala_C.oeste ,"não é tão complicado",  "if True:print('oi')"],
                  [sala_C.sul ,"avai sim",  "if True:print('oi')"],
                  [sala_D.norte ,"tudo vai bem",  "if True:print('oi')"],
                  [sala_D.leste ,"não desista",  "if True:print('oi')"],
                  [sala_D.oeste ,"não é tão complicado",  "if True:print('oi')"],
                  [sala_D.sul ,"avai sim",  "if True:print('oi')"],
                  [sala_E.norte ,"tudo vai bem",  "if True:print('oi')"],
                  [sala_E.leste ,"não desista",  "if True:print('oi')"],
                  [sala_E.oeste ,"não é tão complicado",  "if True:print('oi')"],
                  [sala_E.sul ,"avai sim",  "if True:print('oi')"]





                  
                  
        ]
        STYLE = dict(width=400,heigth="250px",left=500,top=100)
        [Codigo(cena = a,topo = b ,codigo= c, style= STYLE) for a, b , c in MENSAGENS]
if __name__ == '__main__':
     Museu()
                           
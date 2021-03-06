# jean.rachel.main.py
R_OESTE = "https://i.imgur.com/mU4yGXG.jpg"
R_LESTE = "https://i.imgur.com/z1G5SQt.jpg"
R_NORTE = "https://i.imgur.com/hyEqPc5.jpg"
R_SUL = "https://i.imgur.com/TWpucy2.jpg"
C1_NORTE = "https://i.imgur.com/Xh7lpyt.jpg"
C1_SUL = "https://i.imgur.com/jJDkNdi.jpg"
C1_OESTE = "https://i.imgur.com/jcJdTXQ.jpg"
C1_LESTE = "https://i.imgur.com/TZSvzrY.jpg"
C2_NORTE = "https://i.imgur.com/nJ81M7R.jpg"
C2_LESTE = "https://i.imgur.com/iMkFqhS.jpg"
C2_SUL = "https://i.imgur.com/eKs3PIz.jpg"
C2_OESTE = "https://i.imgur.com/dEpPujC.jpg"
CA_NORTE = "https://i.imgur.com/WtwHBB5.jpg"
CA_LESTE = "https://i.imgur.com/uDS6rZg.jpg"
CA_SUL = "https://i.imgur.com/HpbbGtD.jpg"
CA_OESTE = "https://i.imgur.com/XdzF9in.jpg"
C3_NORTE = "https://i.imgur.com/tctRj4C.jpg"
C3_LESTE = "https://i.imgur.com/2Zg96D6.jpg"
C3_OESTE = "https://i.imgur.com/tGzydvu.jpg"
C3_SUL = "https://i.imgur.com/pVGpE1V.jpg"
C4_NORTE = "https://i.imgur.com/XuGL7DU.jpg"
C4_LESTE = "https://i.imgur.com/W0NIeC0.jpg"
C4_OESTE = "https://i.imgur.com/ZO0ijvk.jpg"
C4_SUL = "https://i.imgur.com/9RHiYDO.jpg"
C5_NORTE = "https://i.imgur.com/IDqMCyJ.jpg"
C5_OESTE = "https://i.imgur.com/ZJL59tQ.jpg"
C5_LESTE =  "https://i.imgur.com/gwOESvr.jpg"
C5_SUL = "https://i.imgur.com/zrnfGvO.jpg"
C6_NORTE = "https://i.imgur.com/wva7qnQ.jpg"
C6_LESTE = "https://i.imgur.com/ABvQUhW.jpg"
C6_OESTE = "https://i.imgur.com/K8YNOXs.jpg"
C6_SUL = "https://i.imgur.com/gFfL8K3.jpg"
CB_NORTE = "https://i.imgur.com/h5Cq94H.jpg"
CB_OESTE = "https://i.imgur.com/YtW5o60.jpg"
CB_SUL = "https://i.imgur.com/BFca2Fu.jpg"
CB_LESTE = "https://i.imgur.com/oh15qf6.jpg"
CC_NORTE = "https://i.imgur.com/LuhoGSo.jpg"
CC_LESTE = "https://i.imgur.com/ianxTOg.jpg"
CC_OESTE = "https://i.imgur.com/JSDZrXW.jpg"
CC_SUL = "https://i.imgur.com/NQNUXxX.jpg"
CD_LESTE = "https://i.imgur.com/Ci9SK8I.jpg"
CD_NORTE = "https://i.imgur.com/eM04YMI.jpg"
CD_OESTE = "https://i.imgur.com/R0b05u3.jpg"
CD_SUL = "https://i.imgur.com/GsW8Sdt.jpg"
CE_NORTE = "https://i.imgur.com/hTlb2cx.jpg"
CE_LESTE = "https://i.imgur.com/YeeSMKs.jpg"
CE_OESTE = "https://i.imgur.com/DGdb860.jpg"
CE_SUL = "https://i.imgur.com/4LpJnqP.jpg"
C7_NORTE = "https://i.imgur.com/hmyqGqF.jpg"
C7_LESTE = "https://i.imgur.com/lWwD4Zr.jpg"
C7_OESTE = "https://i.imgur.com/NXRctwj.jpg"
C7_SUL = "https://i.imgur.com/mkz9QTu.jpg"
C8_NORTE = "https://i.imgur.com/wIKmDJs.jpg"
C8_SUL = "https://i.imgur.com/9lKoZCo.jpg"
C8_LESTE = "https://i.imgur.com/t398lZ9.jpg"
C8_OESTE = "https://i.imgur.com/AQguZGv.jpg"
C9_NORTE = "https://i.imgur.com/ldpn1ge.jpg"
C9_LESTE = "https://i.imgur.com/rHCTu2H.jpg"
C9_OESTE = "https://i.imgur.com/q3Mabl1.jpg"
C9_SUL = "https://i.imgur.com/E21mbSx.jpg"
DINO = "http://imagem.ongame.com.br/pb/blog/stingrr.png"
PEDRA = "https://i.imgur.com/81XKpgM.jpg"
interrogacao_="https://i.imgur.com/umcmPnb.png"
from _spy.vitollino.main import Sala, STYLE, Codigo as Code, INVENTARIO, Elemento, NS,Texto
from browser import html

STYLE["width"] = 850
STYLE["height"] = "650px"
class Codigo(Code):
    def __init__(self, codigo="", topo="", cena=INVENTARIO, img="", vai=None, style=NS):
        style.update({"height":"550px"})
        Code.__init__(self, codigo=codigo, topo=topo, cena=cena, img=img, vai=vai, style=style)
        a = html.A("×", href="#", style=dict(position="absolute", top="0px", right="10px",
        fontSize="30px", fontWeight="bold"))  
        a.onclick = self._close
        self.elt<=a
        self._close()
        self._area.style.overflow="scroll"
        self._area.style.height="400px"
        self.elt.style.maxHeight="550px"
        #self.elt.style = {"visibility": "hidden", "opacity": 0}
    def _close(self, *_):
        self.elt.style = {"visibility": "hidden", "opacity": 0}
        self.cena._code_=self

         
        
        
class Museu:
    def __init__(self):        
        C_SUL = C1_SUL
        C2_SUL = C1_LESTE
        self.sala_0=sala_0 =  Sala(R_NORTE, R_LESTE, R_SUL, R_OESTE)
        self.sala_1=sala_1 =  Sala(C1_NORTE, C1_LESTE, C_SUL, C1_OESTE)
        self.sala_2=sala_2 =  Sala(C2_NORTE, C2_LESTE, C2_SUL, C2_OESTE)
        self.sala_3=sala_3 =  Sala(C3_NORTE, C3_LESTE, C3_SUL , C3_OESTE)
        self.sala_4=sala_4 =  Sala(C4_NORTE,C4_LESTE, C4_SUL, C4_OESTE)
        self.sala_5=sala_5 =  Sala(C5_NORTE, C5_LESTE, C5_SUL, C5_OESTE) 
        self.sala_6=sala_6 =  Sala(C6_NORTE, C6_LESTE, C6_SUL, C6_OESTE)
        self.sala_7=sala_7 =  Sala(C7_NORTE, C7_LESTE, C7_SUL , C7_OESTE)
        self.sala_8=sala_8 =  Sala(C8_NORTE, C8_LESTE, C8_SUL, C8_OESTE)
        self.sala_9=sala_9 =  Sala(C9_NORTE,C9_LESTE, C9_SUL,C9_OESTE)
        self.sala_A=sala_A =  Sala(CA_NORTE,CA_LESTE,CA_SUL, CA_OESTE)
        self.sala_B=sala_B =  Sala(CB_NORTE, CB_LESTE, CB_SUL, CB_OESTE)
        self.sala_C=sala_C =  Sala(CC_NORTE, CC_LESTE, CC_SUL, CC_OESTE)
        self.sala_D=sala_D =  Sala(CD_NORTE, CD_LESTE, CD_SUL, CD_OESTE)
        self.sala_E=sala_E =  Sala(CE_NORTE, CE_LESTE,CE_SUL, CE_OESTE)
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
        dino.entra(sala_5.norte)
        
        def botainventario():
            INVENTARIO.bota(dino)
        dinotexto = Texto(sala_5.norte, "e ai,colega, tudo tranks?", foi=botainventario)   
        dino.vai = dinotexto.vai
        
        
        def recobra(_):
            #return
            INVENTARIO.cena._code_.elt.style={"visibility": "visible", "opacity": 1}
        INVENTARIO.inicia()
        interrogacao = Elemento(interrogacao_,cena= INVENTARIO, tit = "Tutorial", vai=recobra,
        style=dict(left = 100, top = 100, width = 100, height = "100px"))
        interrogacao.entra(INVENTARIO)
        INVENTARIO.bota(interrogacao)
        
                #video=html.VIDEO(width="320", height="240",autoplay=True, style=dict(position="absolute", top=0, left=0))
        #video<=html.SOURCE(src="https://www.w3schools.com/html/mov_bbb.mp4")
        #sala_0.norte.elt<=video
        
        #sala_0.norte.vai = sala_1.norte.vai()
        sala_0.norte.vai()
        # cod = Codigo(cena=sala_0.norte ,topo= "ola", codigo = "if True:print('oi')",style = dict(width=400,heigth="250px",left=500,top=100))
        # cod = Codigo(cena=sala_1.norte, topo = "hello",codigo = "if True:print('ooi')",style = dict(width=400,heigth="250px",left=500,top=100))
        # cod = Codigo(cena=sala_1.leste, topo = "Bonju",codigo = "if True:print('ooi')",style = dict(width=400,heigth="250px",left=500,top=100))
        # cod = Codigo(cena=sala_1.oeste, topo = "Buenos dias",codigo = "if True:print('ooi')",style = dict(width=400,heigth="250px",left=500,top=100))
        # cod =Codigo(cena=sala_1.sul, topo = "como vai?",codigo = "if True:print('ooi')",style = dict(width=400,heigth="250px",left=500,top=100))

        MENSAGENS=[
                  [sala_0.norte ,"Olá! Se prepare, que finalmente chegou o dia de aprender a programar em Python. Vamos embarcar nessa aventura já! Crie uma cena utilizando o código abaixo. ",
                  """from _spy.vitollino.main import Cena
link_para_imagem_1 = "https://i.imgur.com/IPa06hM.jpg" 
cena_1=Cena(link_para_imagem_1)
cena_1.vai()"""],
[sala_0.leste ,"Agora que você já conseguiu programar sua primeira cena, que tal acrescentar uma nova e poder navegar entre elas com um clique à direita da imagem?",
                  """from _spy.vitollino.main import Cena
link_para_imagem_1 = "https://i.imgur.com/IPa06hM.jpg"
link_para_imagem_2 = "https://i.imgur.com/rHzbmtM.jpg"
cena_1=Cena(link_para_imagem_1)
cena_2=Cena(link_para_imagem_2)
cena_1.direita = cena_2
cena_1.vai()
"""],
                  [sala_0.sul ,"Depois de aprender a acrescentar uma nova cena, você agora pode criar um cômodo completo! Utilize o código abaixo para criar as quatro cenas que formarão um cômodo inteiro.",
                  """from _spy.vitollino.main import Cena
link_para_imagem_1 = "https://i.imgur.com/IPa06hM.jpg"
link_para_imagem_2 = "https://i.imgur.com/rHzbmtM.jpg"
link_para_imagem_3 = "https://i.imgur.com/NnVA765.jpg"
link_para_imagem_4 = "https://i.imgur.com/XJXjA9r.jpg"
cena_1=Cena(link_para_imagem_1)
cena_2=Cena(link_para_imagem_2)
cena_3=Cena(link_para_imagem_3)
cena_4=Cena(link_para_imagem_4)
cena_1.direita = cena_2
cena_2.esquerda = cena_1
cena_2.direita = cena_3
cena_3.esquerda = cena_2
cena_3.direita = cena_4
cena_4.esquerda = cena_3
cena_4.direita = cena_1
cena_1.esquerda = cena_4
cena_1.vai()
"""],
                  [sala_0.oeste , "Achou o código para montar o cômodo grande? Saiba que há uma maneira de fazer o mesmo trabalho em poucas linhas, através da função Sala. Confira testando o código abaixo:",
                  """from _spy.vitollino.main import Sala
cena_1 = "https://i.imgur.com/IPa06hM.jpg"
cena_2 = "https://i.imgur.com/rHzbmtM.jpg"
cena_3 = "https://i.imgur.com/NnVA765.jpg"
cena_4 = "https://i.imgur.com/XJXjA9r.jpg"
sala = Sala(cena_1, cena_2, cena_3, cena_4)
sala.norte.vai()
"""],

                  [sala_1.norte ,"bonju",  "if True:print(':)')"],
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
                  [sala_5.norte ,"""Vamos aprender a criar um Elemento! O primeiro passo é inserir ele na primeira linha do código.""",
                  """from _spy.vitollino.main import Sala, Labirinto, Elemento"""],
                  [sala_5.leste ,"""Insira a imagem do elemento abaixo de onde você nomeou e colocou os links das cenas""",  
                  """S1_SUL = "https://i.imgur.com/pIRvnJS.jpg"
DINO = "http://imagem.ongame.com.br/pb/blog/stingrr.png" """],
                  [sala_5.oeste ,"Agora, só falta pedir para ele rodar.",  """dino.entra(sala_7.norte)"""],
        
                  [sala_5.sul ,"Logo abaixo da última linha do Labirinto no código",  
       """dino = Elemento(img=DINO, tit="Dino", style=dict(left=50, top=160, width=200, height=200))
       """],
        
                  [sala_6.norte ,"se cuide",  "if True:print('oi')"],
                  [sala_6.leste ,"hoje o dia esta lindo",  "if True:print('oi')"],
                  [sala_6.oeste ,"deixe a chuva lavar a alma",  "if True:print('oi')"],
                  [sala_6.sul ,"hasta la vista",  "if True:print('oi')"],
                  [sala_7.norte ," you say goodbye",  "if True:print('oi')"],
                  [sala_7.leste ,"and say Hello",  "if True:print('oi')"],
                  [sala_7.oeste ,"Para inserir um Elemento à cena é preciso escolher uma imagem e  importar o Elemento do Vitollino. Em seguida, ajustar as dimensões da imagem e seu posicionamento. Por fim, dar o comando para o Elemento aparecer na sala desejada. Código:", 
"""from _spy.vitollino.main import Elemento
pedra = Elemento(img=PEDRA, tit="Pedra", 
style=dict(left=40, top=380, width=200, height="150px"))
pedra.entra(sala_7.oeste)
pedra.vai 
""" ],
                  [sala_7.sul ,"vc é capaz",  "if True:print('oi')"],
                  [sala_8.norte ,"don't worry",  "if True:print('oi')"],
                  [sala_8.leste ,"vc é capaz",  "if True:print('oi')"],
                  [sala_8.oeste ,"É importante saber que  para seu jogo funcionar você precisa chamar a função que fez no inicio , é como se vc dissesse para o código que agora ele pode rodar.",  
"""if __name__ == '__main__':
        Museu()
"""],
                  [sala_8.sul,"está quase acabando",  "if True:print('oi')"],
                  [sala_9.sul,"Antes de criar as próximas salas você precisa iniciar uma função inserir as salas. É como se fosse uma casa com vários cômodos, pois sem casa não é possível ter cômodos...O mesmo ocorre com o código abaixo, ele mostra onde as salas têm que estar inseridas.", 
"""class Museu:
     def __init__(self):
     
     
"""],
                  [sala_9.oeste,"Agora você precisa definir as 4 cenas de cada sala. Essas salas servem para você criar cômodo onde se olha todas as paredes, assim , como foi feito no Tutorial Cena do jogo.Você pode criar quantas salas forem necessárias para o seu jogo.",
"""        
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

        

        sala_0.leste.vai()
if __name__ == '__main__':


     Museu()
        
"""],
                  [sala_9.leste ,""""O primeiro passo agora é listar todas as cenas do museu nomeando 
                  e indicando os seus links.""",  
                  """S0_NORTE = "https://i.imgur.com/XJXjA9r.jpg"
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
                  """],
                  [sala_9.sul ,"""Você deve ter observado que só a primeira sala ficou visível no jogo. 
                  Agora você tem que usar a função labiritno do vitollino para que seja possível juntá-las criando uma ponte
                  , possibilitando a navegação entre elas.
                  Assim, pode-se criar um caminho, depois de usar a função 
                  labirinto para 5 salas. Para isso, insira a função Labirinto no topo do seu código.
                  
                  """,
                    
"""   
from _spy.vitollino.main import Sala, Labirinto    
"""],
                  [sala_9.norte ,"""É importante saber que a função labirinto é uma função que liga salas em forma 
                  de cruz na qual a pirmeira sala é o centro desta cruz e a segunda sala é o topo. As seguintes salas 
                  seguem o sentido horário. O termo
                  "None" é utilizado para uma parte da cruz que não tem sala. """,  
                  """   
        Labirinto(sala_0, None, sala_1, sala_S12, None)
        Labirinto(sala_2, sala_1, sala_3, None, None)
        Labirinto(sala_4, None, sala_5, sala_3, None)
        Labirinto(sala_6, None, sala_7, None, sala_5)
        Labirinto(sala_7A, None, None, sala_7B, sala_7)
        Labirinto(sala_8, sala_7, None, None, sala_9)
        Labirinto(sala_10, None, sala_9, None, sala_S11)
        Labirinto(sala_S11, None, sala_10, None, sala_S12)
"""],
                  [sala_A.norte ,"não desista",  "if True:print('oi')"],
                  [sala_A.leste ,"Agora par ficar mais divertido temos como movimentos elementos dentro da Cena, essa função chamamos de Drag and Drop",  
"""
VAR1 = 'https://i.imgur.com/vb4zrA0.jpg'
VAR2 = 'https://trabalhodigitalinfo.files.wordpress.com/2016/01/seta-vermelha-2png.png'
VAR3 = "https://imagens.simplo7.net/static/2497/sku/thumb_tricoline-100-algodao-lisa-tricoline-100-algodao-lisa-branca-1474467553683.jpg"

def movimento():
    camada1 = Cena(VAR3)
    camada2 = Elemento(VAR1, tit = "segunda camada", drag= False,
        x = 0, y = 0, w = 800 , h = 600, drop= "Mova-me",
        cena= camada1)
        
    def reposiciona_figura(sid, x, y):
        sid.style.left = x
        sid.style.top = y
        
    movel = Elemento(VAR2, tit = "Mova-me", drag=True,
        x = 310, y = 160, w = 80, h = 90, drop="",
    cena=camada1)
    camada2.doit_drop = reposiciona_figura
    camada1.vai()

movimento() 
"""],
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
                  [sala_E.sul ,"não é tão complicado",  "if True:print('oi')"],




                  
                  
        ]
        STYLE = dict(width=400,heigth="250px",left=400,top=100, visibility= "hidden", opacity= 0)
        #STYLE = dict(width=400,heigth="250px",left=400,top=100, visibility= "visible", opacity= 1)
        self.salas = [Codigo(cena = a,topo = b ,codigo= c, style= STYLE) for a, b , c in MENSAGENS]
        
        pedra = Elemento(img=PEDRA, tit="Pedra", style=dict(left=40, top=380, width=200, height="150px"))
        pedra.entra(sala_7.oeste)
        pedra.vai 
        
        
if __name__ == '__main__':


     Museu()
                           
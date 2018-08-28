# jean.danae.main.py
from _spy.vitollino.main import Sala, STYLE, Cena, Codigo as Code, INVENTARIO, Elemento, NS,Texto
from browser import html

STYLE["width"] = 850
STYLE["height"] = "650px"
MAPA = "https://i.imgur.com/d9YNdTu.png"
R_OESTE = "https://i.imgur.com/XJXjA9r.jpg"
CIRCULOB = "https://images.emojiterra.com/twitter/512px/26aa.png"
CENAS = """Criar uma cena
Criar uma Segunda cena
Ligar uma cena a outra
Formar um cômodo com quatro cenas
Usar a função Sala para formar um cômodo
Usar a função labirinto para conectar cinco salas
Usar a função Mapa para conectar  diversas salas
Colocar elementos na cena
Associar um Texto e uma Cena (ao entrar ou sair)
Associar um Texto e um elemento
Associar uma ação ao fechamento do Texto
Uso do Elemento no Inventário""".split("\n")
#Drag and drop do Elemento para outro elemento
 #Drag and drop do Elemento para a cena
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



def inventario():
    mapa = Elemento(img=MAPA,tit= "Mapa",style=dict(left=50, top=160, width=200, height="200px"))
    r_oeste =Cena(img=R_OESTE)
    mapa.entra(r_oeste)
    INVENTARIO.inicia()
    INVENTARIO.bota(mapa)
    cmapa= Cena(img=MAPA)
    mapa.vai = cmapa.vai
    cenas= [Cena(img=cena) for cena in SALAS.values()]
    dx, dy = 850//6, 650//2
    marcadores= [Elemento (img= CIRCULOB, tit=tit, style=dict(
        left=dx*(x%6), top=dy*(x//6), width=dx, height="325px", opacity=0.01,
        ))
       
    for x, tit in enumerate (CENAS)]
    for  x, marcador in enumerate (marcadores) :
        marcador.entra(cmapa)
        marcador.vai= cenas[x].vai
        
        

    
    
    
    
    
    r_oeste.vai()
inventario()


""" csalas= Cena(img= SALAS)
    sala.vai = csala.vai  
    marcadores= [Elemento (img= CIRCULOB, tit=tit, style=dict(
        left=dx*(x%6), top=dy*(x//6), width=dx, height="325px", opacity=0.01,
        ))
    for x, tit in enumerate(SALAS)]
    for marcador in marcadores:
        marcador.entra(SALAS)
        marcador.vai 
"""
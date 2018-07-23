# jean.stacy.main.py
WHITE = "https://i.imgur.com/opHOSiE.jpg"
PAREDES = dict(
C0_OESTE = "https://i.imgur.com/XJXjA9r.jpg",
C0_LESTE = "https://i.imgur.com/rHzbmtM.jpg",
C0_NORTE = "https://i.imgur.com/IPa06hM.jpg",
C1_LESTE = "https://i.imgur.com/YYuRyQR.jpg",
C1_OESTE = "https://i.imgur.com/ryMwKc8.jpg",
C1_NORTE = "https://i.imgur.com/uTIO2tN.jpg",
C1_SUL = "https://i.imgur.com/1fMjUFO.jpg",
C2_NORTE = "https://i.imgur.com/FlwvTzi.jpg",
C2_LESTE = "https://i.imgur.com/9uub4QD.jpg",
C2_OESTE = "https://i.imgur.com/vJZ7pKJ.jpg",
C8_NORTE = "https://i.imgur.com/hxZUIOf.jpg",
C8_LESTE = "https://i.imgur.com/MCEVdWU.jpg",
C8_OESTE = "https://i.imgur.com/ozE3Qhg.jpg",
C3_NORTE = "https://i.imgur.com/rRzsYT8.jpg",
C3_LESTE = "https://i.imgur.com/uy7BGaZ.jpg",
C3_OESTE = "https://i.imgur.com/ZxC1zBd.jpg",
C4_NORTE = "https://i.imgur.com/ZX7ksna.jpg",
C4_LESTE = "https://i.imgur.com/31TCLek.jpg",
C4_OESTE = "https://i.imgur.com/xw3dplb.jpg",
C5_NORTE = "https://i.imgur.com/BoFO4Dw.jpg",
C5_OESTE = "https://i.imgur.com/13RbfOr.jpg",
C5_LESTE =  "https://i.imgur.com/VSU2JRi.jpg",
C6_NORTE = "https://i.imgur.com/fQjnFkR.jpg",
C6_LESTE = "https://i.imgur.com/aqAllvM.jpg",
C6_OESTE = "https://i.imgur.com/GonsqOz.jpg",
C7_NORTE = "https://i.imgur.com/GwKkapl.jpg",
C7_LESTE = "https://i.imgur.com/AXT4Zcl.jpg",
C7_OESTE= "https://i.imgur.com/PAk5ZH1.jpg",
C7_SUL = "https://i.imgur.com/2kCYcjs.jpg",
C9_NORTE = "https://i.imgur.com/0DAX1Yq.jpg",
C9_LESTE = "https://i.imgur.com/Clwe0iK.jpg",
C9_OESTE = "https://i.imgur.com/cOVZAln.jpg",
C9_SUL = "https://i.imgur.com/pIRvnJS.jpg"
)
from _spy.vitollino.main import Sala, STYLE, NADA, Elemento, INVENTARIO, PSTYLE, EIMGSTY, NS
from browser import window, html
EDTST = {'position': 'relative', 'padding': '10px', 'margin': '0px',
         'width': '100%', 'resize': 'none', 'borderColor': 'darkslategrey',
         'color': 'navajowhite', 'border': 0, 'background-color': 'rgba(76, 175, 80, 0.3)'}

STYLE["width"] = 1000
STYLE["height"] = "650px"
RUMOS = "NORTE LESTE SUL OESTE".split()
CART = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # [(i, j) for j, i in CART]

CODE_0 = """
from _spy.vitollino.main import Cena
C9_OESTE = "https://i.imgur.com/cOVZAln.jpg",
cena = Cena(C9_OESTE)
cena.vai()
"""

class Codigo(Elemento):
    """
    Um objeto de interação que é representado por uma imagem em uma cena.
            papel = Elemento(
             img="papel.png", tit="caderno de notas",
             vai=pega_papel, style=dict(left=350, top=550, width=60))
    :param img: URL de uma imagem
    :param vai: função executada quando se clica no objeto
    :param style: dicionário com dimensões do objeto {"left": ..., "top": ..., width: ..., height: ...}
    :param tit: Texto que aparece quando se passa o mouse sobre o objeto
    :param alt: Texto para leitores de tela
    :param cena: cena alternativa onde o objeto vai ser colocado
    :param score: determina o score para este elemento
    :param kwargs: lista de parametros nome=URL que geram elementos com este nome e a dada imagem
    """
    def __init__(self, codigo="", cena=INVENTARIO, img="", vai=None, style=NS):
        self.img = img
        self.vai = vai if vai else lambda _=0: None
        self.cena = cena
        self.opacity = 0
        self.style = dict(**PSTYLE)
        # self.style["min-width"], self.style["min-height"] = w, h
        self.style.update(**style)
        self.elt = html.DIV(style=self.style)
        self.xy = (-111, -111)
        istyle = dict(EIMGSTY)
        istyle.update(opacity=0.3)
        if img:
            self.img = html.IMG(src=img, style=istyle)  # width=self.style["width"])
            self.elt <= self.img
        self.elt.onclick = self._click
        self.scorer = dict(ponto=1, valor=cena.nome, carta=img, casa=self.xy, move=None)
        self._area = html.DIV(html.PRE(codigo), Class="w3-code pythonHigh", style=dict(position='absolute', top=0, left=0))
        self.elt <= self._area


        _ = self.entra(cena) if cena and (cena != INVENTARIO) else None


class Labirinto:

    @staticmethod
    def m(cenas):
        def valid(cns, jj, ii, m, n):
            return 0 <= jj + m < len(cns) and 0 <= ii + n < len(cns[jj + m]) and cns[jj + m][ii + n]

        def vizinhos(jj, ii, cns=cenas):
            return [(kk, cns[jj + m][ii + n]) for kk, (m, n) in enumerate(CART) if valid(cns, jj, ii, m, n)]
            # return [(kk, cns[jj + m][ii + n]) for kk, (m, n) in enumerate(CART)
            #  if 0 <= jj + m < len(cns) and 0 <= ii + n < len(cns[jj+m])and cns[jj + m][ii + n]]

        for j, linha in enumerate(cenas):
            if isinstance(linha, list):
                for i, centro in enumerate(linha):
                    if not isinstance(centro, Sala):
                        continue
                    for k, sala in vizinhos(j, i):
                        if not isinstance(sala, Sala):
                            continue
                        centro.cenas[k].meio = sala.cenas[k]
                        indice_oposto = (k + 2) % 4
                        sala.cenas[indice_oposto].meio = centro.cenas[indice_oposto]


class Museu:
    def __init__(self):
        [PAREDES.update({"{}_SUL".format(sala[:2]): imagem}) for sala, imagem in PAREDES.items() if "OESTE" in sala]
        museu = {"sala_{}".format(indice): Sala(
            *[PAREDES["C{}_{}".format(indice, rumo)] for rumo in RUMOS], nome="sala_{}".format(indice))
        for indice in range(10)}
        mapa = [[museu["sala_{}".format((j+i) %10)] for i in range(4)] for j in range(0, 16, 4)]
        Labirinto.m(mapa)
        entrada = museu["sala_0"].norte
        cod = Codigo(cena=entrada, codigo=CODE_0, img=WHITE, style=dict(width=400, height="300px", left=500, top=100))
        entrada.vai()
        
        
        
if __name__ == '__main__':
     Museu()
                           
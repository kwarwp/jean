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
from _spy.vitollino.main import Sala, STYLE, NADA, Elemento, INVENTARIO, PSTYLE, EIMGSTY, NS, Cena, Codigo
from browser import window, html
PKEYS = ['False', 'None', 'True', ' and ', ' as ', 'assert', 'break', 'class ', 'continue', 'def ',
         'del', 'elif', 'else', 'except', 'finally', 'for ', 'from ', 'global ', 'if ', 'import ',
         ' in ', ' is ', 'lambda', 'nonlocal', ' not ', ' or ', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
EDTST = {'position': 'relative', 'padding': '5px', 'margin': '0px',
         'width': '100%', 'resize': 'none', 'borderColor': 'darkslategrey',
         'color': 'navajowhite', 'border': 0, 'background-color': 'rgba(76, 175, 80, 0.3)'}

STYLE["width"] = 1000
STYLE["height"] = "650px"
RUMOS = "NORTE LESTE SUL OESTE".split()
CART = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # [(i, j) for j, i in CART]

CODE_0 = """from _spy.vitollino.main import Cena
C9_OESTE = "https://i.imgur.com/cOVZAln.jpg"
cena = Cena(C9_OESTE)
cena.vai()"""

class Labirinto:

    @staticmethod
    def m(cenas):
        def valid(cns, jj, ii, m, n):
            return 0 <= jj + m < len(cns) and 0 <= ii + n < len(cns[jj + m]) and cns[jj + m][ii + n]

        def vizinhos(jj, ii, cns=cenas):
            return [(kk, cns[jj + m][ii + n]) for kk, (m, n) in enumerate(CART) if valid(cns, jj, ii, m, n)]

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
STYLE = dict(width=400, height="250px", left=500, top=100)
# [Codigo(cena=c, topo=t, codigo=g, style=STYLE) for c, t, g in TUT]
VAI = Cena.vai
class Museu:
    CUR = None
    def __init__(self):
        self.nome = ""
        [PAREDES.update({"{}_SUL".format(sala[:2]): imagem}) for sala, imagem in PAREDES.items() if "OESTE" in sala]
        museu = {"sala_{}".format(indice): Sala(
            *[PAREDES["C{}_{}".format(indice, rumo)] for rumo in RUMOS], nome="sala_{}".format(indice))
        for indice in range(10)}
        mapa = [[museu["sala_{}".format((j+i) %10)] for i in range(4)] for j in range(0, 16, 4)]
        Labirinto.m(mapa)
        self.corrente = entrada = museu["sala_0"].norte
        topo = "Este é o código inicial para se construir a primeira cena. Cria-se uma referência à uma imagem na internet"+\
        "e atribui-se à Cena"
        Cena.vai = self.vai

        self.cod = Codigo(cena=entrada, topo=topo, codigo=CODE_0, style=dict(width=400, height="250px", left=500, top=100))
        entrada.vai()
        Museu.CUR = self
    def instrumenta(self, cena):
        self.cod.entra(cena)
        VAI(self)
        # Cena.vai = VAI
    def vai(self):
        Museu.CUR.instrumenta(self)
        Cena.vai = VAI
        self.vai()
        
        
        
        
if __name__ == '__main__':
     Museu()
                           
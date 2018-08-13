from browser import document, html
from _spy.vitollino.main import Cena, STYLE, Elemento, Droppable, Dragger


STYLE['width'] = 740


PLANO_FUNDO = "ttps://cdn.simplo7.net/static/7106/sku/tricoline-lisa-100-algodao-tricoline-lisa-100-algodao-cinza-1921-50cm-x-1-50mt--p-1502305300683.jpg"

FLORESTA = "https://imgc.allpostersimages.com/img/print/posters/claude-monet-girassol_a-G-8757317-0.jpg"

def _main():
    document['pydiv'].html = ""
    plano_fundo = Cena(img=plano_fundo)
    plano_fundo.vai()

class Folha:
    def __init__(self, bloco, left=0, top=0, ileft=0, itop=0,
                 size=dict(width="100px", height="100px")):
        self.suporte = None
        w, h = int(size['width'][:-2]), int(size['height'][:-2])
        ileft, itop = "%dpx" % (ileft*w), "%dpx" % (itop*h)
        style = {'position': 'absolute', 'overflow': 'hidden', 'margin':'1%',
                'background-image': 'url({})'.format(bloco.img),
                'background-position': '{} {}'.format(ileft, itop),
                'background-size': '{}px {}px'.format(400, 400),
        }
        image_style = {'position': "relative", 'min-width': '400px',
        'height': '400px'}  # , 'pointer-events': 'none'}
        style.update(size)
        style.update(left="%dpx" % (left*(w+10)), top="%dpx" % (top*(h+10)))
        #image_style.update(left="%dpx" % (-ileft*w), top="%dpx" % (-itop*h))
        fid = "folha%d" % (10*top+left)
        self.folha = html.DIV(Id=fid, style=style, draggable=True)  #este true/false é apenas estético      
        bloco.folha <= self.folha
        self.folha.ondragstart = self.drag_start
        self.folha.onmouseover = self.mouse_over
        bloco.folhas[fid]=self
        #self.fo_img.ondragstart = self.img_drag_start

    #def mouse_over(self, ev):
       # ev.target.style.cursor = "pointer"
        #return False

    #def img_drag_start(self, ev):
        #ev.preventDefault()
        #ev.stopPropagation()
        #return False

    def drag_start(self, ev):
        ev.stopPropagation()
        ev.data['text'] = ev.target.id
        ev.data.effectAllowed = 'move'
        return False

    def troca(self, suporte):
        self.folha.style.left = 0
        self.folha.style.top = 0
        suporte.recebe(self, self.suporte)
        self.suporte = suporte
        self.folha.style.cursor = "auto"


class Suporte:
    def __init__(self, bloco, certa, left=0, top=0,
                 size=dict(width="25%", height="25%")):
        self.ladrilho = None
        style = {'position': "absolute", 'overflow': 'hidden',
                 'border':'1px solid white'}
        w, h = int(size['width'][:-1]), int(size['height'][:-1])
        style.update(size)
        style.update(left="%d%%" % (left*w), top="%d%%" % (top*h))
        self.certa = certa
        self.folha = html.DIV(style=style)
        bloco.suporte <= self.folha
        self.folha.ondragover = self.drag_over
        self.folha.ondrop = self.drop
        self.bloco = bloco

    def recebe(self, folha, suporte):
        self.folha <= folha.folha
        suporte.recebe(self.ladrilho, None) if suporte else None
        self.ladrilho = folha

    def drag_over(self, ev):
        ev.data.dropEffect = 'move'
        ev.preventDefault()
        return False

    def drop(self, ev):
        ev.preventDefault()
        ev.stopPropagation()
        src_id = ev.data['text']
        self.bloco.folhas[src_id].troca(self) 
   


class Bloco:
    def __init__(self, img):
        self.img = img
        self.folhas = {}
        self.monta = lambda *_: None
        ordem = ["%02d"%x for x in range(16)]
        desordem = ordem[:]
        from random import shuffle
        shuffle(desordem)
        self.tela = document["pydiv"]
        self.suporte = html.DIV(style=dict(position="absolute",
        left=10, top=20, width=400, height='%dpx'%400, border=1,
        borderColor="white"))
        self.folha = html.DIV(style=dict(position="absolute",
        left=410, top=20, width=450, height='%dpx'%450))
        self.tela.html = ""
        self.tela <= self.suporte
        self.tela <= self.folha
        self.pecas_colocadas = []
        #print(list(enumerate(ordem)))
        for pos, fl in enumerate(ordem):
            Suporte(self, "folha" + fl, pos//4, pos%4)
        for pos, tx in enumerate(desordem):
            Folha(self, pos//4, pos%4, int(tx)//4, int(tx)%4)

   

    def vai(self):
        self.monta()
        self.monta = self.nao_monta
        # self.centro.norte.vai()


if __name__ == "__main__":
    #main()
    Bloco(FLORESTA)
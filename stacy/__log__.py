
{'date': 'Mon Jul 23 2018 12:47:07.167 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 49
    Museu()
  module <module> line 44
    [PAREDES.put("{}_SUL".format(sala[:2]), imagem) for sala, imagem in PAREDES.items() if "OESTE" in sala]
AttributeError: 'dict' object has no attribute 'put'
'''},
{'date': 'Mon Jul 23 2018 12:57:34.590 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 53
    Museu()
  module <module> line 45
    museu = {"sala_{}".format(indice): Sala(
NameError: name 'RUMOS' is not defined
'''},
{'date': 'Mon Jul 23 2018 13:14:56.255 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 83
    Museu()
  module <module> line 77
    mapa = [[museu[(j %10)+i] for i in range(4)] for j in range(0, 16, 4)]
KeyError: 0
'''},
{'date': 'Mon Jul 23 2018 13:18:30.185 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 83
    Museu()
  module <module> line 77
    mapa = [[museu["sala_{}".format((j %10)+i)] for i in range(4)] for j in range(0, 16, 4)]
KeyError: sala_10
'''},
{'date': 'Mon Jul 23 2018 14:51:40.777 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 133
    Museu()
  module <module> line 127
    cod = Codigo(cena=entrada, codigo=CODE_0, style=dict(width=300, height="400px", left=400, top=100))
  module <module> line 71
    self._auto_score = self.score if score else self._auto_score
NameError: name 'score' is not defined
'''},
{'date': 'Mon Jul 23 2018 14:54:01.833 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: textarea.parentNode is null>
'''},
{'date': 'Mon Jul 23 2018 14:54:48.983 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 134
    Museu()
  module <module> line 128
    cod = Codigo(cena=entrada, codigo=CODE_0, style=dict(width=300, height="400px", left=400, top=100))
  module <module> line 91
    _ = self.entra(cena) if cena and (cena != INVENTARIO) else None
  module _spy.vitollino.main line 453
    self.scorer.update(valor=cena.nome, move=self.xy,
AttributeError: 'Codigo' object has no attribute 'scorer'
'''},
{'date': 'Mon Jul 23 2018 16:42:47.72 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 139
    Museu()
  module <module> line 133
    cod = Codigo(cena=entrada, codigo=CODE_0, img=WHITE, style=dict(width=400, height="300px", left=500, top=100))
  module <module> line 93
    self._code.innerHtml = window.hljs.highlightPython(codigo)
AttributeError: no attribute highlightPython for [object Object]
'''},
{'date': 'Mon Jul 23 2018 19:26:27.926 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
Exception: <TypeError: e is undefined>
'''},
{'date': 'Mon Jul 23 2018 19:26:41.101 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
Exception: <Error: Unknown language: "
from _spy.vitollino.main import Cena
C9_OESTE = "https://i.imgur.com/cOVZAln.jpg",
cena = Cena(C9_OESTE)
cena.vai()
">
'''},
{'date': 'Mon Jul 23 2018 19:29:56.278 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
Exception: <Error: Unknown language: "
from _spy.vitollino.main import Cena
C9_OESTE = "https://i.imgur.com/cOVZAln.jpg"
cena = Cena(C9_OESTE)
cena.vai()
">
'''},
{'date': 'Mon Jul 23 2018 21:02:06.617 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 39
    STYLE["width"] = 1000
NameError: name 'STYLE' is not defined
'''},
{'date': 'Mon Jul 23 2018 21:02:27.593 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 66
    Museu()
  module <module> line 51
    museu = {"sala_{}".format(indice): Sala(
NameError: name 'RUMOS' is not defined
'''},
{'date': 'Mon Jul 23 2018 21:04:38.727 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 66
    Museu()
  module <module> line 60
    cod = Codigo(cena=entrada, topo=topo, codigo=CODE_0, style=dict(width=400, height="250px", left=500, top=100))
  module _spy.vitollino.main line 504
    codigo = window.hljs.highlight("python", codigo)
NameError: name 'window' is not defined
'''},
{'date': 'Mon Aug 06 2018 17:22:31.310 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 149
    Museu()
  module <module> line 143
    entrada.direita = Cena(vai=mostra_codigo)
NameError: name 'Cena' is not defined
'''},
{'date': 'Mon Aug 06 2018 18:56:47.514 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 104
    Museu()
  module <module> line 94
    cod = Codigo(cena=entrada, topo=topo, codigo=CODE_0, style=dict(width=400, height="250px", left=500, top=100))
NameError: name 'Codigo' is not defined
'''},
{'date': 'Mon Aug 06 2018 18:58:02.85 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 104
    Museu()
  module <module> line 95
    entrada.vai()
  module <module> line 97
    self.corrente.vai()
AttributeError: 'Cena' object has no attribute 'corrente'
'''},
{'date': 'Mon Aug 06 2018 18:59:13.685 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 104
    Museu()
  module <module> line 95
    entrada.vai()
  module <module> line 97
    self.corrente.vai()
AttributeError: 'Cena' object has no attribute 'corrente'
'''},
{'date': 'Mon Aug 06 2018 19:02:27.784 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 105
    Museu()
  module <module> line 96
    entrada.vai()
  module <module> line 97
    self.corrente.vai()
  module <module> line 97
    self.corrente.vai()
AttributeError: 'Cena' object has no attribute 'corrente'
'''},
{'date': 'Sun Aug 12 2018 20:37:01.205 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 112
    Museu()
  module <module> line 97
    entrada.vai()
  module <module> line 104
    Museu.CUR.instrumenta(self)
  module <module> line 100
    self.cod.entra(cena)
  module _spy.vitollino.main line 459
    cena <= self
TypeError: '<=' not supported between instances of 'Museu' and 'Codigo'
'''},
{'date': 'Fri Apr 26 2019 08:41:58.307 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 278
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 112
    Museu()
  module <module> line 97
    entrada.vai()
  module <module> line 104
    Museu.CUR.instrumenta(self)
  module <module> line 100
    self.cod.entra(cena)
  module _spy.vitollino.main line 465
    cena <= self
TypeError: '<=' not supported between instances of 'Museu' and 'Codigo'
'''},
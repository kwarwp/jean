
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
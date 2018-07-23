
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
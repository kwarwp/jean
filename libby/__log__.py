
{'date': 'Mon Jul 30 2018 10:48:25.439 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 106
    Museu()
  module <module> line 97
    ex1=Codigo(topo= "oi", style=dict(left=100, top=100, width=100, heigth="100px"))
  module _spy.vitollino.main line 505
    def rp(cod, keys=PKEYS[:], mark='<span class="hljs-keyword">{}</span>'):
NameError: name 'PKEYS' is not defined
'''},
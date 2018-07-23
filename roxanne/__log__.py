
{'date': 'Wed Jul 18 2018 11:17:24.441 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 5
  R_OESTE = “https://i.imgur.com/XJXjA9r.jpg”
             ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Jul 18 2018 11:18:12.888 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 6
  R_LESTE = "https://i.imgur.com/rHzbmtM.jpg”
                                             ^
SyntaxError: EOL while scanning string literal
'''},
{'date': 'Mon Jul 23 2018 10:17:16.242 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 45
    Museu()
  module <module> line 41
    sala_0 = Sala(R_NORTE, R_LESTE,None, R_OESTE)
  module _spy.vitollino.main line 618
    self.p()
  module _spy.vitollino.main line 640
    self.cenas[cena_a_direita].esquerda = self.cenas[esquerda]
AttributeError: 'NoneType' object has no attribute 'esquerda'
'''},
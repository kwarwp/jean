
{'date': 'Wed Aug 15 2018 11:49:45.526 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 68
    class Codigo(Code):
  module <module> line 69
    _code_.STYLE["visibility"] = "hidden"
NameError: name '_code_' is not defined
'''},
{'date': 'Wed Aug 15 2018 12:09:24.121 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 75
  self.elf.style.visibility = "hidden" if mostra = FALSE else self.elf.style.visibility = "visible" 
                                                          ^
SyntaxError: invalid syntax
'''},
{'date': 'Wed Aug 15 2018 12:13:10.647 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 252
    Museu()
  module <module> line 248
    [Codigo(cena = a,topo = b ,codigo= c, mostra = False, style= STYLE) for a, b , c in MENSAGENS]
  module <module> line 75
    self.elf.style.visibility = "visible" if mostra else "hidden" 
AttributeError: 'Codigo' object has no attribute 'elf'
'''},
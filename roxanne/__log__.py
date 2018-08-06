
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
{'date': 'Mon Jul 23 2018 10:46:50.967 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
RuntimeError: too much recursion
  module '$exec_2443' line 47
        sala_1.norte.vai()
'''},
{'date': 'Mon Jul 23 2018 10:47:05.15 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
RuntimeError: too much recursion
  module '$exec_2487' line 50
Museu()
'''},
{'date': 'Mon Jul 23 2018 10:47:20.398 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
RuntimeError: too much recursion
  module '$exec_2531' line 47
        sala_1.norte.vai()
'''},
{'date': 'Mon Jul 23 2018 10:47:57.561 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
RuntimeError: too much recursion
  module '$exec_2575' line 50
Museu()
'''},
{'date': 'Mon Jul 23 2018 10:50:51.12 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
RuntimeError: too much recursion
  module '$exec_2619' line 47
        sala_1.norte.vai()
'''},
{'date': 'Mon Jul 23 2018 10:50:52.422 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
RuntimeError: too much recursion
  module '$exec_2663' line 50
Museu()
'''},
{'date': 'Mon Jul 23 2018 10:50:53.486 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
RuntimeError: too much recursion
  module '$exec_2707' line 50
Museu()
'''},
{'date': 'Mon Jul 23 2018 11:17:48.62 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 58
  sala_0.norte.meio = sala_1.norte
                    ^
SyntaxError: keyword can't be an expression
'''},
{'date': 'Mon Jul 23 2018 11:17:59.756 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 58
  sala_0.norte.meio = sala_1.norte
                    ^
SyntaxError: keyword can't be an expression
'''},
{'date': 'Mon Jul 23 2018 11:24:23.794 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 67
    Museu()
  module <module> line 60
    sala_1.norte.meio = sala_2.norte
NameError: name 'sala_2' is not defined
'''},
{'date': 'Mon Jul 23 2018 11:28:08.86 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 68
  (__name__="__main__"))
                       ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Jul 23 2018 11:31:24.305 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 67
  if __name__ == '__main__'
                            ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Jul 23 2018 11:31:39.196 GMt-0300 (-03) -X- SuPyGirls -X-',
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
    museu()
NameError: name 'museu' is not defined
'''},
{'date': 'Mon Jul 23 2018 11:31:58.516 GMt-0300 (-03) -X- SuPyGirls -X-',
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
    Museu()
  module <module> line 60
    sala_1.norte.meio = sala_2.norte
NameError: name 'sala_2' is not defined
'''},
{'date': 'Mon Jul 23 2018 11:35:19.936 GMt-0300 (-03) -X- SuPyGirls -X-',
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
    Museu()
  module <module> line 60
    sala_1.norte.meio = sala_2.norte
NameError: name 'sala_2' is not defined
'''},
{'date': 'Mon Jul 23 2018 11:35:21.275 GMt-0300 (-03) -X- SuPyGirls -X-',
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
    Museu()
  module <module> line 60
    sala_1.norte.meio = sala_2.norte
NameError: name 'sala_2' is not defined
'''},
{'date': 'Mon Jul 23 2018 11:56:50.204 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 34
    from _spy.vitollino.main import Sala, STYLE, Mapa
ImportError: cannot import name 'Mapa'

ImportError
Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 264
    action()
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 34
    from _spy.vitollino.main import Sala, STYLE, Mapa
'''},
{'date': 'Mon Jul 23 2018 12:24:50.990 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 78
    Museu()
  module <module> line 68
    mapa = Labirinto.m(
NameError: name 'sala_8' is not defined
'''},
{'date': 'Mon Jul 23 2018 12:25:43.596 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 78
    Museu()
  module <module> line 68
    mapa = Labirinto.m(
NameError: name 'sala_8' is not defined
'''},
{'date': 'Mon Aug 06 2018 17:31:45.946 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 61
    from _spy.vitollino.main import Sala, STYLE, codigo
ImportError: cannot import name 'codigo'

ImportError
Traceback (most recent call last):
  module _core.main line 160
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 306
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 264
    action()
  module _core.supygirls_factory line 295
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 61
    from _spy.vitollino.main import Sala, STYLE, codigo
'''},
{'date': 'Mon Aug 06 2018 17:49:24.82 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 121
  cod = Codigo(cena=sala_1.oeste, topo = "hello",codigo = "if True:print('ooi'),style = dict(width=400,heigth="250px",left=500,top=100))
                                                                                                                ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Aug 06 2018 18:32:34.623 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 121
  Mensagens=[
                                                                                               ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Aug 06 2018 18:32:57.393 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 121
  MENSAGENS=[
                                                                                               ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Aug 06 2018 18:34:04.434 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 126
  MENSAGENS=[
                                                                                               ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Aug 06 2018 18:34:28.398 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 133
  STYLE = dict(width=400,heigth="250px",left=500,top=100))
                                                         ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Aug 06 2018 18:34:37.331 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 126
    MENSAGENS=[
NameError: name 'sala_0' is not defined
'''},
{'date': 'Mon Aug 06 2018 18:36:11.196 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 136
    Museu()
  module <module> line 126
    MENSAGENS=[
AttributeError: 'Sala' object has no attribute 'este'
'''},
{'date': 'Mon Aug 06 2018 18:36:40.581 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 136
    Museu()
  module <module> line 126
    MENSAGENS=[
AttributeError: 'Sala' object has no attribute 'este'
'''},
{'date': 'Mon Aug 06 2018 18:40:00.829 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 136
    Museu()
  module <module> line 126
    MENSAGENS=[
AttributeError: 'Sala' object has no attribute 'este'
'''},
{'date': 'Mon Aug 06 2018 18:43:41.427 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 136
    Museu()
  module <module> line 126
    MENSAGENS=[
AttributeError: 'Sala' object has no attribute 'este'
'''},
{'date': 'Mon Aug 06 2018 19:35:23.53 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 126
  MENSAGENS=[
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Aug 06 2018 19:35:53.657 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 126
  MENSAGENS=[
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ^
SyntaxError: invalid syntax
'''},
{'date': 'Mon Aug 06 2018 19:36:42.473 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 126
  MENSAGENS=[
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           ^
SyntaxError: invalid syntax
'''},
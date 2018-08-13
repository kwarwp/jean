
{'date': 'Sun Aug 12 2018 22:59:58.209 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
'error': '''
 module <string> line 60
  def mouse_over(self, ev):
  ^
IndentationError: unexpected indent
'''},
{'date': 'Sun Aug 12 2018 23:02:01.993 GMt-0300 (Horário Padrão de Brasília) -X- SuPyGirls -X-',
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
  module <module> line 173
    Bloco(FLORESTA)
  module <module> line 147
    Folha(self, pos//4, pos%4, int(tx)//4, int(tx)%4)
  module <module> line 53
    self.folha = html.DIV(Id=fid, style=style, draggable= true) #Esse draggable true é apenas para aparência       
NameError: name 'true' is not defined
'''},
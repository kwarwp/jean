
{'date': 'Mon Sep 03 2018 12:27:54.857 GMt-0300 (-03) -X- SuPyGirls -X-',
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
  module <module> line 429
    Museu()
  module <module> line 160
    video=Video(source="https://www.w3schools.com/html/mov_bbb.mp4",width="320", height="240",top=0, 
NameError: name 'Video' is not defined
'''},
import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDD(self):
        lista = list()
        for el in lista:
            self._view.dd.options.append(ft.dropdown.Option(text=el.id,
                                                 data=el,
                                                 on_click=self.pickEl))
    def pickEl(self, e):
        self.el = e.control.value
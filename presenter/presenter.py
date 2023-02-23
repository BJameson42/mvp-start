from __future__ import annotations

from typing import Protocol

from model.model import Model


class View(Protocol):
    def create_ui(self, presenter: Presenter) -> None:
        ...

    def mainloop(self) -> None:
        ...

    def required_method1(self) -> None:
        ...

    def required_method2(self) -> None:
        ...

        


class Presenter:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def handler1(self, event=None) -> None:
        pass

    def handler2(self, event=None) -> None:
        pass

    
    def run(self) -> None:
        self.view.create_ui(self)
        self.view.mainloop()
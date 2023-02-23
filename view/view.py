import tkinter as tk
from tkinter import ttk
from typing import Protocol

TITLE = "My MVP App"

class Presenter(Protocol):
    def handler1(self, event=None) -> None:
        ...

    def handler2(self, event=None) -> None:
        ...

        


class View(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title(TITLE)
        self.geometry("500x500")
        

    def create_ui(self, presenter: Presenter) -> None:
        self.label = ttk.Label(self)
        self.label.config(text="Test")
        self.label.pack()

    def required_method1(self) -> None:
        pass

    def required_method2(self) -> None:
        pass
        
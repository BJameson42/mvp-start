from model.model import Model
from view.view import View
from presenter.presenter import Presenter

def main() -> None:
    model = Model()
    view = View()
    presenter = Presenter(model, view)
    presenter.run()

if __name__ == "__main__":
    main()

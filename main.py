from Repository import InMemoryRepository
from Controller import Controller
from UI import UI
# from tests.validations_test import

if __name__ == '__main__':
    repository = InMemoryRepository()
    controller = Controller(repository)
    ui = UI(controller)
    ui.run()

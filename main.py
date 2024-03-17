from BookRepository import BookRepository
from BookController import BookController
from UI import UI
# from tests.validations_test import

if __name__ == '__main__':
    repository = BookRepository()
    controller = BookController(repository)
    ui = UI(controller)
    ui.run()

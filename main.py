from BookRepository import BookRepository
from BookController import BookController
from UserRepository import UserRepository
from UserController import UserController
from UI import UI


if __name__ == '__main__':
    book_repository = BookRepository()
    book_controller = BookController(book_repository)

    user_repository = UserRepository()
    user_controller = UserController(user_repository)

    ui = UI(book_controller, user_controller)
    ui.run()

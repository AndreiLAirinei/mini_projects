from Repository import InMemoryRepository
from Controller import Controller
from UI import UI

if __name__ == '__main__':
    repository = InMemoryRepository()
    controller = Controller(repository)
    ui = UI(controller)

    # Examples
    # initial_books = [
    #     Book(title="The Great Gatsby", author="F. Scott Fitzgerald", publisher="Scribner", isbn="978-0-7432-7356-5",
    #          publication_year=1925, stock=10),
    #     Book(title="To Kill a Mockingbird", author="Harper Lee", publisher="J.B. Lippincott & Co.",
    #     isbn="0-06-112008-1", publication_year=1960,  stock=8)
    # ]8

    ui.run()

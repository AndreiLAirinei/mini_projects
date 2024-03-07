from Repository import InMemoryRepository
from Controller import Controller

if __name__ == '__main__':
    repository = InMemoryRepository()
    controller_instance = Controller(repository)

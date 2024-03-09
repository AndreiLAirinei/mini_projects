

class UI:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        while True:
            self.print_menu()
            user_input = int(input("Please input the option: "))

            try:
                if user_input == 1:
                    print("Book details:")
                    self.create()
                elif user_input == 2:
                    print("All book entries:\n")
                    self.controller.read_all()
                elif user_input == 3:
                    isbn = input("Enter the ISBN: \n")
                    self.controller.read_by_id(isbn)
                elif user_input == 4:
                    self.update()
                elif user_input == 5:
                    isbn = input("Enter the ISBN: \n")
                    deleted_book = self.controller.delete(isbn)
                    print("Deleted Book:", deleted_book)
                elif user_input == 6:
                    break
                else:
                    print("Invalid choice. Please try again.")

            except ValueError:
                print("Invalid input. Please enter a valid option.")

    @staticmethod
    def print_menu():
        print("\n")
        print("1. Create entry")
        print("2. Read all entries")
        print("3. Read entry by ISBN")
        print("4. Update entry by ISBN")
        print("5. Delete entry by ISBN")
        print("6. Exit")

    def create(self):
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        publisher = input("Enter the publisher: ")
        isbn = input("Enter the ISBN: ")
        publication_year = int(input("Enter the publication year: "))
        stock = int(input("Enter the stock: "))

        self.controller.create(title, author, publisher, isbn, publication_year, stock)
        print("Book created successfully.")

    def update(self):
        title = input("Enter the updated title: ")
        author = input("Enter the updated author: ")
        publisher = input("Enter the updated publisher: ")
        isbn = input("Enter the ISBN of the book to update: ")
        publication_year = int(input("Enter the updated publication year: "))
        stock = int(input("Enter the updated stock: "))

        self.controller.update(title, author, publisher, isbn, publication_year, stock)
        print("Book updated successfully.")

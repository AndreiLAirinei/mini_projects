

class UI:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        while True:
            self.print_menu()
            user_input = int(input("Please input the option: "))

            if user_input == 1:
                self.create_entry()

            elif user_input == 2:
                self.read_all_entries()

            elif user_input == 3:
                self.read_entry_by_id()

            elif user_input == 4:
                self.update_entry_by_id()

            elif user_input == 5:
                self.delete_entry_by_id()

            elif user_input == 6:
                break

            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def print_menu():

        print("\n")
        print("1. Create entry")
        print("2. Read all entries")
        print("3. Read entry by ID")
        print("4. Update entry by ID")
        print("5. Delete entry by ID")
        print("6. Exit")

    def create_entry(self):
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        publisher = input("Enter the publisher: ")
        isbn = input("Enter the ISBN: ")
        publication_year = input("Enter the publication year: ")
        stock = int(input("Enter the stock: "))

        if self.controller.create_book(title, author, publisher, publication_year, isbn, stock):
            print("Book created successfully.")
        else:
            print("Error creating the book. Please try again.")

    def read_all_entries(self):
        entries = self.controller.read_all_books()
        if entries:
            print("All book entries:\n")
            for entry in entries:
                print(entry)
        else:
            print("No book entries found.")

    def read_entry_by_id(self):
        book_id = int(input("Enter the ID: "))
        book = self.controller.read_book_by_id(book_id)
        if book:
            print(book)
        else:
            print(f"Book with ID {book_id} not found.")

    def update_entry_by_id(self):
        book_id = int(input("Enter the ID of the book to update: "))
        title = input("Enter the updated title: ")
        author = input("Enter the updated author: ")
        publisher = input("Enter the updated publisher: ")
        isbn = input("Enter the ISBN of the book to update: ")
        publication_year = int(input("Enter the updated publication year: "))
        stock = int(input("Enter the updated stock: "))

        if self.controller.update_book(book_id, title, author, publisher, publication_year, isbn, stock):
            print("Book updated successfully.")
            return True
        else:
            print("Error updating the book. Please try again.")
            return False

    def delete_entry_by_id(self):
        book_id = int(input("Enter the ID of the book to delete: "))
        deleted = self.controller.delete_book(book_id)
        if deleted:
            print(f"Book with ID {book_id} deleted successfully.")
        else:
            print(f"Book with ID {book_id} not found or could not be deleted.")

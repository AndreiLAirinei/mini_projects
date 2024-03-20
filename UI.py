

class UI:
    def __init__(self, book_controller, user_controller):
        self.book_controller = book_controller
        self.user_controller = user_controller

    def run(self):
        while True:
            self.print_menu()
            user_input = int(input("Please input the option: "))

            if user_input == 1:
                self.handle_book_menu()
            elif user_input == 2:
                self.handle_user_menu()
            elif user_input == 3:
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def print_menu():
        print("\n")
        print("1. Enter book menu")
        print("2. Enter user menu")
        print("3. Exit the application")

    def handle_book_menu(self):
        while True:
            self.print_book_menu()
            user_input = int(input("Please input the option: "))

            if user_input == 1:
                self.create_book_entry()
            elif user_input == 2:
                self.read_all_book_entries()
            elif user_input == 3:
                self.read_book_entry_by_id()
            elif user_input == 4:
                self.update_book_entry_by_id()
            elif user_input == 5:
                self.delete_book_entry_by_id()
            elif user_input == 6:
                break
            else:
                print("Invalid choice. Please try again.")

    def handle_user_menu(self):
        while True:
            self.print_user_menu()
            user_input = int(input("Please input the option: "))

            if user_input == 1:
                self.create_user_entry()
            elif user_input == 2:
                self.read_all_user_entries()
            elif user_input == 3:
                self.read_user_entry_by_id()
            elif user_input == 4:
                self.update_user_entry_by_id()
            elif user_input == 5:
                self.delete_user_entry_by_id()
            elif user_input == 6:
                break
            else:
                print("Invalid choice. Please try again.")

    @staticmethod
    def print_book_menu():
        print("\n")
        print("1. Create book entry")
        print("2. Read all book entries")
        print("3. Read book entry by ID")
        print("4. Update book entry by ID")
        print("5. Delete book entry by ID")
        print("6. Exit book menu")
        print("\n")

    @staticmethod
    def print_user_menu():
        print("\n")
        print("1. Create user entry")
        print("2. Read all user entries")
        print("3. Read user entry by ID")
        print("4. Update user entry by ID")
        print("5. Delete user entry by ID")
        print("6. Exit user menu")
        print("\n")

    def create_book_entry(self):
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        publisher = input("Enter the publisher: ")
        isbn = input("Enter the ISBN: ")
        publication_year = int(input("Enter the publication year: "))
        stock = int(input("Enter the stock: "))

        if self.book_controller.create_book(title, author, publisher, publication_year, isbn, stock):
            print("Book created successfully.")
        else:
            print("Error creating the book. Please try again.")

    def read_all_book_entries(self):
        entries = self.book_controller.read_all_books()
        if entries:
            print("All book entries:\n")
            for entry in entries:
                print(entry)
        else:
            print("No book entries found.")

    def read_book_entry_by_id(self):
        book_id = int(input("Enter the ID: "))
        book = self.book_controller.read_book_by_id(book_id)
        if book:
            print(book)
        else:
            print(f"Book with ID {book_id} not found.")

    def update_book_entry_by_id(self):
        book_id = int(input("Enter the ID of the book to update: "))
        title = input("Enter the updated title: ")
        author = input("Enter the updated author: ")
        publisher = input("Enter the updated publisher: ")
        isbn = input("Enter the ISBN of the book to update: ")
        publication_year = int(input("Enter the updated publication year: "))
        stock = int(input("Enter the updated stock: "))

        if self.book_controller.update_book(book_id, title, author, publisher, publication_year, isbn, stock):
            print("Book updated successfully.")
            return True
        else:
            print("Error updating the book. Please try again.")
            return False

    def delete_book_entry_by_id(self):
        book_id = int(input("Enter the ID of the book to delete: "))
        deleted = self.book_controller.delete_book(book_id)
        if deleted:
            print(f"Book with ID {book_id} deleted successfully.")
        else:
            print(f"Book with ID {book_id} not found or could not be deleted.")

    def create_user_entry(self):
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        address = input("Enter the address: ")

        if self.user_controller.create_user(first_name, last_name, address):
            print("User created successfully.")
        else:
            print("Error creating the user. Please try again.")

    def read_all_user_entries(self):
        entries = self.user_controller.read_all_users()
        if entries:
            print("All user entries:\n")
            for entry in entries:
                print(entry)
        else:
            print("No user entries found.")

    def read_user_entry_by_id(self):
        user_id = int(input("Enter the user ID: "))
        user = self.user_controller.read_user_by_id(user_id)
        if user:
            print(user)
        else:
            print(f"User with ID {user_id} not found.")

    def update_user_entry_by_id(self):
        user_id = int(input("Enter the user ID: "))
        first_name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        address = input("Enter the address: ")

        if self.user_controller.update_user(user_id, first_name, last_name, address):
            print("User updated successfully.")
            return True
        else:
            print("Error updating the user. Please try again.")
            return False

    def delete_user_entry_by_id(self):
        user_id = int(input("Enter the user ID: "))

        if self.user_controller.delete_user(user_id):
            print("User deleted successfully.")
        else:
            print("Error deleting the user. Please try again.")

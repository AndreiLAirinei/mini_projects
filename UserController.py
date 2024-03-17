from user_model import User
from exceptions import IDNotFound


class UserController:

    def __init__(self, repository):
        self.repository = repository

    def create_user(self, first_name, last_name, address):
        instance = User(first_name, last_name, address)
        self.repository.user_create(instance)

    def read_all_users(self):
        return self.repository.user_read_all()

    def read_user_by_id(self, user_id):
        try:
            if not self.repository.user_id_exists(user_id):
                raise IDNotFound(user_id)
            else:
                self.repository.user_read_by_id(user_id)
        except IDNotFound as error:
            print(str(error))

    def update_user(self, user_id, first_name, last_name, address):
        try:
            if not self.repository.user_id_exists(user_id):
                raise IDNotFound(user_id)

            updated_user = User(first_name, last_name, address)

            # Validation
            if updated_user:
                return self.repository.user_update(user_id)
            else:
                raise Exception

        except (IDNotFound, Exception) as error:
            print(str(error))

    def delete_user(self, user_id):
        try:
            if not self.repository.user_id_exists(user_id):
                raise IDNotFound(user_id)
            else:
                return self.repository.user_delete(user_id)
        except IDNotFound as error:
            print(str(error))

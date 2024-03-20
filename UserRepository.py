
class UserRepository:

    def __init__(self):
        self.data = []
        self.last_user_id = 0

    def user_create(self, instance):
        self.last_user_id += 1
        instance.user_id = self.last_user_id
        self.data.append(instance)
        return True

    def user_read_all(self):
        return self.data

    def user_read_by_id(self, user_id):
        for user in self.data:
            if user.user_id == user_id:
                return user
        return None

    def user_update(self, user_id, user):
        if not self.data:
            return False

        for index, existing_user in enumerate(self.data):
            if existing_user.user_id == user_id:
                self.data[index] = user
                return True
        return False

    def user_delete(self, user_id):
        if not self.data:
            return False

        for index, existing_user in enumerate(self.data):
            if existing_user.user_id == user_id:
                del self.data[index]
                return True
        return False

    def user_id_exists(self, user_id):
        for user in self.data:
            if user.user_id == user_id:
                return True
        return False

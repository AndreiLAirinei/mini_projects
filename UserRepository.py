
class UserRepository:

    def __init__(self):
        self.data = []
        self.last_user_id = 0

    def user_create(self, instance):
        self.last_user_id += 1
        instance.user_id = self.last_user_id
        self.data.append(instance)

    def user_read_all(self):
        return self.data

    def user_read_by_id(self, user_id):
        for user in self.data:
            if user.user_id == user_id:
                return user
        return None

    def update(self, user_id, user):
        if not self.data:
            return False

        for i, existing_user in enumerate(self.data):
            if existing_user.user_id == user_id:
                self.data[i] = user
                return True
        return False

    def delete(self, user_id):
        if not self.data:
            return False

        for i, existing_user in enumerate(self.data):
            if existing_user.user_id == user_id:
                del self.data[i]
                return True
        return False

    def id_exists(self, user_id):
        for user in self.data:
            if user.user_id == user_id:
                return True
        return False

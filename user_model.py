

class User:
    _id_counter = 0  # Initializing counter

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 address: str
                 ):
        self.user_id = User._id_counter + 1  # Increment the user_id counter
        User._id_counter += 1  # Increment for next iteration
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Address: {self.address}"

    # @property
    # def full_name(self):
    #     return f"{self.first_name} {self.last_name}"

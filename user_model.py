

class User:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 address: str
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

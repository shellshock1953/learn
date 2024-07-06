from class_user import User

class Admin(User):
    def __init__(self, name, privileges=[]) -> None:
        super().__init__(name)
        self.privileges = Privileges(privileges)


class Privileges:
    def __init__(self, privileges: list) -> None:
        self.privileges = privileges

    def show_privileges(self):
        print(f"has next privileges: {self.privileges}")

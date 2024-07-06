class User:
    def __init__(self, name) -> None:
        self.name = name

    def greeting(self):
        print(f"Hello {self.name}")



from random import randint

class Die:
    def __init__(self, sides: int) -> None:
        self.sides = sides

    def roll_die(self):
        print(f"die with {self.sides} sides: {randint(1, self.sides)}")

six = Die(6)
six.roll_die()


ten = Die(10)
ten.roll_die()

twenty = Die(20)
twenty.roll_die()
